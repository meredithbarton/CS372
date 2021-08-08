import socket


def recv(s, host, port):
    # socket must be bound and listening to accept connections
    s.bind((host, port))
    # listen, accept 1 failed connection
    s.listen(1)
    # prints the received value, declaring minimum value
    resp = s.recv(4096)
    while len(resp) > 0:
        print(str(resp, 'utf-8'))
        resp = s.recv(4096)


def send(s, host, port):
    # Define response
    message = input()

    while True:
        # client_conn is new socket object, address is bound to this new object on other end
        client_conn, client_address = s.accept()

        # get request
        request = client_conn.recv(1024).decode()
        print(request)

        # send response
        client_conn.sendall(message.encode())
        client_conn.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 2212
    print("Waiting for message on port %s..." % port)
    # server will use connection-based protocol, and (host, port) address family
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recv(s, host, port)
    send(s, host, port)
