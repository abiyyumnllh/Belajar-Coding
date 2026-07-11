prompt_user = "Halo AI, tolong buatkan saya puisi tentang kucing"

daftar_token = prompt_user.split()

print (f"teks mentan : {prompt_user}")
print(f"hasil tokenisasi : {daftar_token}")

jumlah_token = len(daftar_token)

print(f"jumlah token pada prompt ini adalah {jumlah_token}")