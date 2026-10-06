from datetime import date

import feedparser
from trafilatura import extract, fetch_url

from llm import write_script
from tts_demo import create_audio

articles = feedparser.parse('https://techcrunch.com/feed/')

# print(len(articles.entries))
link = articles.entries[0].link
print(link)

# for a in articles.entries:
#     print(a.link)

downloaded = fetch_url(link)
text = extract(downloaded)

if text:
    script = write_script(text)
    print(script)

    # e.g. .../2026/10/05/lucid-motors-ev-output-falls/ -> 2026-10-06-lucid-motors-ev-output-falls.wav
    slug = link.rstrip("/").split("/")[-1]
    create_audio(script, filename=f"{date.today()}-{slug}.wav")
else:
    print("Couldn't extract article text.")
