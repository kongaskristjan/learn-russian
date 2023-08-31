
from src.lib.file_io import Word

def ask_word(word: Word) -> bool:
    """Ask a word and return whether the user answered correctly."""
    answer = input(f"{word.translation} ({word.part_of_speech}): ")
    correct = answer == word.word
    print()
    print()
    if correct:
        print("+++              CORRECT              +++")
    else:
        print("---               WRONG               ---" + f"    (correct answer: {word.word})")
    print()
    print(f"{word.word}: {word.example}")
    print()
    print()
    return correct
