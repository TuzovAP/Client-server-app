'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date).
В это словаре параметров обязательно должны присутствовать юникод-символы, отсутствующие в кодировке ASCII.
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''
import json
from chardet import detect

def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4, ensure_ascii=False)
    print('Compleat!')

if __name__ == '__main__':
    write_order_to_json('printer', '20', '7000', 'Петров В.В.', '20.12.2021')
    write_order_to_json('fax', '200', '500', 'Smirnov A.A.', '14.12.2021')
    write_order_to_json('phone', '50', '100', 'Иванов В.В.', '18.12.2021')
