# Text to Speech Converter

This project converts `.txt` files in the specified directory into audio files using OpenAI's high quality Text-to-Speech API.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and set your OpenAI API key:
   ```bash
   cp .env.example .env
   # then edit .env and set your key
   ```
3. Adjust `setting.ini` to select model, voice, language and paths.
4. Place your `.txt` files into the `target` directory (or specify another via `--target` or in `setting.ini`).
5. Run the converter:
   ```bash
   python convert.py --target target --audio audio --setting setting.ini
   ```
   Audio files will be generated in the output directory.
6. Concatenate the generated audio files:
   ```bash
   python concat_audio.py --setting setting.ini
   ```
   This creates `combined.mp3` in the directory specified by `audio_concat`.

Path options can also be set in the `[paths]` section of `setting.ini`. Command
line arguments take precedence over the config file values, which in turn
override the built-in defaults.

