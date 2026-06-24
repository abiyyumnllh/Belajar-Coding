import pandas as pd

df_awal = pd.read_csv("data_penjualan_cabang.csv")
df_pt1 = df_awal.pivot_table(index="Kota", columns="Produk", values="Penjualan", aggfunc="sum")

df_pt2 = df_awal.pivot_table(index="Kota", columns="Produk", values="Kepuasan_Pelanggan", aggfunc="mean")

print(df_pt1)
print(df_pt2)