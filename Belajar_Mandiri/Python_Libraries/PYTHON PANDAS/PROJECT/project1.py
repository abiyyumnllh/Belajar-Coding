import pandas as pd

df = pd.read_csv("data_playlist.csv")

df["Durasi_Menit"] = df["Durasi_Detik"] / 60

df_favorit = df[df["Jumlah_Diputar"] > 20]

df_baru = df.groupby("Genre")["Jumlah_Diputar"].sum().reset_index()
print("--- lagu dengan seluruh jumlah diputarnya ---")
print(df_baru)

df_favorit.to_csv("playlist_favorit.csv", index = False)
print("data terbaru berhasil disimpan")