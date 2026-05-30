# =========================================================
# PROGRAM LOGIN SEDERHANA DENGAN HASHING PASSWORD
# Menggunakan MD5 dan SHA-256
# Penyimpanan data menggunakan JSON
# =========================================================

import hashlib
import json
import os

# Nama file penyimpanan user
FILE_USER = "users.json"


# =========================================================
# MEMBUAT FILE JSON JIKA BELUM ADA
# =========================================================
def buat_file():
    if not os.path.exists(FILE_USER):
        with open(FILE_USER, "w") as file:
            json.dump({}, file)


# =========================================================
# MEMBACA DATA USER DARI JSON
# =========================================================
def baca_data():
    with open(FILE_USER, "r") as file:
        return json.load(file)


# =========================================================
# MENYIMPAN DATA USER KE JSON
# =========================================================
def simpan_data(data):
    with open(FILE_USER, "w") as file:
        json.dump(data, file, indent=4)


# =========================================================
# HASH PASSWORD MD5
# =========================================================
def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()


# =========================================================
# HASH PASSWORD SHA-256
# =========================================================
def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================================================
# REGISTRASI USER
# =========================================================
def registrasi():
    data = baca_data()

    print("\n===== REGISTRASI AKUN =====")

    username = input("Masukkan Username : ")

    if username in data:
        print("Username sudah terdaftar!")
        return

    password = input("Masukkan Password : ")

    print("\nPilih Algoritma Hash:")
    print("1. MD5")
    print("2. SHA-256")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        hasil_hash = hash_md5(password)
        algoritma = "MD5"

    elif pilihan == "2":
        hasil_hash = hash_sha256(password)
        algoritma = "SHA-256"

    else:
        print("Pilihan tidak valid!")
        return

    # Simpan data user
    data[username] = {
        "hash_password": hasil_hash,
        "algoritma": algoritma
    }

    simpan_data(data)

    # Menampilkan hasil
    print("\n===== DATA REGISTRASI =====")
    print("Username        :", username)
    print("Password Asli   :", password)
    print("Algoritma Hash  :", algoritma)
    print("Hasil Hash      :", hasil_hash)

    print("\nRegistrasi berhasil!\n")


# =========================================================
# LOGIN USER
# =========================================================
def login():
    data = baca_data()

    print("\n===== LOGIN USER =====")

    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")

    # Cek username
    if username not in data:
        print("Username tidak ditemukan!")
        return

    algoritma = data[username]["algoritma"]
    hash_tersimpan = data[username]["hash_password"]

    # Hash password input sesuai algoritma
    if algoritma == "MD5":
        hash_input = hash_md5(password)

    elif algoritma == "SHA-256":
        hash_input = hash_sha256(password)

    else:
        print("Algoritma tidak dikenali!")
        return

    # Tampilkan proses verifikasi
    print("\n===== VERIFIKASI LOGIN =====")
    print("Password Asli      :", password)
    print("Hash Input         :", hash_input)
    print("Hash Tersimpan     :", hash_tersimpan)

    # Verifikasi login
    if hash_input == hash_tersimpan:
        print("\nLogin Berhasil!")
    else:
        print("\nPassword Salah!")


# =========================================================
# MENAMPILKAN DATA USER
# =========================================================
def tampilkan_user():
    data = baca_data()

    print("\n===== DATA USER =====")

    if len(data) == 0:
        print("Belum ada user.")
        return

    for username, info in data.items():
        print(f"\nUsername      : {username}")
        print(f"Algoritma     : {info['algoritma']}")
        print(f"Hash Password : {info['hash_password']}")


# =========================================================
# MENU UTAMA
# =========================================================
def menu():
    buat_file()

    while True:
        print("\n==============================")
        print(" SISTEM LOGIN HASH PASSWORD ")
        print("==============================")
        print("1. Registrasi")
        print("2. Login")
        print("3. Tampilkan Data User")
        print("4. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            registrasi()

        elif pilihan == "2":
            login()

        elif pilihan == "3":
            tampilkan_user()

        elif pilihan == "4":
            print("\nProgram selesai.")
            break

        else:
            print("Pilihan tidak valid!")


# =========================================================
# MENJALANKAN PROGRAM
# =========================================================
menu()