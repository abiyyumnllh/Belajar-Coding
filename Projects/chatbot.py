from google import genai

# 1. Masukkan API Key kamu
API_KEY = ""

# 2. Inisialisasi client menggunakan struktur library baru
client = genai.Client(api_key=API_KEY)

# 3. Memulai sesi percakapan (menggunakan model yang lebih baru jika diperlukan, misal gemini-2.5-flash)
chat = client.chats.create(model="gemini-2.5-flash")

print("=== Asisten AI Pribadi Siap ===")
print("Ketik 'keluar' untuk menghentikan program.\n")

# 4. Membangun perulangan agar program terus berjalan
while True:
    pesan_pengguna = input("Anda: ")
    
    if pesan_pengguna.lower() == 'keluar':
        print("Sistem AI dimatikan. Sampai jumpa!")
        break
    
    # 5. Mengirim pesan menggunakan format SDK baru
    try:
        respons = chat.send_message(pesan_pengguna)
        print(f"AI: {respons.text}\n")
    except Exception as e:
        print(f"Terjadi kesalahan koneksi: {e}")