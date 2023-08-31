
from src.lib.file_io import Word

def ask_word(word: Word, to_english: bool = False) -> bool:
    """Ask a word and return whether the user answered correctly."""
    word_str = word.word if to_english else word.translation
    translation_str = word.translation if to_english else word.word

    answer = input(f"{word_str} ({word.part_of_speech}): ")
    correct = answer == translation_str.split(",")[0]
    print()
    print()
    if correct:
        print("+++              CORRECT              +++")
    else:
        print("---               WRONG               ---" + f"    (correct answer: {translation_str})")
    #print()
    #print(f"{word_str}: {word.example}")
    print()
    print()
    return correct
