import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("TCP Server está ouvindo na porta 12345...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Conexão recebida de {addr}")
            data = client_socket.recv(1024)
            print("Mensagem recebida:", data.decode())
            client_socket.close()
    except KeyboardInterrupt:
        print("Encerrando o servidor TCP.")
    finally:
        server_socket.close()

tcp_server()
