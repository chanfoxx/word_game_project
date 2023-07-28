import requests
from random import choice
from basic_word import BasicWord


def load_file(url):
    """Загружает данные по ссылке и переводит в файл.json"""
    try:
        response = requests.get(url)
        json_file = response.json()
        return json_file
    except FileNotFoundError:
        return None


def load_random_word(url):
    """Возвращает экземпляр класса BasicWord"""
    filename = load_file(url)
    get_word = choice(filename)
    return BasicWord(get_word['word'], get_word['subwords'])
