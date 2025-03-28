import re


def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    sentence_endings = {'.', '!', '?'}
    word_delimiters = {' ', ',', ':', ';', '\n'}

    # Розбиваємо на слова
    words = []
    word = ''
    for char in text:
        if char not in word_delimiters:
            word += char
        else:
            if word:
                words.append(word)
                word = ''
    if word:  # Додаємо останнє слово, якщо таке є
        words.append(word)

    words_count = len(words)

    # Рахуємо речення
    sentences_count = sum(1 for i, char in enumerate(text)
                          if char in sentence_endings and text[i:i + 3] != '...')

    # Перевіряємо, чи є останнє речення без кінцевого знака
    if text and text[-1] not in sentence_endings and words_count > 0:
        sentences_count += 1

    return words_count, sentences_count


if __name__ == "__main__":
    file_path = "test_file.txt"
    word_count, sentence_count = count_words_and_sentences(file_path)

    if word_count is not None:
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")
