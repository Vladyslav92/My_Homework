#2. Даны два списка чисел. Показать,
#    - числа содержащиеся одновременно как в первом списке, так и во втором
#    - числа содержащиеся в первом, но отсутствуют во втором
#    - солько уникальных для первого и второго списков
#РЕШЕНИЕ:
list1 = {10, 20, 1, 30, 3, 40, 50, 5}
list2 = {15, 25, 1, 35, 3, 45, 55, 5}
print(list1.union(list2))
print(list1.difference(list2))
print(list1.intersection(list2))

#1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в
#этом тексте ранее.
#Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
#пробелов или символами конца строки.
#РЕШЕНИЕ:
text = {}
for w in input("Введите текст: ").split():
    text[w] = text.get(w, 0) + 1
    print(w, "-", text[w] - 1, "раз", end='\n')

#3. Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите все,
#которые подходять по условию задачи.
#Задачу необходимо решить с использованием словаря.
#РЕШЕНИЕ:
text = "Говорил попугай попугаю: Я тебя, попугай, попугаю. Отвечает ему попугай: Попугай, попугай, попугай!"
conv = text.split()
vocabulary = {}
for i in conv:
    if i not in vocabulary:
        vocabulary[i] = 0
    vocabulary[i] += 1
mmax = max(list(vocabulary.values()))
for j, value in vocabulary.items():
    if value == mmax:
        print(text)
        print("Чаще всего встречается слово -", j)

#5. Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов. Необходимо развеннуть
#ловарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь, у которого в качестве
#ключей будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.
#    ```
#    apple - malum, pomum, popula
#    fruit - baca, bacca, popum
#    punishment - malum, multa
#    ```
#РЕШЕНИЕ:
from pprint import pprint

vocabulary1 = {"apple": ['malum', 'pomum', 'popula'],
              "fruit": ['baca', 'bacca', 'popum'],
              "punishment": ['malum', 'multa']
}
pprint(vocabulary1)
print()
vocabulary2 = {}
for key, item in vocabulary1.items():
    for item2 in item:
        vocabulary2[item2] = key
pprint(vocabulary2)

