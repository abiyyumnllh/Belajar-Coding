import sqlite3

conn = sqlite3.connect('belajar.db')

cursor = conn.cursor()

id_pelanggan_baru = int(input("masukkan ID pelanggan : "))
harga_baru = int(input("masukkan harga layanan baru : "))

cursor.execute("UPDATE pelanggan SET harga = ? WHERE id_pelanggan = ?",(harga_baru, id_pelanggan_baru))
conn.commit()

if cursor.rowcount > 0 :
    print(f"\nberhasil, harga untuk ID {id_pelanggan_baru} telah diperbarui menjadi Rp{harga_baru}")
    
    cursor.execute("SELECT * FROM pelanggan WHERE id_pelanggan = ?", (id_pelanggan_baru,))
    print(f"detail terbaru {cursor.fetchone()}")
else :
    print(f"gagal : pelanggan dengan ID {id_pelanggan_baru} tidak ditemukan")

conn.close()