class BasicWord:
    """Модель слова и количества подслов в нем."""

    def __init__(self, word, subwords):
        """Инициализирует атрибуты связанные со словом, подсловами."""
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        """
        Возвращает количество подслов,
        которые нужно составить из определенного слова.
        """
        return f"BasicWord ({self.word}, {self.subwords})"

    def check_subword(self, subwords):
        """Проверяет наличие введенного слово в списке допустимых слов."""
        return subwords in self.subwords

    def count_subwords(self):
        """Подсчет количества слов."""
        return len(self.subwords)
