'''
Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777. Функции сервера: принимает сообщение клиента;
формирует ответ клиенту; отправляет ответ клиенту; имеет параметры командной строки: -p <port> — TCP-порт для работы
(по умолчанию использует 7777); -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
'''

from socket import socket, AF_INET, SOCK_STREAM
import time
import json

client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
client.connect(('localhost', 8888))  # Соединиться с сервером


def form_precense_msg():
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    jmsg = json.dumps(message)
    bmsg = jmsg.encode('ascii')

    return bmsg


client.send(form_precense_msg())

tm = client.recv(1024)  # Принять не более 1024 байтов данных
client.close()

print("Текущее время: %s" % tm.decode('ascii'))