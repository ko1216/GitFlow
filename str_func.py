#Обновление
def title_letters(text: str) -> str:
    """
Функция превращает все строчные буквы входящей строки в Заглавные
:param text: str
:return: str
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

#Другой код
def lower_words(text: str) -> str:
    """
Возвращает строку, где все буквы в словах переводятся в нижний регистр
:param text: str
:return: str
    """
    words = text.split()
    lower_words_list = []
    for word in words:
        lower_words_list.append(word.lower())

    return ' '.join(lower_words_list)
