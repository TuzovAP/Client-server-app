"""
3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»
"""

a = 'attribute'
b = 'класс'
c = 'функция'
d = 'type'

check_list = [a, b, c, d]
result = []
for word in check_list:
    for cher in word:
        if ord(cher) > 127:
            result.append(word)
            break
print(f'Слова, которые не возможно записать в виде байтовой строки: {result}')
