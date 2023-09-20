import copy
import random
import time
from pathlib import Path

import fire

from src.lib.file_io import (
    HistoryEntry,
    Word,
    read_progress,
    read_words,
    write_progress,
)
from src.lib.user_io import ask_word, clear_screen, show_words_to_repeat


def main(lesson_size: int = 15, previous: bool = False) -> None:
    """A program to learn russian words from their translations."""
    words_path = Path("data/words.csv")
    progress_path = Path("progress/progress_lessons.txt")

    progress = read_progress(progress_path.read_text()) if progress_path.exists() else []
    words = get_current_lesson_words(words_path, progress, lesson_size, previous)

    t = time.time()

    clear_screen(prompt=False)
    print(f"\nTranslate {len(words)} words from russian to english:")
    run_lesson(words, to_english=True)

    print()
    for i in range(3):
        print("-------------------------------------------")

    print("\nGreat job! Now let's do the other way around!")
    print(f"Translate {len(words)} words from english to russian:\n")
    run_lesson(words, to_english=False)

    if not previous:
        progress.extend([HistoryEntry(word.word, True) for word in words])
        progress_path.write_text(write_progress(progress))

    delta = int(time.time() - t)
    min, sec = delta // 60, delta % 60
    print(f"\nGreat job! Lesson finished in {min} minutes and {sec} seconds! See you next time!\n")
    if not previous:
        print(f"Progress: {len(progress)}/{len(read_words(words_path.read_text()))}")


def run_lesson(words: list[Word], to_english: bool) -> None:
    """Run a lesson with the given words."""

    words = copy.deepcopy(words)
    removed_words: set[str] = set()
    while len(words) > len(removed_words):
        show_words_to_repeat(removed_words, words, to_english)
        clear_screen()

        random.shuffle(words)
        for word in words:
            if word.word in removed_words:
                continue

            correct = ask_word(word, to_english=to_english)
            if correct:
                removed_words.add(word.word)

        clear_screen()


def get_current_lesson_words(
    words_path: Path, progress: list[HistoryEntry], lesson_size: int, previous: bool
) -> list[Word]:
    """Return a list of words for the current lesson."""
    words = read_words(words_path.read_text())
    entries = [entry.word for entry in progress if entry.correct]
    if previous:
        entries = entries[:-lesson_size]
    remaining_words = [word for word in words if word.word not in entries]

    return remaining_words[:lesson_size]


if __name__ == "__main__":
    fire.Fire(main)
