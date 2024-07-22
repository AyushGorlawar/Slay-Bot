# app.py
import streamlit as st
from brainshop_helper import get_brainshop_response, save_response, ping_brainshop_api

# Set up your Brainshop API credentials
API_KEY = "rl9O6TuAhfS194dX"
BOT_ID = "173837"
USER_ID = "default_user"  # You can change this to a dynamic value if needed

st.set_page_config(page_title="Slayy Bot", page_icon="🤖")

st.title("Slayy Bot")
st.write("Ask anything and get a response!")

with st.form(key='my_form', clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    response = get_brainshop_response(API_KEY, BOT_ID, user_input, USER_ID)
    save_response(user_input, response)
    st.text_area("AI:", response, height=100)

ping_status = ping_brainshop_api(API_KEY, BOT_ID)
st.markdown(f"**API Status**: {ping_status}")
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Adding space before footer
st.markdown("**© Made by Ayush Gorlawar**", unsafe_allow_html=True)
