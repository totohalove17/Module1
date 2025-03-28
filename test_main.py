import pytest
from text_analyzer import count_sentences, count_words

#Фікстура для підготовки тексту
@pytest.fixture
def complex_text():
    return "Hi! How are you? I'm fine..."

#Параметризація для count_sentences
@pytest.mark.parametrize("text, expected", [
    ("Hello world!", 1),
    ("Hello... How are you?", 2),
    ("No sentences", 0),
    pytest.param("Hi! How are you? I'm fine...", 3, id="complex_case"),
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected

#Тест з використанням фікстури complex_text
def test_count_sentences_with_fixture(complex_text):
    assert count_sentences(complex_text) == 3

# Параметризація для count_words
@pytest.mark.parametrize("text, expected", [
    ("Hello, world!", 2),
    ("One:two;three four", 4),
    ("   Multiple   spaces   ", 2),
])
def test_count_words(text, expected):
    assert count_words(text) == expected
