import pandas as pd

df = pd.read_csv("data_karyawan_pusat.csv")

df_baru = df.copy()
df_baru["Bonus"] = df_baru["Bonus"].fillna(0)
df_baru["Departemen"] = df_baru["Departemen"].fillna("Umum")

df_baru["Total_Gaji"] = df_baru["Gaji_Pokok"] + df_baru["Bonus"]

df_baru["Keterangan"] = df_baru["Nama"] + " - " + df_baru["Status"]

df_dept = df_baru.groupby("Departemen")["Total_Gaji"].mean().reset_index()
print("--- rata rata gaji per departemen ---")
print(df_dept)

df_elite = df_baru[(df_baru["Status"] == "Tetap") & (df["Total_gaji"] > 7000000)]

df_elite.to_csv("karyawan_elite.csv", index=False)
print("data terbaru berhasil disimpan")