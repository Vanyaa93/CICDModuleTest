import pytest
import tempfile
from main import count_words_and_sentences

@pytest.fixture
def temp_text_file():
    def _create_temp_file(content):
        temp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        temp.write(content)
        temp.close()
        return temp.name
    return _create_temp_file


@pytest.mark.parametrize("text, expected", [
    ("Hello world. How are you?", (5, 2)),
    ("One sentence only", (3, 1)),
    ("Multiple. Sentences! With different? Endings.", (5, 4)),
    ("An ellipsis... is tricky.", (4, 2)),
    ("No punctuation at all", (4, 1)),
    ("", (0, 0)),
    ("SingleWord", (1, 1)),
])
def test_count_words_and_sentences(temp_text_file, text, expected):
    """Перевірка підрахунку слів та речень."""
    file_path = temp_text_file(text)
    result = count_words_and_sentences(file_path)
    assert result == expected
