import argparse
import configparser
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def load_settings(path: Path):
    config = configparser.ConfigParser()
    config.read(path)
    section = config["openai"] if "openai" in config else {}
    return {
        "model": section.get("model", "tts-1-hd"),
        "voice": section.get("voice", "alloy"),
        "response_format": section.get("response_format", "mp3"),
        "language": section.get("language", ""),
        "speed": float(section.get("speed", "1.0")),
    }


def convert_files(target_dir: Path, output_dir: Path, settings: dict):
    client = OpenAI()
    output_dir.mkdir(parents=True, exist_ok=True)
    for txt_file in target_dir.glob("*.txt"):
        ext = settings["response_format"]
        # Skip if output already exists
        if list(output_dir.glob(f"{txt_file.stem}*.{ext}")):
            print(f"Skip {txt_file.name}: output already exists")
            continue
        print(f"Processing {txt_file.name}")
        text = txt_file.read_text(encoding="utf-8")
        max_length = 4096
        chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
        for idx, chunk in enumerate(chunks):
            options = dict(
                model=settings["model"],
                voice=settings["voice"],
                input=chunk,
                response_format=settings["response_format"],
                speed=settings["speed"],
            )
            response = client.audio.speech.create(**options)
            ext = settings["response_format"]
            if len(chunks) == 1:
                out_path = output_dir / f"{txt_file.stem}.{ext}"
            else:
                out_path = output_dir / f"{txt_file.stem}_{idx+1}.{ext}"
            with open(out_path, "wb") as f:
                f.write(response.content)
            print(f"Saved {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert text files to speech using OpenAI TTS")
    parser.add_argument("--target", default="target", help="folder containing .txt files")
    parser.add_argument("--audio", default="audio", help="folder to save audio files")
    parser.add_argument("--setting", default="setting.ini", help="path to setting.ini")
    args = parser.parse_args()

    load_dotenv()
    settings = load_settings(Path(args.setting))
    convert_files(Path(args.target), Path(args.audio), settings)


if __name__ == "__main__":
    main()
