from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    error = None
    if request.method == 'POST':
        try:
            # Ambil input dari form
            luas = float(request.form['luas'])
            kamar = int(request.form['kamar'])
            lokasi = request.form['lokasi']

            # Encode lokasi
            lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
            lokasi_encoded = lokasi_mapping.get(lokasi.lower(), 0)

            # Prediksi harga rumah
            features = np.array([[luas, kamar, lokasi_encoded]])
            prediksi = model.predict(features)

            prediction_text = f'Harga Rumah Diprediksi: Rp {prediksi[0]:,.0f}'
        except Exception as e:
            error = f"Terjadi error: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text, error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
