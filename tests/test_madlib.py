from madlib_cli import __version__
from madlib_cli.madlib import parse_blanks
from madlib_cli.madlib import parse_original
from madlib_cli.madlib import display
from madlib_cli.madlib import read_file
from madlib_cli.madlib import write_to_file

def test_version():
    assert __version__ == '0.1.0'

def test_parse_blanks():
    actual = parse_blanks("A {Adjective} and {Adjective} {Noun}")
    expected = ["{Adjective}", "{Adjective}", "{Noun}"]
    assert actual == expected

def test_parse_original():
    actual = parse_original("A {Adjective} and {Adjective} {Noun}")
    expected = ["A ", " and ", " ", ""]
    assert actual == expected

def get_result_1():
    original_parsed = ["A ", " and ", " ", ""]
    inputs = ["dark", "stormy", "night"]
    actual = "A dark and stormy night"
    expected = display(original_parsed, inputs)
    assert actual == expected

def get_result_2():
    original_parsed = ["A ", " and ", " ", " something"]
    inputs = ["dark", "stormy", "night"]
    actual = "A dark and stormy night something"
    expected = display(original_parsed, inputs)
    assert actual == expected

def get_result_3():
    original_parsed = ["A ", " and ", " "]
    inputs = ["dark", "stormy", "night", "something"]
    actual = "A dark and stormy nightsomething"
    expected = display(original_parsed, inputs)
    assert actual == expected

def test_read_file():
    actual = read_file('assets/template-test.txt')
    expected = "A {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_write_to_file():
    expected = "content"
    write_to_file(expected)
    actual = read_file('assets/output.txt')
    assert actual == expected
    