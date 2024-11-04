import socket

def udp_server():
    server_address = ('localhost', 12345)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)
    
    print("UDP Server está ouvindo na porta 12345...")

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            print(f"Mensagem recebida de {client_address}: {data.decode()}")
            
            server_socket.sendto("Mensagem recebida com sucesso!".encode(), client_address)
    except KeyboardInterrupt:
        print("Encerrando o servidor UDP.")
    finally:
        server_socket.close()

udp_server()
