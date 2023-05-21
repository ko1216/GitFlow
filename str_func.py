def title_letters(text: str):
    """
    Функция превращает все строчные буквы входящей строки в Заглавные
    """
    return text.upper()


def title_words(text: str) -> str:
    """
Возвращает строку, где все слова начинаются с Заглавной буквы
:param text: str
:return: str
    """
    words = text.split()
    title_words_list = []
    for word in words:
        title_words_list.append(word.title())

    return ' '.join(title_words_list)
