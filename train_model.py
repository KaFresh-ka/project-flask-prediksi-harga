import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv('data/dataset.csv')

# Encode lokasi
lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
data['lokasi_encoded'] = data['lokasi'].map(lambda x: lokasi_mapping.get(x.lower(), 0))

# Training
X = data[['luas', 'kamar', 'lokasi_encoded']]
y = data['harga']

model = LinearRegression()
model.fit(X, y)

# Simpan model
pickle.dump(model, open('model.pkl', 'wb'))
