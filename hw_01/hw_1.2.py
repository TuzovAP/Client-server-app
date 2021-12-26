"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе.
Сделать это необходимо в автоматическом, а не ручном режиме с помощью добавления литеры b к текстовому значению,
(т.е. ни в коем случае не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

a = 'class'
b = 'function'
c = 'method'

str_list = [a, b, c]

for item in str_list:
    eval_el = eval(f"b'{item}'")
    print('=' * 50)
    print(f'type: {type(eval_el)}')
    print(f'content: {eval_el}')
    print(f'length: {len(eval_el)}')
