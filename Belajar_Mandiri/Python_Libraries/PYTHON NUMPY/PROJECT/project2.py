import numpy as np

pengunjung = np.random.randint(5, 16, size=(4, 7))
print(f"jumlah pengunjung dari 4 karyawan selama 7 hari : \n{pengunjung}")

tarif = 35000
matriks_omzet = pengunjung * tarif
print(f"\ndata omzet karyawan per hari dengan tarif 35000 :\n{matriks_omzet}")

omzet_mingguan = np.sum(matriks_omzet)
print(f"\nomzet seluruh karyawan : {omzet_mingguan}")

omzet_tertinggi = np.max(matriks_omzet)
print(f"\nomzet harian tertinggi : {omzet_tertinggi}")

rekap_omzet = matriks_omzet[matriks_omzet > 350000]
print(f"ada {rekap_omzet.size} shift yang tembus target Rp350.000")
print(f"\nrekap omzet harian yang lebih dari Rp350.000 :\n{rekap_omzet}")


