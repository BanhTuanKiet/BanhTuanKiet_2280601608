from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_key = RSA.generate(2048)

# Receive server public key
server_public_key = RSA.import_key(client_socket.recv(2048))

# Send client public key to the server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# Receive encrypted AES key from the server
encrypted_aes_key = client_socket.recv(2048)

# Decrypt AES key using client's private key
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + cipher_text

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def receive_messages():
    while True:
        encrypted_message = client_socket.recv(1024)
        if encrypted_message:
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Received: {decrypted_message}")
        else:
            break

# Start receiving thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("Enter message (exit to quit): ")
    encrypted_message = encrypt_message(aes_key, message)
    client_socket.send(encrypted_message)

    if message == "exit":
        break

client_socket.close()
