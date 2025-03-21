from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Path ke file CSV
CSV_PATH = os.path.join(os.getcwd(), "kontraindikasi.csv")

# Load dataset saat aplikasi dijalankan
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    df["obat"] = df["obat"].str.strip().str.lower()  # Normalisasi teks
else:
    df = pd.DataFrame(columns=["obat", "kontraindikasi"])  # Jika file tidak ada, buat DataFrame kosong

@app.route("/", methods=["GET", "POST"])
def home():
    kontraindikasi = None  # Default tidak ada hasil

    if request.method == "POST":
        obat = request.form.get("obat", "").strip().lower()

        # Cari obat dalam dataset
        hasil = df[df["obat"] == obat]

        if not hasil.empty:
            kontraindikasi = hasil.iloc[0]["kontraindikasi"]
        else:
            kontraindikasi = "Obat tidak ditemukan dalam database."

    return render_template("index.html", kontraindikasi=kontraindikasi)

if __name__ == "__main__":
    app.run(debug=True)
