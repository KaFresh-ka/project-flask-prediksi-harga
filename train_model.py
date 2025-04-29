import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('dataset.csv')

# Encode lokasi menjadi angka
lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
data['lokasi_encoded'] = data['lokasi'].map(lokasi_mapping)

# Fitur dan target
X = data[['luas', 'kamar', 'lokasi_encoded']]  # Pastikan fitur memiliki nama kolom yang benar
y = data['harga']

# Train model
model = LinearRegression()
model.fit(X, y)

# Simpan model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model berhasil disimpan!")
