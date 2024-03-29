from src.lib.file_io import Word


def ask_word(word: Word, to_english: bool = False) -> bool:
    """Ask a word and return whether the user answered correctly."""
    word_str = word.word if to_english else word.translation
    translation_str = word.translation if to_english else word.word

    answer = input(f"{word_str}: ")
    correct = answer.strip() == translation_str.strip()

    print()
    if correct:
        print("+++              CORRECT              +++")
    else:
        print("---               WRONG               ---" + f"    (correct answer: {translation_str})")
    print()
    return correct


def clear_screen(prompt: bool = True):
    if prompt:
        print()
        input("Press enter to continue...")
    print("\n" * 100)


def show_words_to_repeat(removed_words: set[str], words: list[Word], to_english: bool):
    # Find max length of words
    max_len = max([len(word.word) for word in words if word.word not in removed_words])

    print("\n-------------------------------------------\n")
    print("Words to repeat:")
    for word in words:
        if word.word not in removed_words:
            word_str = word.word if to_english else word.translation
            translation_str = word.translation if to_english else word.word
            print(f"{word_str:{max_len}}   {translation_str}")
    print("\n-------------------------------------------\n")
    print(f"Progress: {len(removed_words)}/{len(words)}")
