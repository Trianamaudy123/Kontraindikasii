import streamlit as st
import pandas as pd
import os

# Load dataset
CSV_PATH = os.path.join(os.getcwd(), "kontraindikasi.csv")

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
else:
    df = pd.DataFrame(columns=["obat", "kontraindikasi"])

# Tampilan utama aplikasi
st.set_page_config(page_title="Cek Obat Dulu", layout="wide")

st.title("🔎 Cek Obat Dulu")
st.subheader("Supaya nggak salah konsumsi obat!")

# Input pencarian obat
obat = st.text_input("Masukkan nama obat:", "").strip().lower()

# Pencarian obat di dataset
if st.button("Cari"):
    hasil = df[df["obat"].str.lower() == obat]
    
    if not hasil.empty:
        kontraindikasi = hasil.iloc[0]["kontraindikasi"]
        st.success(f"**Kontraindikasi:** {kontraindikasi}")
    else:
        st.error("❌ Obat tidak ditemukan dalam database.")

# Info tentang kontraindikasi
st.markdown("### ❓ Apa Itu Kontraindikasi?")
st.info(
    "Kontraindikasi adalah kondisi tertentu di mana seseorang tidak boleh menggunakan obat tertentu "
    "karena dapat menimbulkan efek berbahaya. Pastikan selalu konsultasi dengan dokter atau apoteker sebelum mengonsumsi obat."
)

# Artikel edukasi dalam bentuk expandable
st.markdown("### 📚 Artikel Edukasi")
with st.expander("📖 Penggunaan Obat yang Aman"):
    st.write("Penting untuk selalu membaca label obat, mengikuti dosis yang dianjurkan, dan berkonsultasi dengan tenaga medis.")
with st.expander("👨‍⚕️ Tips Berkonsultasi dengan Dokter"):
    st.write("Siapkan pertanyaan, ceritakan riwayat kesehatan dengan jelas, dan catat rekomendasi dokter.")
with st.expander("⚠️ Efek Samping Obat yang Perlu Diwaspadai"):
    st.write("Beberapa efek samping obat bisa ringan, tetapi ada juga yang serius. Jika mengalami reaksi alergi, segera cari pertolongan medis.")

# Komentar pengguna
st.markdown("### 💬 Komentar")
st.text_area("Tulis komentar Anda di sini...")

st.caption("© 2025 Farmasi Unsika")
