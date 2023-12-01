# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda n: n
print(values)
transformated = list(map(transformation, values))
print(transformated)
if values == transformated:
    print('ok')
else:
    print('fail') # сама написала)))




####################################################################################################
# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

def find_farthest_orbit(orbits):
    filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
    squares = list(map(lambda orbit: orbit[0] * orbit[1], filtered_orbits))
    maximum = max(squares)
    result = list(filter(lambda orbit: orbit[0]*orbit[1] == maximum, filtered_orbits))
    return result[0]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit(orbits)

print(*find_farthest_orbit(orbits)) # первый способ

#############

def find_farthest_orbit(orbits):
    filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
    return max(filtered_orbits, key=lambda orbit: orbit[0] * orbit[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit(orbits)

print(*find_farthest_orbit(orbits)) # второй способ, лучший способ

#############

def find_farthest_orbit(orbits):
    return max(filter(lambda orbit: orbit[0] != orbit[1], orbits),
               key=lambda orbit: orbit[0] * orbit[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit(orbits)

print(*find_farthest_orbit(orbits))  # самая короткая запись