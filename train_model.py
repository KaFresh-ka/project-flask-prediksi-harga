import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Contoh data: Luas Tanah, Jumlah Kamar, Lokasi (encoded)
X = np.array([
    [100, 3, 5],
    [120, 4, 3],
    [80, 2, 4],
    [150, 4, 5],
    [90, 3, 2]
])

y = np.array([500000, 600000, 400000, 750000, 450000])

# Bikin model
model = LinearRegression()
model.fit(X, y)

# Simpan model ke file model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model sudah disimpan ke model.pkl!")
