import copy
import random
from pathlib import Path

import fire

from src.lib.file_io import (
    HistoryEntry,
    Word,
    read_progress,
    read_words,
    write_progress,
)
from src.lib.user_io import ask_word, clear_screen


def main(lesson_size: int = 15) -> None:
    """A program to learn russian words from their translations."""
    words_path = Path("data/words.csv")
    progress_path = Path("progress/progress_lessons.txt")

    progress = read_progress(progress_path.read_text()) if progress_path.exists() else []
    words = get_current_lesson_words(words_path, progress, lesson_size)

    clear_screen()
    print(f"\nTranslate {len(words)} words from russian to english:\n")
    run_lesson(words, to_english=True)

    print()
    for i in range(3):
        print("-------------------------------------------")

    print("\nGreat job! Now let's do the other way around!")
    print(f"Translate {len(words)} words from english to russian:\n")
    run_lesson(words, to_english=False)
    print("\nGreat job! Lesson finished! See you next time!\n")

    progress.extend([HistoryEntry(word.word, True) for word in words])
    progress_path.write_text(write_progress(progress))


def run_lesson(words: list[Word], to_english: bool) -> None:
    """Run a lesson with the given words."""

    words = copy.deepcopy(words)
    removed_words: set[str] = set()
    while len(words) > len(removed_words):
        print("\n-------------------------------------------\n")
        print("Words to repeat:")
        for word in words:
            if word.word not in removed_words:
                word_str = word.word if to_english else word.translation
                translation_str = word.translation if to_english else word.word
                print(f"{word_str} - {translation_str}")
        print("\n-------------------------------------------\n")
        print(f"Progress: {len(removed_words)}/{len(words)}")
        print()
        input("Press enter to continue...")
        clear_screen()

        random.shuffle(words)
        for word in words:
            if word.word in removed_words:
                continue

            correct = ask_word(word, to_english=to_english)
            if correct:
                removed_words.add(word.word)

        input("Press enter to continue...")
        clear_screen()


def get_current_lesson_words(words_path: Path, progress: list[HistoryEntry], lesson_size: int) -> list[Word]:
    """Return a list of words for the current lesson."""
    words = read_words(words_path.read_text())
    entries = [entry.word for entry in progress if entry.correct]
    remaining_words = [word for word in words if word.word not in entries]

    return remaining_words[:lesson_size]


if __name__ == "__main__":
    fire.Fire(main)
