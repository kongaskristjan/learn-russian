from scripts.transform_words import read_words_from_lines, write_words_to_csv_str

def test_read_words_from_lines():
    inp = \
"""
и
and, though				conjunction

в
in, at				preposition
"""
    expected = [
        ("и", "and, though", "conjunction"),
        ("в", "in, at", "preposition"),
    ]
    assert read_words_from_lines(inp) == expected


def test_write_words_to_csv_str():
    inp = [
        ("и", "and, though", "conjunction"),
        ("в", "in, at", "preposition"),
    ]
    expected = "и;and, though;conjunction\nв;in, at;preposition\n"
    assert write_words_to_csv_str(inp) == expected
