import rsa
import socket
import time

from response_formation import *

APP_PORT = 9073
MAX_CONN = 5
SIZE_TRANSFER = 200  # в Байтах


def choose_group(local_data):
    group_code = int(local_data[0])
    if group_code == 1:
        return local_data[0] + registration(local_data[1:])
    elif group_code == 2:
        return local_data[0] + authorization(local_data[1:])
    elif group_code == 3:
        return local_data[0] + add_lock(local_data[1:])
    elif group_code == 4:
        return local_data[0] + open_lock(local_data[1:])
    elif group_code == 5:
        return local_data[0] + lock_action(local_data[1:])
    else:
        return "Error in group_code"


def filling(x):
    while len(x) != SIZE_TRANSFER:
        x += "0"
    return x


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', APP_PORT))  # прослушка с любого хоста по порту APP_PORT
    sock.listen(MAX_CONN)  # макс соед - MAX_CONN
    conn, addr = sock.accept()  # conn - новый сокет, addr - адрес клиента  # 4DEBUG
    print("server1 ", conn, " |||| ", addr)  # 4DEBUG
    while True:
        # conn, addr = sock.accept()  # conn - новый сокет, addr - адрес клиента
        # print("server1 ", conn, " |||| ", addr)
        """ registration
        data = conn.recv(SIZE_TRANSFER).decode()  # принимаем порциями по SIZE_TRANSFER байта
        print("l/p: ", data)
        answer = choose_group(data)  # 4DEBUG answer = 21s
        conn.send(filling(answer).encode())
        data = conn.recv(SIZE_TRANSFER).decode()  # принимаем порциями по SIZE_TRANSFER байта
        print("key: ", data)
        conn.send(filling("12s").encode())
        data = ""
        if not data:
            break
        """
        """ authorization
        data = conn.recv(SIZE_TRANSFER).decode()  # принимаем порциями по SIZE_TRANSFER байта
        print("l/p: ", data)
        answer = choose_group(data)  # 4DEBUG answer = 21s
        answer += "l1, l2"
        conn.send(filling(answer).encode())
        data = ""
        if not data:
            break
        """
        """ add_lock """
        data = conn.recv(SIZE_TRANSFER).decode()  # принимаем порциями по SIZE_TRANSFER байта
        print("data: ", data)
        answer = choose_group(data)  # 4DEBUG answer = 41s
        print("answer with challenge", answer)
        conn.send(filling(answer).encode())
        data = conn.recv(SIZE_TRANSFER).decode()  # принимаем порциями по SIZE_TRANSFER байта
        print("sign: ", data)
        conn.send(filling("42s").encode())
        data = ""  # 4DEBUG
        if not data:
            break

    conn.close()


