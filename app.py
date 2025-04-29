from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Daftar kota & harga per meter
harga_per_kota = {
    'jakarta': 12000000, 'bandung': 8000000, 'surabaya': 10000000,
    'medan': 7000000, 'semarang': 7500000, 'yogyakarta': 6000000,
    'makassar': 6500000, 'denpasar': 8500000, 'bekasi': 9000000,
    'depok': 8500000, 'tangerang': 9500000, 'bogor': 8000000,
    'malang': 7000000, 'padang': 6500000, 'palembang': 6800000,
    'pekanbaru': 6700000, 'batam': 7200000, 'banjarmasin': 6300000,
    'pontianak': 6200000, 'manado': 6400000, 'cimahi': 7800000,
    'solo': 6000000, 'magelang': 5800000, 'kediri': 5700000,
    'mataram': 5500000, 'kupang': 5000000, 'cirebon': 5900000,
    'pasuruan': 5800000, 'probolinggo': 5700000, 'salatiga': 5600000,
    'tasikmalaya': 5400000, 'serang': 5300000, 'cilegon': 5200000,
    'binjai': 5100000, 'lubuklinggau': 5000000, 'samarinda': 6000000,
    'balikpapan': 6500000, 'tarakan': 6400000, 'palangkaraya': 6000000,
    'tanjungpinang': 6300000, 'bengkulu': 5000000, 'ambon': 5200000,
    'ternate': 5000000, 'manokwari': 5100000, 'sorong': 5200000,
    'palu': 5300000, 'kendari': 5400000, 'gorontalo': 5500000,
    'parepare': 5600000, 'bitung': 5700000, 'baubau': 5800000,
    'langsa': 5900000, 'subulussalam': 6000000, 'sabang': 6100000,
    'banda aceh': 6200000, 'lhokseumawe': 6300000, 'sibolga': 6400000,
    'pematangsiantar': 6500000, 'padangsidempuan': 6600000,
    'gunungsitoli': 6700000, 'tebing tinggi': 6800000, 'prabumulih': 6900000,
    'pangkalpinang': 7000000, 'metro': 7100000, 'bandarlampung': 7200000,
    'bengkulu utara': 7300000, 'jambi': 7400000, 'palembang': 7500000,
    'lubuk pakam': 7600000, 'bangka': 7700000, 'belitung': 7800000,
    'karangasem': 7900000, 'buleleng': 8000000, 'jember': 8100000,
    'sidoarjo': 8200000, 'gresik': 8300000, 'blitar': 8400000,
    'nganjuk': 8500000, 'lamongan': 8600000, 'pamekasan': 8700000,
    'sumenep': 8800000, 'tuban': 8900000, 'banyuwangi': 9000000,
    'bangkalan': 9100000, 'situbondo': 9200000, 'bojonegoro': 9300000,
    'ngawi': 9400000, 'ponorogo': 9500000, 'purwokerto': 9600000,
    'cilacap': 9700000, 'tegal': 9800000, 'pemalang': 9900000
}

# Simpan riwayat
history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            luas = float(request.form['luas'])
            kamar = int(request.form['kamar'])
            lantai = int(request.form['lantai'])
            lokasi = request.form['lokasi'].lower()

            harga_per_meter = harga_per_kota.get(lokasi, 0)
            if harga_per_meter == 0:
                raise ValueError("Lokasi tidak dikenali.")

            harga = (harga_per_meter * luas) + (kamar * 50000000) + ((lantai - 1) * 100000000)
            harga = max(harga, 0)

            prediction = f'Harga Rumah Diprediksi: Rp {harga:,.0f}'

            history.append({
                'luas': luas,
                'kamar': kamar,
                'lantai': lantai,
                'lokasi': lokasi.title(),
                'harga': harga
            })

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction, history=history, error=error, cities=sorted(harga_per_kota.keys()))

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    print("Menjalankan aplikasi di http://localhost:8000 ...")
    app.run(host="0.0.0.0", port=port, debug=True)
