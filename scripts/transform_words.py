
import os
from pathlib import Path
from src.file_io import write_words, Word

def read_words_from_lines(input: str) -> list[Word]:
    """Read words from a string containing lines of text.

    Word, translation, and its part of speech are returned.
    """
    lines = input.splitlines()
    words = []
    for i in range(0, len(lines), 3):
        words.append(Word(lines[i+1].strip(), lines[i+2].split("\t")[0].strip(), lines[i+2].split("\t")[-1].strip()))
    return words

def main():
    all_words: list[Word] = []

    lessons_path = Path(".lessons")
    paths = [path for path in lessons_path.iterdir()]
    paths = sorted(paths, key=lambda path: int(path.stem.split("-")[0]))
    for lesson in paths:
        print(lesson)
        input = lesson.read_text()
        words = read_words_from_lines(input)
        all_words.extend(words)

    output = write_words(all_words)
    os.makedirs("data", exist_ok=True)
    Path("data/words.csv").write_text(output)

if __name__ == "__main__":
    main()
