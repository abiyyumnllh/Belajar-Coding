import pandas as pd

df_data = pd.read_csv("penjualan_toko.csv")

df_total = df_data.groupby("bulan")["pendapatan"].sum()

df_total.to_csv("penjualan_toko.csv", index=False)

print("data terbaru sudah disimpan")