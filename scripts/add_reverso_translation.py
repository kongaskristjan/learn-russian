
from pathlib import Path
import os

import fire
from reverso_api.context import ReversoContextAPI

from src.file_io import read_words, write_words, Word

def main(inp: str, out: str) -> None:
    inp, out = Path(inp), Path(out)
    words = read_words(inp.read_text())
    for word in words:
        translation_str = get_translations(word.word)
        if translation_str is not None:
            word.translation = translation_str
        print(f"Translated {word.word} to {word.translation}")

    os.makedirs(out.parent, exist_ok=True)
    out.write_text(write_words(words))


def get_translations(word: str) -> str|None:
    translations = ReversoContextAPI(word, "", "ru", "en").get_translations()
    translations = list(translations)
    if len(translations) == 0:
        return None
    
    translations.sort(key=lambda x: x.frequency, reverse=True)

    strs = []
    max_frequency = translations[0].frequency
    for index, (source_word, translation, frequency, part_of_speech, inflected_forms) in enumerate(translations):
        if frequency < 0.25 * max_frequency or index >= 3:
            break
        strs.append(translation)
    
    translation_str = ", ".join(strs)
    return translation_str


if __name__ == "__main__":
    fire.Fire(main)
