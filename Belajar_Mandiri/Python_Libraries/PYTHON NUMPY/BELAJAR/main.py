import numpy as np

data_penting = np.array([100, 200, 300, 400, 500])

np.save('data_simpanan.npy', data_penting)
print("\narray telah disimpan ke file 'data_simpanan.npy'")

data_muat = np.load('data_simpanan.npy')
print(f"\ndata yang dimuat kembali :\n{data_muat}")