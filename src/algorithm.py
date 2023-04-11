
from src.file_io import Word, HistoryEntry
from typing import Optional

class WordChoiceAlgorithm:
    """
    Algorithm for choosing the next word to ask the user.

    words: list of words to choose from
    progress: list of words that have been asked and whether the user answered correctly
    ask_schedule: list of how many times a word must be answered correctly before it is no longer asked
    false_answer_delay: how many words to ask before asking the same word again after a false answer
    """
    def __init__(self, words: list[Word], progress: list[HistoryEntry], ask_schedule: list[int], false_answer_delay: int):
        self.words = words
        self.ask_schedule = ask_schedule
        self.false_answer_delay = false_answer_delay

        self.word_to_index = {word.word: i for i, word in enumerate(words)}

        self.progress_index = 0
        self.progress = []
        self.times_correct = [0] * len(words)
        self.next_scheduled: list[Optional[int]] = [i for i in range(len(words))]

        for entry in progress:
            self.update_progress(entry.word, entry.correct)

    def get_next_word(self) -> Optional[Word]:
        while self.progress_index < 10000:
            word = self.get_next_word_inner()
            if word is None:
                self.update_progress("--- INCREMENT PROGRESS ---", True)
                continue
            return word
        return None

    def get_next_word_inner(self) -> Optional[Word]:
        for i in range(len(self.words)):
            if self.next_scheduled[i] is None:
                continue
            if self.next_scheduled[i] <= self.progress_index:
                return self.words[i]

        return None

    def update_progress(self, word: str, correct: bool) -> None:
        if word == "--- INCREMENT PROGRESS ---":
            self.progress_index += 1
            return

        index = self.word_to_index[word]
        self.progress.append(HistoryEntry(word, correct))

        if correct:
            self.times_correct[index] += 1

            if self.times_correct[index] == 1:
                self.progress_index += 1

            if self.times_correct[index] >= len(self.ask_schedule):
                self.next_scheduled[index] = None
            else:
                self.next_scheduled[index] = self.progress_index + self.ask_schedule[self.times_correct[index]]

        else:
            self.next_scheduled[index] = self.progress_index + self.false_answer_delay
