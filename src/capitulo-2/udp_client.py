import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Teste de conexão UDP para um servidor TCP ou UDP."
    client_socket.sendto(message.encode(), ('localhost', 12345))
    print("Mensagem enviada via UDP para o servidor TCP na porta 12345.")
    client_socket.close()

udp_client()
