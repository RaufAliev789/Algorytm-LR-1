import string  # для того, чтобы знаки препинания убрать
import time

start_time = time.time()


def bubble_sort(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]


file_path = input("Введите путь к файлу ORIGINAL.txt: ")

# Считываем текст из файла
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

except FileNotFoundError:
    print("Файл не найден! Проверьте путь и попробуйте снова.")
    exit()

# Удаляем знаки препинания из текста
text = text.translate(str.maketrans('', '', string.punctuation))

# Разбиваем текст на слова (массив слов)
words = text.lower().split()

# функция
bubble_sort(words)

end_time = time.time()
result_time = abs(start_time - end_time)

# Записываем отсортированные слова в новый файл RESULT.txt
with open('RESULT.txt', 'w', encoding='utf-8') as result_file:
    for word in words:
        result_file.write(word + '\n')  # Записываем каждое слово на новой строке

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
letter_count = {letter: 0 for letter in alphabet}
for word in words:
    first_letter = word[0]  # первая буква слова
    if first_letter in letter_count:
        letter_count[first_letter] += 1

words_count = len(words)
# Записываем анализ в файл ANALYSIS.txt
with open('ANALYSIS.txt', 'w', encoding='utf-8') as analis_file:
    analis_file.write("Введенный текст:\n")
    analis_file.write(text)
    analis_file.write("\n")
    analis_file.write("Вариант 1: кириллица, по алфавиту, по возрастанию, учитывать числа, сортировка пузырьком \n")
    analis_file.write("Количество слов:")
    analis_file.write(str(words_count))
    analis_file.write("\n")
    analis_file.write("Время сортировки:")
    analis_file.write(str(result_time))
    analis_file.write("\n")
    analis_file.write("Статистика: \n")
    analis_file.write(str(letter_count))

print("Слова отсортированы и записаны в файл RESULT.txt и записан анализ в ANALYSIS.txt")
