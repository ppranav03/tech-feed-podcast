import re
import sys

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    num_ctx=8192
)


def clean_script(text):
    # Drop a leading preamble line like "Here's a TLDR summary:"
    text = re.sub(r"^\s*here(?:'s| is)[^\n]*:\s*\n", "", text, flags=re.IGNORECASE)
    # Strip markdown headings, bullets, bold/italics and stray asterisks/underscores
    text = re.sub(r"^\s*#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*•]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_]{1,3}", "", text)
    return text.strip()


def write_script(user_text):
    messages = [
        SystemMessage(content="""
        You are a helpful assistant and you will be given an article and
        summarize it into a 20-second read adopting a TLDR format.

        Your output will be read aloud by a text-to-speech engine, so write plain spoken text only:
        no markdown, asterisks, headings, bullet points, or emojis.
        Do not add any preamble like "Here's a summary"; start directly with the script.

        The dialogue should be upbeat yet informational, adopting a style similar to NPR's Up-First podcast.
        """),
        HumanMessage(content=user_text)
    ]

    response = llm.invoke(messages)
    return clean_script(response.content)


if __name__ == "__main__":
    user_text = " ".join(sys.argv[1:]) or input("Enter a topic: ")
    print(write_script(user_text))
