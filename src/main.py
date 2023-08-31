import os
from pathlib import Path

from src.lib.algorithm import WordChoiceAlgorithm
from src.lib.file_io import read_progress, read_words, write_progress
from src.lib.user_io import ask_word

def main() -> None:
    """A program to learn russian words from their translations."""
    words_path = Path("data/words.csv")
    progress_path = Path("progress/progress.txt")
    progress_bak_path = Path("progress/progress.txt.bak")
    os.makedirs(progress_path.parent, exist_ok=True)

    algorithm = get_word_choice_algorithm(words_path, progress_path)
    while word := algorithm.get_next_word():
        correct = ask_word(word)
        algorithm.update_progress(word.word, correct)
        progress_path.write_text(write_progress(algorithm.progress))
        progress_bak_path.write_text(write_progress(algorithm.progress))
        correct_count = len([entry for entry in algorithm.progress if entry.correct])
        print(f"Total progress: {correct_count}/{len(algorithm.words) * len(algorithm.ask_schedule)}")
        print()
    print(f"Congratulations! You have learned all {len(algorithm.words)} words!")


def get_word_choice_algorithm(words_path: Path, progress_path: Path) -> WordChoiceAlgorithm:
    """Return an algorithm to choose words to ask."""
    ask_schedule = [0, 20, 50, 150, 500]
    false_answer_delay = 5

    words = read_words(words_path.read_text())
    progress = read_progress(progress_path.read_text()) if progress_path.exists() else []
    return WordChoiceAlgorithm(words, progress, ask_schedule, false_answer_delay)


if __name__ == "__main__":
    main()
