import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 1. Buat data dummy
data = {
    'luas_tanah': [100, 150, 200, 250, 300],
    'jumlah_kamar': [2, 3, 4, 4, 5],
    'lokasi': [1, 1, 0, 0, 1],  # 1 = kota, 0 = desa
    'harga': [500, 700, 600, 650, 850]  # dalam juta
}

df = pd.DataFrame(data)

# 2. Pisahkan input (X) dan output (y)
X = df[['luas_tanah', 'jumlah_kamar', 'lokasi']]
y = df['harga']

# 3. Buat dan latih model
model = LinearRegression()
model.fit(X, y)

# 4. Simpan model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model berhasil dilatih dan disimpan sebagai model.pkl")
