
import os
from pathlib import Path

def read_words_from_lines(input: str) -> list[tuple[str, str, str]]:
    """Read words from a string containing lines of text.

    Word, translation, and its part of speech are returned.
    """
    lines = input.splitlines()
    words = []
    for i in range(0, len(lines), 3):
        words.append((lines[i+1].strip(), lines[i+2].split("\t")[0].strip(), lines[i+2].split("\t")[-1].strip()))
    return words

def write_words_to_csv_str(words: list[tuple[str, str, str]]) -> str:
    """Write words to a string containing CSV data.

    Word, translation, and its part of speech are written.
    """
    output = ""
    for word in words:
        output += f"{word[0]};{word[1]};{word[2]}\n"
    return output

def main():
    all_words = []

    lessons_path = Path(".lessons")
    paths = [path for path in lessons_path.iterdir()]
    paths = sorted(paths, key=lambda path: int(path.stem.split("-")[0]))
    for lesson in paths:
        print(lesson)
        input = lesson.read_text()
        words = read_words_from_lines(input)
        all_words += words

    output = write_words_to_csv_str(all_words)
    os.makedirs("data", exist_ok=True)
    Path("data/words.csv").write_text(output)

if __name__ == "__main__":
    main()
