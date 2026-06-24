import sqlite3

conn = sqlite3.connect('belajar.db')
cursor = conn.cursor()

id_baru = int(input("Masukkan ID : "))
nama_baru = input("Masukkan Nama: ").title()
layanan_baru = input("Masukkan Layanan : ").title()
harga_baru = int(input("Masukkan Harga : "))

try :
    cursor.execute("INSERT INTO pelanggan VALUES (?, ?, ?, ?)",(id_baru, nama_baru, layanan_baru, harga_baru))
    conn.commit()
    print("data berhasil disimpan!")

    cursor.execute("SELECT * FROM pelanggan WHERE id_pelanggan = ?", (id_baru,))
    data_baru = cursor.fetchone()

    print ("--- DETAIL DATA BARU ---")
    print(f"ID : {data_baru[0]} | Nama : {data_baru[1]} | Layanan : {data_baru[2]} | Harga : {data_baru[3]}")
    
    cursor.execute("SELECT * FROM pelanggan")
    semua_data = cursor.fetchall()
    
    print ("--- \nDETAIL SEMUA DATA ---")
    for data in semua_data:
        print(f"ID : {data[0]} | Nama : {data[1]} |   Layanan : {data[2]} | Harga : {data[3]}")
        
except sqlite3.IntegrityError:
    print("\ndata dengan ID tersebut sudah ada di database!")
    
conn.close()