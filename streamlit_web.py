import streamlit as st
import requests
from streamlit_lottie import st_lottie

#load lottie url
def load_url(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()
#page config
st.set_page_config(page_title="My website", page_icon=":tada:", layout="wide")
#load assets
lottie_code = load_url("https://assets9.lottiefiles.com/packages/lf20_le8PpGpm9v.json")
#head section
st.subheader("Hello, This is my website")
st.title("A student from CTU")
#content
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("----###----")
        st.write(""""
        About me:
        - Name.
        - Age.
        - School.
        - Major.
        """)
    with right_column:
        st_lottie(lottie_code, height=400, key="laptop")
with st.container():
    st.header("Get in touch with me")
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="text" name="name" required>
        <input type="email" name="email" required>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    contact_lottie = load_url("https://assets7.lottiefiles.com/packages/lf20_eroqjb7w.json")
    with right_column:
        st_lottie(contact_lottie, height=400, key="contact")


        

    
