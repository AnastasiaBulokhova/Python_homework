# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
'''''''''''''''

c = 'a a a b c a a d c d d'

c = c.split()
print(c)
dct = {}

for i in c:  # пробегаемся прям по буквам
    if i not in dct:
        dct[i] = 1
        print(i, end = ' ')
    else:
        dct[i] = dct[i] + 1
        print(f'{i}_{dct[i] - 1}', end = ' ')

'''''

####################################################################

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = "She sells sea shells on the sea shore The shells \
that she sells are sea shells I'm sure. So if she sells sea \
shells on the sea shore I'm sure that the shells are sea \
shore shells"

words = text.lower().replace('.', ' ').split()
print(words)

st = set(words)
print(st)
count = 0
# print(len(st)) - очень короткое решение

for i in range(len(st)):
    count += 1

print('Уникальные значения:', count) # мое решение, длинное


var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

# Введите ваше решение ниже

st_1 = {var2}
st_2 = {var3}
print(st_1, st_2)
res = st_1.intersection(st_2)
print(res)