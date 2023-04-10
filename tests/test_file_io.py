
from src.file_io import read_words, read_progress, write_progress, Word

def test_read_words():
    inp = \
"""и;and, though;conjunction
в;in, at;preposition
"""
    expected = [
        Word("и", "and, though", "conjunction"),
        Word("в", "in, at", "preposition"),
    ]
    print(read_words(inp), expected)
    assert read_words(inp) == expected

def test_read_progress():
    inp = \
"""и
в"""
    expected = [
        "и",
        "в",
    ]
    assert read_progress(inp) == expected

def test_write_progress():
    inp = [
        "и",
        "в",
    ]
    expected = "и\nв"
    assert write_progress(inp) == expected
