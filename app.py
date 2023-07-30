# Импортируем стандартный модуль random
import random


def morse_encode(words_, morse_dict_):
    """
    Перевод слова в Азбуку Морзе
    """
    encode_letters = [morse_dict_[letter] for letter in words_]
    new_word = "".join(encode_letters)
    return new_word


def get_word():
    """
    Получение случайного слова из списка
    """
    random_word = random.choice(words)
    return random_word


def print_statistics(answers_):
    """
    Подсчёт статистики
    """
    right_answer = answers_.count(True)
    wrong_answer = answers_.count(False)
    statistics = (f"Всего задачек: {len(answers_)}\n"
                  f"Отвечено верно: {right_answer}\n"
                  f"Отвечено неверно: {wrong_answer}")
    return statistics


# Создаём список английский слов для расшифровки
words = ["open", "cat", "drawing", "soccer", "code"]

# Создаём словарь Азбуки Морзе
morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

# Создаём список ответов answers
answers = []

# Создаём приветствие и предлагаем начать
user_greeting = input("Сегодня мы потренируемся расшифровывать морзянку.\n"
                      "Нажмите Enter и начнём. ")
print()

# Создаём и запускаем цикл вопрос-ответ
for i in range(len(words)):
    eng_word = get_word()
    morse_word = morse_encode(eng_word, morse_dict)
    user_input = input(f"Слово {i+1} – {morse_word}\n"
                       f"Ваш ответ: ")
    if user_input.title() == eng_word.title():
        answers += [True]
        print(f"Верно, {eng_word.title()}!")
        print()
    else:
        answers += [False]
        print(f"Неверно, {eng_word.title()}!")
        print()

# Выводим статистику
print(print_statistics(answers))
