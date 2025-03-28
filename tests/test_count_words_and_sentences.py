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


