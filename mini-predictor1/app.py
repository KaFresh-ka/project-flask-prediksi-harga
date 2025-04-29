from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Halaman utama
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            luas = float(request.form['luas'])
            kamar = int(request.form['kamar'])
            lokasi = request.form['lokasi']
        except KeyError as e:
            return f"Error: Key {str(e)} tidak ditemukan dalam form", 400

        # Proses prediksi
        lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
        lokasi_encoded = lokasi_mapping.get(lokasi.lower(), 0)

        features = np.array([[luas, kamar, lokasi_encoded]])
        prediksi = model.predict(features)

        return render_template('index.html', prediction_text=f'Harga Rumah Diprediksi: Rp {prediksi[0]:,.0f}')
    
    return render_template('index.html')

# Endpoint prediksi
@app.route('/predict', methods=['POST'])
def predict():
    luas = float(request.form['luas'])
    kamar = int(request.form['kamar'])
    lokasi = request.form['lokasi']

    # Contoh encode lokasi ke angka (sederhana)
    lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
    lokasi_encoded = lokasi_mapping.get(lokasi.lower(), 0)

    features = np.array([[luas, kamar, lokasi_encoded]])
    prediksi = model.predict(features)

    return render_template('index.html', prediction_text=f'Harga Rumah Diprediksi: Rp {prediksi[0]:,.0f}')

# Ini WAJIB buat Railway / deploy
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
