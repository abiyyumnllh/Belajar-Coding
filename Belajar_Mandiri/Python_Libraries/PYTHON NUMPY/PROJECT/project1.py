import numpy as np

suhuAcak = np.random.randint(20, 36, size=30)
print(f"suhu ruangan selama 30 hari :\n{suhuAcak}")

suhuTertinggi = np.max(suhuAcak)
print(f"\nsuhu tertingginya adalah {suhuTertinggi}")
suhuTerendah = np.min(suhuAcak)
print(f"\nsuhu terendahnya adalah {suhuTerendah}")
suhuRataRata = np.mean(suhuAcak)
print(f"\nsuhu rata - ratanya adalah {suhuRataRata:.2f}")

print(f"\nsuhu yang tepat untuk dinyalakan AC : \n{suhuAcak[suhuAcak > 30]}")

np.save('data_suhu.npy', suhuAcak)
print("\ndata suhu berhasil disimpan")
