import pandas as pd

df_data = pd.read_csv("data_karyawan.csv")

df_data = df_data[df_data["departemen"] == "IT"]

print(df_data)

df_data.to_csv("data_karyawan.csv", index=False)

print("data terbaru sudah disimpan")