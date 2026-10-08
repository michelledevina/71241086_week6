import streamlit as st
from user import user_data_by_username


# cek apakah sudah login
if "logged_in" not in st.session_state or not st.session_state.logged_in == True:
    st.switch_page("app.py")


st.set_page_config(page_title="DwTix - Profile")


# ambil data user
user = user_data_by_username()


# ambil username yang sedang login
username = st.session_state.username


# ambil data user yang sedang login
current_user = user[username]


st.title("Profile")


# 2 input text
# Username disabled
st.text_input(
    "Username",
    value=username,
    disabled=True
)


# Password
new_password = st.text_input(
    "Password Baru",
    type="password"
)


# kolom tombol
col1, space, col2 = st.columns([1, 3, 1])


with col1:

    # tombol logout
    if st.button("Logout", type="primary"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.switch_page("app.py")


with col2:

    # tombol ganti password
    if st.button(
        "Ganti Data",
        type="secondary",
        width=400
    ):

        # password baru tidak boleh sama dengan password lama
        if new_password == current_user["password"]:

            st.error("ga boleh sama wok")

        elif new_password == "":

            st.error("Password baru tidak boleh kosong")

        else:

            # ubah password
            current_user["password"] = new_password

            st.success("Berhasil")