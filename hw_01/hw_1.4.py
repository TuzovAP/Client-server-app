"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

a = 'разработка'
b = 'администрирование'
c = 'protocol'
d = 'standard'

str_list = [a, b, c, d]

result_bytes = []
for el in str_list:
    el_b = el.encode('utf-8')
    print(el_b)
    result_bytes.append(el_b)

print('=' * 50)

result_str = []
for el in result_bytes:
    el_str = el.decode('utf-8')
    result_str.append(el_str)

print(result_str)
