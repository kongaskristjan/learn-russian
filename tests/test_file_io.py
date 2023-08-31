from src.lib.file_io import HistoryEntry, Word, read_progress, read_words, write_progress


def test_read_words():
    inp = """и;and, though;conjunction;example1
в;in, at;preposition;example2
"""
    expected = [
        Word("и", "and, though", "conjunction", "example1"),
        Word("в", "in, at", "preposition", "example2"),
    ]
    print(read_words(inp), expected)
    assert read_words(inp) == expected


def test_read_progress():
    inp = "и;True\nв;False;"
    expected = [
        HistoryEntry("и", True),
        HistoryEntry("в", False),
    ]
    assert read_progress(inp) == expected


def test_write_progress():
    inp = [
        HistoryEntry("и", True),
        HistoryEntry("в", False),
    ]
    expected = "и;True\nв;False"
    assert write_progress(inp) == expected
