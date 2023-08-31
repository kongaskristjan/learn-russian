import random

from src.lib.file_io import HistoryEntry, Word


class WordChoiceAlgorithm:
    """Algorithm for choosing the next word to ask the user.

    words: list of words to choose from
    progress: list of words that have been asked and whether the user answered correctly
    ask_schedule: list of how many times a word must be answered correctly before it is no longer asked
    false_answer_delay: how many words to ask before asking the same word again after a false answer
    """

    def __init__(
        self,
        words: list[Word],
        progress: list[HistoryEntry],
        ask_schedule: list[int],
        false_answer_delay: int,
    ):
        self.words = words
        self.ask_schedule = ask_schedule
        self.false_answer_delay = false_answer_delay

        self.word_to_index = {word.word: i for i, word in enumerate(words)}

        self.schedule = [word.word for word in words]
        assert len(self.schedule) == len(set(self.schedule)), "Duplicate words in words.csv"

        self.progress: list[HistoryEntry] = []
        self.times_correct = [0] * len(words)

        for entry in progress:
            self.update_progress(entry.word, entry.correct)

    def get_next_word(self) -> Word | None:
        if self.schedule == []:
            return None
        word = self.schedule[0]
        return self.words[self.word_to_index[word]]

    def update_progress(self, word: str, correct: bool) -> None:
        self.progress.append(HistoryEntry(word, correct))

        self.schedule.remove(word)
        if correct:
            index = self.word_to_index[word]
            self.times_correct[index] += 1

            if self.times_correct[index] < len(self.ask_schedule):
                self.schedule_next(word, self.ask_schedule[self.times_correct[index]])
        else:
            self.schedule_next(word, self.false_answer_delay)

    def schedule_next(self, word: str, delay: int) -> None:
        delay_range = int(delay * 0.15) + 2
        delay = random.randint(delay - delay_range, delay + delay_range)
        self.schedule.insert(delay, word)
