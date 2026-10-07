# Tech Feed Podcast

Turns the latest TechCrunch articles into a short spoken podcast episode. Everything runs locally.

1. Reads the TechCrunch RSS feed and extracts the text of the top articles.
2. Summarizes each article into a ~20-second TLDR using a local LLM (Ollama, `llama3.1`).
3. Converts the combined script to speech with Kokoro TTS and saves it as `YYYY-MM-DD.wav`.

## Requirements

- Python 3.12
- [Ollama](https://ollama.com) installed and running, with the model pulled:
  ```bash
  ollama pull llama3.1
  ```

## Setup

```bash
python -m venv venv
source ./venv/Scripts/activate   # Windows (Git Bash); use venv/bin/activate on macOS/Linux
pip install -r requirements.txt
```

The first run downloads the Kokoro model (~300MB).

## Usage

```bash
./run.sh
```

or, with the venv activated:

```bash
python script.py
```

The episode is written to the project root as `<today's date>.wav`.

## Configuration

Edit the constants at the top of [script.py](script.py):

- `FEED_URL`: RSS feed to read
- `MAX_ARTICLES`: number of articles to include (default 5)
- `MAX_CHARS`: max characters of each article sent to the LLM (default 6000, sized for the 8192-token context set in `llm.py`)

## Project layout

- [script.py](script.py): main pipeline (feed, extraction, summarize, audio)
- [llm.py](llm.py): `write_script()` summarizes an article via Ollama and cleans the output for speech. Can also be run standalone: `python llm.py "article text"`
- [audio_generator.py](audio_generator.py): `create_audio()` turns a script into a WAV file with Kokoro
- [tts_demo.py](tts_demo.py): minimal Kokoro example
- [run.sh](run.sh): activates the venv and runs the pipeline
