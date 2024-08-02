import streamlit as st
from utils import check_password

def login():
    st.title("Login")

    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submit_button = st.form_submit_button("Login")

        if submit_button:
            if check_password(username, password):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid username or password")
