import streamlit as st
import subprocess

# Membaca dan menampilkan file HTML
with open('index.html', 'r') as file:
    html_content = file.read()

st.markdown(html_content, unsafe_allow_html=True)

# Menjalankan script Perl dan menangkap outputnya
result = subprocess.run(['perl', 'diagnosis.pl'], capture_output=True, text=True)

# Menampilkan output dari script Perl di Streamlit
st.text(result.stdout)
# Judul Aplikasi
st.title('Diagnosa Kesehatan Mental')

# Gejala-gejala yang bisa dipilih
gejala = [
    "Perasaan sedih"
    "Kehilangan minat atau kegembiraan"
    "Gangguan tidur",
    "Perubahan berat badan drastis.",
    "Pikiran tentang bunuh diri.",
    "Perubahan signifikan suasana hati.",
    "Perubahan nafsu makan.",
    "Ketidakmampuan untuk berkonsentrasi."
]

# Menampilkan checkbox untuk setiap gejala
selected_gejala = []
for g in gejala:
    if st.checkbox(g):
        selected_gejala.append(g)

# Area untuk kesimpulan dan saran
kesimpulan = st.text_area("Kesimpulan:", height=100)
saran = st.text_area("Saran:", height=100)

# Tombol Diagnosa
if st.button('Diagnosa'):
    if selected_gejala:
        # Contoh logika sederhana untuk menentukan kesimpulan dan saran
        if len(selected_gejala) >= 3:
            kesimpulan = "Anda mungkin mengalami masalah kesehatan mental serius."
            saran = "Segera konsultasikan dengan profesional kesehatan mental."
        else:
            kesimpulan = "Anda mungkin mengalami beberapa masalah kesehatan mental ringan."
            saran = "Pantau kondisi Anda dan pertimbangkan untuk berbicara dengan seseorang yang dapat Anda percaya."
    else:
        kesimpulan = "Tidak ada gejala yang dipilih."
        saran = "Silakan pilih gejala-gejala yang Anda alami untuk mendapatkan diagnosa."

    # Menampilkan kesimpulan dan saran
    st.text_area("Kesimpulan:", value=kesimpulan, height=100)
    st.text_area("Saran:", value=saran, height=100)
