from chat2md.utils.text_tools import detect_language, is_probably_code

def test_detect_language_python():
    assert detect_language("def hello_world():\n    pass") == "python"

def test_detect_language_json():
    assert detect_language('{ "name": "Rick" }') == "json"

def test_detect_language_sql():
    assert detect_language("SELECT * FROM users;") == "sql"

def test_detect_language_html():
    assert detect_language("<html><body></body></html>") == "html"

def test_detect_language_fallback():
    assert detect_language("This is just plain text.") == "text"

def test_is_probably_code_true_cases():
    assert is_probably_code("def foo():\n    return 42")
    assert is_probably_code("import os\nprint(os.getcwd())")
    assert is_probably_code("class MyClass:\n    pass")

def test_is_probably_code_false_cases():
    assert not is_probably_code("This is a sentence.")
    assert not is_probably_code(123)
