import streamlit as st
import subprocess

# Membaca dan menampilkan file HTML
with open('index.html', 'r') as file:
    html_content = file.read()

st.markdown(html_content, unsafe_allow_html=True)

# Menjalankan script Perl dan menangkap outputnya
result = subprocess.run(['perl', 'diagnosis.pl'], capture_output=True, text=True)
