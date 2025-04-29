from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    error = None
    if request.method == 'POST':
        try:
            luas = float(request.form['luas'])
            kamar = int(request.form['kamar'])
            lokasi = request.form['lokasi']

            # Encode lokasi
            lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
            lokasi_encoded = lokasi_mapping.get(lokasi.lower(), 0)

            fitur = np.array([[luas, kamar, lokasi_encoded]])
            prediksi = model.predict(fitur)
            harga = max(prediksi[0], 0)  # Hindari nilai minus

            return render_template('index.html', prediction_text=f'Harga Rumah Diprediksi: Rp {harga:,.0f}')
        except Exception as e:
            error = str(e)
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')

# Untuk Railway / deploy
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
