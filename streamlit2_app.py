import streamlit as st

# Simple login credentials
USER_CREDENTIALS = {
    "admin": "password123",  # Replace with your desired username and password
    "user1": "securepass"
}

# Login form
def login():
    st.title("Secure Streamlit App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success(f"Welcome, {username}!")
            return True
        else:
            st.error("Invalid username or password.")
            return False

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    if login():
        st.session_state.authenticated = True
else:
    st.title("Protected Content")
    st.write("Here are your secure plots!")

    # Display secure plots
    plot_urls = [
       "https://raw.githubusercontent.com/krishangguptafibonacciresearch/distro_project/main/ZN_1m_Volatility_Distribution_2024-09-30_2024-12-26_High_Low_.png"

    ]
    for url in plot_urls:
        st.image(url, caption=f"Plot: {url.split('/')[-1]}")
