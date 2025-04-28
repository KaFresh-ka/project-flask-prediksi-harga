from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    advice = None
    error = None

    if request.method == 'POST':
        try:
            # Ambil data
            luas_tanah = float(request.form['luas_tanah'])
            jumlah_kamar = int(request.form['jumlah_kamar'])
            lokasi = int(request.form['lokasi'])

            # Validasi
            if luas_tanah <= 0 or jumlah_kamar <= 0:
                error = "Luas tanah dan jumlah kamar harus lebih dari 0."
            else:
                # Prediksi harga
                input_data = np.array([[luas_tanah, jumlah_kamar, lokasi]])
                prediksi_harga = model.predict(input_data)[0]
                prediction = round(prediksi_harga, 2)

                # Berikan saran berdasarkan harga
                if prediction < 600:
                    advice = "Harga properti ini tergolong murah."
                elif 600 <= prediction <= 800:
                    advice = "Harga properti ini standar."
                else:
                    advice = "Harga properti ini cukup mahal."

        except Exception as e:
            error = "Input tidak valid. Harap masukkan angka dengan benar."

    return render_template('index.html', prediction=prediction, advice=advice, error=error)

if __name__ == '__main__':
    app.run(debug=True)
