from player import Player
from utils import load_random_word
from url_file import JSON_URL

# Вызываем функцию, которая возвращает экземпляр класса BasicWord.
word_list = load_random_word(JSON_URL)

# Просим игрока ввести свое имя и создаем экземпляр класса Player.
player_name = input("Please, Enter player's name: ")
player = Player(player_name)

# Приветствуем игрока и выводим правила игры.
print(f"Welcome to the game 'Compose the Words', {player.get_name()}!")
print(f"""- You need to make {len(word_list.subwords)} words 
from the letter of the word '{word_list.word}'.
- The words must be at least 3 letters long.
- To end the game, guess all the words or write 'stop'.
- Let's go! Your first word?""")

# Объявляем переменные для метода класса BasicWord, который вернет кол-во
# слов и для метода класса Player, который вернет кол-во использованных слов.
range_tour = word_list.count_subwords()
used_word = player.get_used_words()

# Создаем цикл, пока кол-во использованных слов будет меньше, чем кол-во
# подслов для слова. Делаем в цикле проверки вводимого игроком слова.
while used_word < range_tour:
    player_word = input("ENTER subword: ")

    if player_word.lower() in ['stop', 'стоп']:
        break

    elif len(player_word) < 3:
        print("It's too short.")

    elif not word_list.check_subword(player_word):
        print("Incorrect word!")

    elif player.check_usage_word(player_word):
        print("This word has already been used.")

    else:
        player.adding_word(player_word)
        print("Alright!")

    # Обновляем переменную с количеством использованных слов.
    used_word = player.get_used_words()

# Выводим результаты игры.
if used_word == range_tour:
    print(f"The game is over! You have guessed all the word. Congratulations!")
else:
    print(f"The game is over! You have guessed {used_word} word.")
