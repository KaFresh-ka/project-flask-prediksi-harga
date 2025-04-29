from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Ambil input dari form
            luas = request.form['luas']
            kamar = request.form['kamar']
            lokasi = request.form['lokasi']
            
            # Validasi input
            if not luas.isdigit() or not kamar.isdigit() or float(luas) <= 0 or int(kamar) <= 0:
                raise ValueError("Input invalid. Pastikan 'Luas Tanah' dan 'Jumlah Kamar' adalah angka positif.")
            
            luas = float(luas)
            kamar = int(kamar)

            # Encode lokasi
            lokasi_mapping = {'jakarta': 5, 'bandung': 3, 'surabaya': 4}
            lokasi_encoded = lokasi_mapping.get(lokasi.lower(), 0)

            # Prediksi harga rumah
            features = np.array([[luas, kamar, lokasi_encoded]])
            prediksi = model.predict(features)

            return render_template('index.html', prediction_text=f'Harga Rumah Diprediksi: Rp {prediksi[0]:,.0f}')
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error: {str(e)}")
    
    return render_template('index.html')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Railway otomatis akan mengatur PORT
    app.run(host="0.0.0.0", port=port, debug=True)
