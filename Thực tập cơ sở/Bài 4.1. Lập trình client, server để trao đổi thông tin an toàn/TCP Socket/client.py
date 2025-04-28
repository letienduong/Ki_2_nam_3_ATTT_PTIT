import hashlib
import socket

def client_program():
    host = socket.gethostname()  # Lấy tên máy chủ
    port = 17202  # Địa chỉ cổng của server
    client_socket = socket.socket() 
    client_socket.connect((host, port))  # Kết nối đến server
    key = "LeTienDuongX"
    message = "Hello, I am LeTienDuong_B22DCAT063_client"  # Dữ liệu gửi đến server
    hashed = hashlib.sha512(message.encode("utf-16") + key.encode("utf-16")).hexdigest()  # Mã hóa dữ liệu

    print("Client gửi tới server: " + message)
    client_socket.send(message.encode())  # Gửi dữ liệu đến server

    print("Client gửi mã hóa SHA512 tới Server: " + hashed)
    client_socket.send(hashed.encode())  # Gửi mã hóa đến server

    data = client_socket.recv(1024).decode()  # Nhận dữ liệu từ server
    print("Nhận từ server: " + data)
    client_socket.close()

if __name__ == '__main__':
    client_program()