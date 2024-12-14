from flask import Flask, request, render_template
import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Ketika ada input POST (prediksi dilakukan)
    if request.method == "POST":
        # Contoh logika prediksi
        prediction = "Rp 1.000.000.000"  # Ganti dengan model prediksi Anda
        return render_template("index.html", prediction_text=f"Harga prediksi: {prediction}")
    
    # Jika halaman hanya di-refresh (GET)
    return render_template("index.html")


# Inisialisasi Flask
app = Flask(__name__)

# Load model dan scaler
model = joblib.load('model/models (2).pkl')  # Sesuaikan dengan path file model
scaler_x = joblib.load('model/scaler_x (2).pkl')  # Scaler untuk fitur input
scaler_y = joblib.load('model/scaler_y (2).pkl')  # Scaler untuk output (jika ada)

# Daftar fitur yang digunakan dalam model
required_features = [
    'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea',
    'TotalBsmtSF', '1stFlrSF',  'FullBath',  'TotRmsAbvGrd',  
    'YearBuilt','YearRemodAdd'
]

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil nilai dari input pengguna dan pastikan tidak ada nilai kosong
        user_features = {feature: request.form[feature] for feature in required_features}

        # Validasi input
        for key, value in user_features.items():
            if not value.strip():
                raise ValueError(f"Nilai kosong untuk fitur: {key}")
        
        # Konversi input ke tipe data float
        user_features = {feature: float(value) for feature, value in user_features.items()}
        
        # Ubah ke DataFrame untuk input model dan pastikan urutan fitur sesuai
        input_data = pd.DataFrame([user_features], columns=required_features)

        # Lakukan scaling pada fitur input
        scaled_features = scaler_x.transform(input_data)

        # Prediksi harga rumah
        prediction_scaled = model.predict(scaled_features)

        # Reverse scaling untuk prediksi
        prediction = scaler_y.inverse_transform(prediction_scaled.reshape(-1, 1))[0, 0]

        # Debugging: Periksa hasil prediksi
        print(f"Prediksi Harga Rumah: $ {prediction:,.2f}")
        
        # Tampilkan hasil prediksi
        return render_template('index.html', prediction_text=f"Prediksi Harga Rumah: $ {prediction:,.2f}")
    except Exception as e:
        # Debugging: Periksa error
        print(f"Error: {str(e)}")
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
