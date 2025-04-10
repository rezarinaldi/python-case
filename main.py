import streamlit as st

st.title("Belajar Python di Devscale ID")
st.write("Ini adalah contoh aplikasi Streamlit sederhana")
st.write("Penambahan")

value_a = st.number_input("Angka Pertama", step=1)
# default-nya float
# step -> positional argument
value_b = st.number_input("Angka Kedua", step=1)

submit_btn = st.button("Tambahkan")

if submit_btn:
  st.write(f"Total penjumlahan dari {value_a} dan {value_b} adalah {value_a + value_b}.")