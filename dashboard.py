import streamlit as st
from user import user_data_by_username

st.set_page_config(page_title="DwTix - Dashboard")

# cek apakah sudah login -> JIKA BELUM ALIHKAN KE app.py
if 'logged_in' not in st.session_state:
    st.switch_page("pages/app.py")

# JANGAN PERNAH RAGU UNTUK CEK DATA PAKAI st.write() ya dari pada ngawang
data = user_data_by_username()
# ambil role yang login dari data
# role = ??

# JIKA YANG LOGIN PESERTA -> ALIHKAN KE PAGE EVENT
if 'logged_in' == peserta: 
    st.session_state['logged_in'] = True
    st.switch_page("pages/event.py")
st.title(f"Welcome, {role} 👋")

# JIKA YANG LOGIN ADMIN TAMPILKAN SELURUH DATA TERSERAH MAU BENTUKNYA APAPUN st.table, st.write boleh aja