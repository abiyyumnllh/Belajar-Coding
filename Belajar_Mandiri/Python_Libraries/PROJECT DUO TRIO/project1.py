import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Produk': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Headset', 'Webcam'],
    'Harga': [15000000, 200000, 2500000, 500000, np.nan, 800000], # Ada data kosong (NaN)
    'Terjual': [10, 50, 15, 30, 20, 12]
})

print(f"data awal : \n{df}")
rata_rata_harga = np.nanmean(df['Harga'])
df['Harga'] = df['Harga'].replace(np.nan, rata_rata_harga)

print(f"\n=== setelah pembershihan (harga kosong di isi Rp {rata_rata_harga:.0f}) ===")
print(df)

df['Total Pendapatan'] = df['Harga'] * df['Terjual']
print("\n=== data dengan total pendapatan ===")
print(df)