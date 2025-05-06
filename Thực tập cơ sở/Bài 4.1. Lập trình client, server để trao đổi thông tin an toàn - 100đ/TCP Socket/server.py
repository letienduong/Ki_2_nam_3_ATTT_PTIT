import hashlib
import socket

def server_program():
    host = socket.gethostname()  # Lấy tên máy chủ
    port = 17202
    server_socket = socket.socket()  # Tạo socket
    server_socket.bind((host, port))  # Gán địa chỉ và cổng cho socket
    server_socket.listen(1) 
    conn, address = server_socket.accept()  # Chấp nhận kết nối từ client
    key = "LeTienDuong_B22DCAT063"

    data = conn.recv(1024).decode()  # data không mã hóa từ client
    data_hash = conn.recv(1024).decode()  # client hashed gửi đến server
    print("Nhận từ client: " + str(data))
    print("Nhận mã hóa SHA-512 của thông điệp trên từ Client: " + str(data_hash))

    svhashed = hashlib.sha512(data.encode("utf-16") + key.encode("utf-16")).hexdigest() # server hashed
    data_s = 'Mã hóa thành công! \n\tHello, I am LeTienDuong_B22DCAT063_server'
    print('Server phản hồi tới client: ' + data_s)
    print("Server mã hóa SHA-512 của bản rõ thông điệp thành: " + svhashed)

    if data_hash != svhashed:
        data_s = "The received message has lost its integrity."

    conn.send(data_s.encode())  
    conn.close()  # Đóng kết nối

if __name__ == '__main__':
    print("Server sẵn sàng!")
    server_program()