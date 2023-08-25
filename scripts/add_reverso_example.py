import os
import time
from pathlib import Path

import fire
from reverso_api.context import ReversoContextAPI

from src.file_io import Word, read_words, write_words


def main(inp: str, out: str) -> None:
    inp, out = Path(inp), Path(out)
    words = read_words(inp.read_text())
    for i, word in enumerate(words):
        word.example = get_example(word.word)
        print(f"{i} - {word.word}: {word.example}")
        time.sleep(5)  # to avoid getting blocked by Reverso

    os.makedirs(out.parent, exist_ok=True)
    out.write_text(write_words(words))


def get_example(word: str) -> str:
    api = ReversoContextAPI(word, "", "ru", "en")
    examples = api.get_examples()
    try:
        example = next(examples, None)
    except Exception:
        example = None

    if not example:
        return ""
    return example[0].text


if __name__ == "__main__":
    fire.Fire(main)
