import streamlit as st
from login import login
from dashboard import dashboard

def main():
    st.set_page_config(page_title="Login App", layout="centered")
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = True

    if st.session_state.logged_in:
        dashboard()
    else:
        login()

if __name__ == "__main__":
    main()
