from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os

# Membuat key dari password
def generate_key(password, salt):
    return PBKDF2(password, salt, dkLen=32)

# Fungsi encrypt
def encrypt_file(file_name, password):
    salt = get_random_bytes(16)
    key = generate_key(password, salt)

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(file_name, 'rb') as f:
        data = f.read()

    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    with open('encrypted.bin', 'wb') as f:
        f.write(salt)
        f.write(iv)
        f.write(encrypted_data)

    print("\nFile berhasil dienkripsi!")
    print("Hasil tersimpan sebagai: encrypted.bin")

# Fungsi decrypt
def decrypt_file(password):
    with open('encrypted.bin', 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    key = generate_key(password, salt)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    decrypted_data = unpad(
        cipher.decrypt(encrypted_data),
        AES.block_size
    )

    with open('decrypted_sample.txt', 'wb') as f:
        f.write(decrypted_data)

    print("\nFile berhasil didekripsi!")
    print("Hasil tersimpan sebagai: decrypted_sample.txt")

# Menu program
while True:
    print("\n===== PROGRAM ENKRIPSI FILE AES =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        password = input("Masukkan password: ")
        encrypt_file("sample.txt", password)

    elif pilihan == "2":
        password = input("Masukkan password: ")
        decrypt_file(password)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")