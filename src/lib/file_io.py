class Word:
    def __init__(self, word: str, translation: str, example: str, example_translation: str):
        self.word = word
        self.translation = translation
        self.example = example
        self.example_translation = example_translation

    def __repr__(self):
        return f"({self.word}; {self.translation}; {self.example}; {self.example_translation})"

    def __eq__(self, other: "Word"):
        return (
            self.word == other.word
            and self.translation == other.translation
            and self.example == other.example
            and self.example_translation == other.example_translation
        )


class HistoryEntry:
    def __init__(self, word: str, correct: bool):
        self.word = word
        self.correct = correct

    def __repr__(self):
        return f"('{self.word}';{self.correct})"

    def __eq__(self, other):
        return self.word == other.word and self.correct == other.correct


def read_progress(progress: str) -> list[HistoryEntry]:
    """Read progress from a string containing CSV data."""
    progress_lines = progress.splitlines()
    entries = [e.split(";") for e in progress_lines]
    entries = [HistoryEntry(e[0], e[1] == "True") for e in entries]
    return entries


def write_progress(progress: list[HistoryEntry]) -> str:
    """Write progress to a string containing CSV data."""
    return "\n".join([f"{e.word};{e.correct}" for e in progress])


def read_words(words: str) -> list[Word]:
    """Read words from a string containing CSV data."""
    word_lines = words.splitlines()
    word_list = [word.split(";") for word in word_lines]
    word_list = [Word(word[0], word[1], word[2], word[3]) for word in word_list]

    seen_words = {w.word: 0 for w in word_list}
    for word in word_list:
        seen_words[word.word] += 1

    errors = 0
    for s in seen_words:
        if seen_words[s] != 1:
            print(f"Error: Duplicate word {s} found")
            errors += 1
    assert errors == 0, f"{errors} errors found"

    return word_list


def write_words(words: list[Word]) -> str:
    """Write words to a string containing CSV data."""
    output = ""
    for word in words:
        output += f"{word.word};{word.translation};{word.example};{word.example_translation}\n"
    return output
