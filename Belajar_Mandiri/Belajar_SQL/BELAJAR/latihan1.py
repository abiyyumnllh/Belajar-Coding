import sqlite3

conn = sqlite3.connect('belajar.db')

cursor = conn.cursor()

id_layanan = input("masukkan data layanan yang ingin anda cari : ").title()

cursor.execute("SELECT * FROM pelanggan WHERE layanan = ?", (id_layanan,))

data_layanan = cursor.fetchall()

if data_layanan :
    print("--- DATA LAYANAN YANG TERSEDIA ---")
    for baris in data_layanan:
        print(f"Nama    : {baris[1]}")
        print(f"Layanan : {baris[2]}")
else :
    print("maaf, layanan dengan ID tersebut tidak ditemukan")
    
conn.close()