import numpy as np

array_acak = np.random.randint(1, 101, size=10)

np.save('hasil_akhir.npy', array_acak)
print("array acak sudah berhaisl tersimpan dalam file 'hasil_akhir.npy'")

data_muat = np.load('hasil_akhir.npy')
print(f"data yang dimuat kembali : \n{data_muat}")