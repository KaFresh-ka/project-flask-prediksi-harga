import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('dataset.csv')

# Encode lokasi
lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
data['lokasi_encoded'] = data['lokasi'].map(lambda x: lokasi_mapping.get(x.lower(), 0))

# Ambil fitur dan target
X = data[['luas', 'kamar', 'lokasi_encoded']]
y = data['harga']

# Latih model
model = LinearRegression()
model.fit(X, y)

# Simpan model
pickle.dump(model, open('model.pkl', 'wb'))

print("✅ Model berhasil dilatih dan disimpan!")
