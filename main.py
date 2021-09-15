 #1) Создать переменную типа String
name = 'Tsvetochek'
print('Tsvetochek', type(name))

# 2) Создать переменную типа Integer

birthday = 5
print(birthday, type(birthday))

# 3) Создать переменную типа Float

day_month = 5.08
print(day_month, type(day_month))

# 4) Создать переменную типа Bytes

my_pat = b'plyusha'
print(my_pat, type(my_pat))

my_pat = b'plyusha'
print(my_pat, type(my_pat))
r = bytes ("bla bla", "utf-8")
print(r, type(r))

ab = b"text"
print(ab, type(ab))

my_pat = b'plyusha'
print(my_pat, type(my_pat))

# 5) Создать переменную типа List

my_list = ['a', 'b', 'c', 'd']
print(my_list, type(my_list))

# 6) Создать переменную типа Tuple

count = 1, 2, 3, 4, 5
for a in range(1,5):
    print(count, type(count))

a = tuple ('Privet, narod!')
print('a', a, type(a))

# 7) Создать переменную типа Set

m = set('camera')
print('m', m, type(m))

# 8. Создать переменную типа Frozen set

n = frozenset("hello")
print('n', n, type(n))

# 9) Создать переменную типа Dict

l = dict(name='Tsveti', age=41)
print('l', l, type(l))

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# Смотри пункты: 1 - 9.

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.

name_1 = 'Tsveti'
name_2 = 'Busya'
name_3 = name_1 + name_2

print(str(name_3), type(name))

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.

param_1 = 7
param_2 = 5
param_3 = (param_1 + param_2)

print(param_3, type(param_3))

#13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.

param_1 = 7
param_2 = 5
param_3 = param_1 / param_2

print('param_3 =', param_3, type(param_3))

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.

param_1 = 7
param_2 = 5
param_3 = param_1 * param_2

print('param_3 =', param_3, type(param_3))

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.

param_1 = 7
param_2 = 5
param_3 = param_1 // param_2

print('param_3 =', param_3, type(param_3))

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.

param_1 = 5
param_1 += 1
print('param_1 =', param_1, type(param_1))

