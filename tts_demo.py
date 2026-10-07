import soundfile as sf
from kokoro import KPipeline

# 1. Initialize the pipeline with a language code
# 'a' stands for American English, 'b' stands for British English
pipeline = KPipeline(lang_code='a')

text = "Hello! This is a quick test of the Kokoro text-to-speech engine running locally."

# 2. Generate the speech generator
# 'af_heart' is one of the built-in high-quality female voices
generator = pipeline(text, voice='af_heart', speed=1.0)

# 3. Process the generator chunks and save the output
for i, (graphemes, phonemes, audio) in enumerate(generator):
    # Kokoro natively outputs audio at a 24000 Hz sample rate
    output_filename = f"output_{i}.wav"
    sf.write(output_filename, audio, 24000)
    print(f"Saved chunk {i} to {output_filename}")
