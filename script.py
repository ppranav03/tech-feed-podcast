from datetime import date

import feedparser
from trafilatura import extract, fetch_url

from llm import write_script
from audio_generator import create_audio

FEED_URL = "https://techcrunch.com/feed/"
MAX_ARTICLES = 5
MAX_CHARS = 6000  # keeps each prompt well inside the model's 8192-token context


def fetch_article_text(link):
    downloaded = fetch_url(link)
    if not downloaded:
        return None
    return extract(downloaded)


def main():
    articles = feedparser.parse(FEED_URL)

    summaries = []
    for a in articles.entries:
        if len(summaries) >= MAX_ARTICLES:
            break
        print(a.link)
        text = fetch_article_text(a.link)
        if not text:
            print("  skipped: couldn't extract text")
            continue
        summary = write_script(text[:MAX_CHARS])
        print(summary, end="\n\n")
        summaries.append(summary)

    if not summaries:
        print("Couldn't extract any article text.")
        return

    script = "\n\n".join(summaries)
    create_audio(script, filename=f"{date.today()}.wav")


if __name__ == "__main__":
    main()
