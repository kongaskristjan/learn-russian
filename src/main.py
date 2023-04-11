
from pathlib import Path
from src.file_io import read_words, read_progress, write_progress
from src.algorithm import WordChoiceAlgorithm

def get_word_choice_algorithm(words_path: Path, progress_path: Path) -> WordChoiceAlgorithm:
    """Return an algorithm to choose words to ask."""
    ask_schedule = [0, 20, 50, 150, 500]
    false_answer_delay = 20

    words = read_words(words_path.read_text())
    progress = read_progress(progress_path.read_text()) if progress_path.exists() else []
    return WordChoiceAlgorithm(words, progress, ask_schedule, false_answer_delay)

def main() -> None:
    """A program to learn russian words from their translations."""
    words_path = Path("data/words.csv")
    progress_path = Path("data/progress.txt")
    progress_bak_path = Path("data/progress.txt.bak")

    algorithm = get_word_choice_algorithm(words_path, progress_path)
    while word := algorithm.get_next_word():
        correct = ask_word(word)
        algorithm.update_progress(word.word, correct)
        progress_path.write_text(write_progress(algorithm.progress))
        progress_bak_path.write_text(write_progress(algorithm.progress))
        print(f"Total progress: {len(algorithm.progress)}/{len(algorithm.words) * len(algorithm.ask_schedule)}")
    print(f"Congratulations! You have learned all {len(algorithm.words)} words!")


if __name__ == "__main__":
    main()
