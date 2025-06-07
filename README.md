# Text to Speech Converter

This project converts `.txt` files in the specified directory into audio files using OpenAI's high quality Text-to-Speech API.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in `.env`:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
3. Adjust `setting.ini` to select model, voice, language, etc.
4. Place your `.txt` files into the `target` directory (or specify another with `--target`).
5. Run the converter:
   ```bash
   python convert.py --target target --audio audio --setting setting.ini
   ```
   Audio files will be generated in the output directory.

