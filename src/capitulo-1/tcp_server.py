import socket

server_host = '172.28.128.77'
server_port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)

print(f"Servidor TCP esperando conexões em {server_host}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexão de {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recebido: {data.decode()}")
        client_socket.send(data)

    client_socket.close()

    print(f"Conexão de {client_address} fechada")