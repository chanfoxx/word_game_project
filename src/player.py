class Player:
    """Модель игрока: хранит имя игрока и верные подслова."""

    def __init__(self, name):
        """Инициализирует атрибуты связанные с игроком."""
        self.name = name
        self.used_subwords = []

    def __repr__(self):
        """Возвращает приветствие с именем игрока."""
        return f"Player ({self.name}, {self.used_subwords})"

    def get_name(self):
        """Возвращает имя игрока."""
        return self.name.title()

    def get_used_words(self):
        """Возвращает количество использованных подслов."""
        return len(self.used_subwords)

    def adding_word(self, subword):
        """Добавляет верные подслова в использованные слова."""
        self.used_subwords.append(subword)

    def check_usage_word(self, subword):
        """Проверяет использование данного подслова до этого."""
        return subword in self.used_subwords
