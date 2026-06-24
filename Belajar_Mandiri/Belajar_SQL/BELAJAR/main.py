import sqlite3

conn = sqlite3.connect('belajar.db')

cursor = conn.cursor()

id_yang_dicari = input("masukkan id pelanggan yang ingin dicari : ")

cursor.execute("SELECT * FROM pelanggan WHERE id_pelanggan = ?", (id_yang_dicari,))

data_tunggal = cursor.fetchone()

print("--- HASIL PENCARIAN ---")

if data_tunggal :
    print(f"Nama    : {data_tunggal[1]}")
    print(f"Layanan : {data_tunggal[2]}")
    print(f"Harga   : {data_tunggal[3]}")
else :
    print("maaf, pelanggan dengan ID tersebut tidak ditemukan")
    
conn.close()