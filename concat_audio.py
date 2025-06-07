import argparse
import configparser
from pathlib import Path

from pydub import AudioSegment


def load_concat_dir(path: Path) -> tuple[Path, str]:
    config = configparser.ConfigParser()
    config.read(path)
    paths_sec = config["paths"] if "paths" in config else {}
    openai_sec = config["openai"] if "openai" in config else {}
    audio_dir = Path(paths_sec.get("audio_concat", "audio"))
    ext = openai_sec.get("response_format", "mp3")
    return audio_dir, ext


def concat_audio(audio_dir: Path, ext: str) -> None:
    audio_files = sorted(audio_dir.glob(f"*.{ext}"))
    if not audio_files:
        print(f"No .{ext} files found in {audio_dir}")
        return

    combined = AudioSegment.empty()
    for f in audio_files:
        combined += AudioSegment.from_file(f)
        print(f"Added {f.name}")

    out_path = audio_dir / f"combined.{ext}"
    combined.export(out_path, format=ext)
    print(f"Saved {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Concatenate audio files in a directory")
    parser.add_argument("--setting", default="setting.ini", help="path to setting.ini")
    args = parser.parse_args()

    audio_dir, ext = load_concat_dir(Path(args.setting))
    concat_audio(audio_dir, ext)


if __name__ == "__main__":
    main()
