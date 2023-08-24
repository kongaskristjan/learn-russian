class Word:
    def __init__(self, word: str, translation: str, part_of_speech: str):
        self.word = word
        self.translation = translation
        self.part_of_speech = part_of_speech

    def __repr__(self):
        return f"('{self.word}';'{self.translation}';'{self.part_of_speech}')"

    def __eq__(self, other):
        return (
            self.word == other.word
            and self.translation == other.translation
            and self.part_of_speech == other.part_of_speech
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
    progress = progress.splitlines()
    entries = [e.split(";") for e in progress]
    entries = [HistoryEntry(e[0], e[1] == "True") for e in entries]
    return entries


def write_progress(progress: list[HistoryEntry]) -> str:
    """Write progress to a string containing CSV data."""
    return "\n".join([f"{e.word};{e.correct}" for e in progress])


def read_words(words: str) -> list[Word]:
    """Read words from a string containing CSV data."""
    words = words.splitlines()
    words = [word.split(";") for word in words]
    words = [Word(word[0], word[1], word[2]) for word in words]

    seen_words = {w.word: 0 for w in words}
    for word in words:
        seen_words[word.word] += 1

    errors = 0
    for s in seen_words:
        if seen_words[s] != 1:
            print(f"Error: Duplicate word {s} found")
            errors += 1
    assert errors == 0, f"{errors} errors found"

    return words


def write_words(words: list[Word]) -> str:
    """Write words to a string containing CSV data.

    Word, translation, and its part of speech are written.
    """
    output = ""
    for word in words:
        output += f"{word.word};{word.translation};{word.part_of_speech}\n"
    return output
