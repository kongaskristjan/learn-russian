
from pathlib import Path

def main() -> None:
    """A program to learn russian words from their translations."""
    ask_schedule = [0, 20, 50, 150, 500]

    words = load_words(Path("data/words.csv"))
    progress = load_progress(Path("data/progress.txt"))
    while word := get_next_word(words, progress, ask_schedule):
        if ask_word(words[word]):
            progress.append(word)
            save_progress(progress, Path("data/progress.txt"))
            save_progress(progress, Path("data/progress.txt.bak"))
        print(f"Total progress: {len(progress)}/{len(words) * len(ask_schedule)}")
    print(f"Congratulations! You have learned all {len(words)} words!")


if __name__ == "__main__":
    main()
