import streamlit as st
from user import user_data_by_username


# set tab title
st.set_page_config(page_title="DwTix - Login")


# deklarasi sesi username, password, dan status login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# page header
st.header(
    "Selamat datang kembali",
    text_alignment="center",
    divider="green"
)

st.write("*Silahkan masuk menggunakan akun DwTix anda*")


# data di sini dalam bentuk dictionary
user_by_name = user_data_by_username()

# ga boleh hapus untuk asdos nanti cek perubahan password
st.write(user_by_name)


# form username dan password
username = st.text_input(
    "Username",
    placeholder="Masukkan username"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Masukkan password"
)


# tombol login
if st.button("Login", type="primary"):

    if username in user_by_name:
        if user_by_name[username]["password"] == password:

            # simpan status login
            st.session_state.logged_in = True
            st.session_state.username = username

            # ambil role
            role = user_by_name[username]["role"]

            # jika peserta langsung ke event
            if role == "Peserta":
                st.switch_page("pages/event.py")

            # jika admin ke dashboard
            elif role == "Admin":
                st.switch_page("pages/dashboard.py")

        else:
            st.error("Login gagal! Silahkan coba kembali")

    else:
        st.error("Login gagal! Silahkan coba kembali")