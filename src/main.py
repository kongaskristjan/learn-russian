
from pathlib import Path
from src.file_io import read_words, read_progress, write_progress

def main() -> None:
    """A program to learn russian words from their translations."""
    ask_schedule = [0, 20, 50, 150, 500]
    words_path = Path("data/words.csv")
    progress_path = Path("data/progress.txt")
    progress_bak_path = Path("data/progress.txt.bak")

    words = read_words(words_path.read_text())
    progress = read_progress(progress_path.read_text()) if progress_path.exists() else []
    while word := get_next_word(words, progress, ask_schedule):
        if ask_word(words[word]):
            progress.append(word)
            progress_path.write_text(write_progress(progress))
            progress_bak_path.write_text(write_progress(progress))
        print(f"Total progress: {len(progress)}/{len(words) * len(ask_schedule)}")
    print(f"Congratulations! You have learned all {len(words)} words!")


if __name__ == "__main__":
    main()
