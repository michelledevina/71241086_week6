import streamlit as st
from user import user_data_by_username


# cek apakah sudah login
if "logged_in" not in st.session_state or not st.session_state.logged_in == True:
    st.switch_page("app.py")


st.set_page_config(page_title="DwTix - Dashboard")


# data user
data = user_data_by_username()


# ambil username yang sedang login
username = st.session_state.username


# ambil role dari data
role = data[username]["role"]


# jika peserta -> event
if role == "Peserta":
    st.switch_page("pages/event.py")


# halaman dashboard
st.title(f"Welcome, {username} 👋")


# jika bukan admin
if role != "Admin":
    st.error("Anda tidak memiliki akses ke dashboard.")
    st.stop()


# tampilkan seluruh data user
st.subheader("Data Pengguna")

st.table(data)