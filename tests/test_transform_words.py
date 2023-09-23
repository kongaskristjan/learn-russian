from scripts.transform_words import read_words_from_lines
from src.lib.file_io import Word, write_words


def test_read_words_from_lines():
    inp = """
и
and, though				conjunction

в
in, at				preposition
"""
    expected = [
        Word("и", "and, though", "", ""),
        Word("в", "in, at", "", ""),
    ]
    assert read_words_from_lines(inp) == expected


def test_write_words_to_csv_str():
    inp = [
        Word("и", "and, though", "Russian example", "English example"),
        Word("в", "in, at", "Russian example", "English example"),
    ]
    expected = "и;and, though;Russian example;English example\nв;in, at;Russian example;English example\n"
    assert write_words(inp) == expected
