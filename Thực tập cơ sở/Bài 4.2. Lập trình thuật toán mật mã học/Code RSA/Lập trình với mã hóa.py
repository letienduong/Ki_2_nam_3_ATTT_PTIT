import sympy
import random
import math

#Hàm tìm ước chung lớn nhất của 2 số a và b
def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a # trả về ước chung lớn nhất của a và b
# print(gcd(9999999999999999, 123456789090909090909))

#Hàm tính lũy thừa: a^b mod m
def bipow(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2
    return result
# print(bipow(9999999999999999, 99999999999999999999999999, 4))

def multiplicative_inverse(e, phi): # d la nghịch đảo của e trong phép modulo phi(n)
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
# print(f'Số d: {multiplicative_inverse(3233, 3120)}')
# mod = 3233 * multiplicative_inverse(3233, 3120) % 3120
# print(f'Số dư d, e mod phi: {mod}')

def generate_keypair(p, q): # hàm tạo cặp khóa
    n = p * q
    phi = (p - 1) * (q - 1)

    #Chọn một số nguyên e sao cho 1 < e < phi và gcd(e, phi) = 1
    e = 65537
    # e = random.randint(1, phi)
    # while math.gcd(e, phi) != 1:
    #     e = random.randint(1, phi)

    # Sử dụng thuật toán Euclid mở rộng để tìm d
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n)) # trả về cặp khóa công khai và riêng tư

def encrypt(public_key, plaintext): # hàm mã hóa
    e, n = public_key
    #Hàm ord: Nhận 1 kí tự đầu vào và trả về mã ASCII của kí tự đó
    cipher = [bipow(ord(char), e, n) for char in plaintext] # mã hóa từng kí tự trong plaintext
    return cipher # trả về danh sách các số nguyên đã mã hóa

def decrypt(private_key, ciphertext): # hàm giải mã
    d, n = private_key
    #Hàm chr: Nhận 1 số nguyên đầu vào và trả về kí tự tương ứng với mã ASCII của số đó
    plain = [chr(bipow(char, d, n)) for char in ciphertext] # giải mã từng số nguyên trong ciphertext
    return ''.join(plain) # trả về chuỗi đã giải mã

# Thử nghiệm mã hóa và giải mã
# p = 61
# q = 53
p = sympy.randprime(2**1023, 2**1024) # tạo số nguyên tố ngẫu nhiên p
q = sympy.randprime(2**1023, 2**1024) # tạo số nguyên tố ngẫu nhiên q

public_key, private_key = generate_keypair(p, q) # tạo cặp khóa
print("Khóa công khai:", public_key) # in khóa công khai
print("Khóa bí mật:", private_key) # in khóa bí mật

message = "I am B22DCAT063"
print("Plaintext:", message) # in thông điệp ban đầu

encrypted_msg = encrypt(public_key, message) # mã hóa thông điệp
out_encrypted = ''.join(str(x) for x in encrypted_msg) # chuyển đổi danh sách thành chuỗi
print("Encrypted message:", out_encrypted) # in thông điệp đã mã hóa

decrypted_msg = decrypt(private_key, encrypted_msg) # giải mã thông điệp
print("Decrypted message:", decrypted_msg) # in thông điệp đã giải mã





