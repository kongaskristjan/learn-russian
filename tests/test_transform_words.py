from scripts.transform_words import read_words_from_lines
from src.file_io import Word, write_words


def test_read_words_from_lines():
    inp = """
и
and, though				conjunction

в
in, at				preposition
"""
    expected = [
        Word("и", "and, though", "conjunction"),
        Word("в", "in, at", "preposition"),
    ]
    assert read_words_from_lines(inp) == expected


def test_write_words_to_csv_str():
    inp = [
        Word("и", "and, though", "conjunction"),
        Word("в", "in, at", "preposition"),
    ]
    expected = "и;and, though;conjunction\nв;in, at;preposition\n"
    assert write_words(inp) == expected
