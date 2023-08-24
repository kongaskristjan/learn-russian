from src.algorithm import WordChoiceAlgorithm
from src.file_io import Word


def test_WordChoiceAlgorithm():
    words = [
        Word("и", "and, though", "conjunction"),
        Word("в", "in, at", "preposition"),
    ]
    ask_schedule = [0, 20]

    algorithm = WordChoiceAlgorithm(words, [], ask_schedule, 0)
    assert algorithm.get_next_word() == words[0]
    algorithm.update_progress(words[0].word, True)
    assert algorithm.get_next_word() == words[1]
    algorithm.update_progress(words[1].word, True)

    assert algorithm.get_next_word() == words[0]
    algorithm.update_progress(words[0].word, True)
    assert algorithm.get_next_word() == words[1]
    algorithm.update_progress(words[1].word, True)

    assert algorithm.get_next_word() is None


def test_WordChoiceAlgorithm_false_entries():
    words = [
        Word("и", "and, though", "conjunction"),
        Word("в", "in, at", "preposition"),
    ]
    ask_schedule = [0, 20]

    algorithm = WordChoiceAlgorithm(words, [], ask_schedule, 20)
    assert algorithm.get_next_word() == words[0]
    algorithm.update_progress(words[0].word, False)
    assert algorithm.get_next_word() == words[1]
    algorithm.update_progress(words[1].word, False)

    assert algorithm.get_next_word() == words[0]
    algorithm.update_progress(words[0].word, True)
    assert algorithm.get_next_word() == words[1]
    algorithm.update_progress(words[1].word, True)

    assert algorithm.get_next_word() == words[0]
    algorithm.update_progress(words[0].word, True)
    assert algorithm.get_next_word() == words[1]
    algorithm.update_progress(words[1].word, True)

    assert algorithm.get_next_word() is None
