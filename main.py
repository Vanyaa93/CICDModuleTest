def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().strip()

    sentence_endings = {'.', '!', '?'}
    word_delimiters = {' ', ',', ':', ';', '\n'}

    # Видаляємо зайві пробіли
    cleaned_text = ''
    prev_char = ''
    for char in text:
        if char in word_delimiters and prev_char in word_delimiters:
            continue
        cleaned_text += char
        prev_char = char

    # Розбиваємо на слова
    words = []
    word = ''
    for char in cleaned_text:
        if char not in word_delimiters:
            word += char
        else:
            if word:
                words.append(word)
                word = ''
    if word:
        words.append(word)

    words_count = len(words)

    # Рахуємо речення
    sentences_count = 0
    i = 0
    while i < len(cleaned_text):
        if cleaned_text[i] in sentence_endings:
            if i + 2 < len(cleaned_text) and cleaned_text[i:i + 3] == '...':
                i += 2
                continue
            sentences_count += 1
        i += 1

    # Перевіряємо, чи є останнє речення без кінцевого знака
    if cleaned_text and cleaned_text[-1] not in sentence_endings and words_count > 0:
        sentences_count += 1

    return words_count, sentences_count


if __name__ == "__main__":
    file_path = "test_file.txt"
    word_count, sentence_count = count_words_and_sentences(file_path)

    if word_count is not None:
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")
