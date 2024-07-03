import nest_asyncio
nest_asyncio.apply()


import sys
from pathlib import Path

# Add the parent directory to the PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))
import streamlit as st
# from utils_others import UserSession, redirect_pages
from streamlit_extras.buy_me_a_coffee import button as buy_me_a_coffee_button
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
import pandas as pd
import base64
from icecream import ic
from page_0_home import home_page
from page_1_chatallfiles import chatallfiles_page

##### Global Settings #########################################################################################
st.set_page_config(
    page_title="Mana Innovation AI Tool", 
    page_icon="💡", 
    layout="wide",
    initial_sidebar_state="expanded"
)
##### Sidebar Elements #####################################################################################
##### Test: sac.menu ###########################################################################################
import streamlit_antd_components as sac

with st.sidebar:
    menu = sac.menu([
        sac.MenuItem('Home', icon='house-fill'),
        sac.MenuItem('Products', icon='box2-heart-fill', children=[
            sac.MenuItem('Demo', icon='box', children=[
                sac.MenuItem('1. Chat for All Files and URLs', icon='chat'),
            ]),
        ]),
    ], open_all=True)

    # ic(menu)

if menu:
    # sac.alert(f"Redirect to {str(menu)} Page", color="success",banner=True, icon=True, closable=True)
    st.toast(f"Redirect to {str(menu)} Page")

##### Main Elements ###########################################################################################
if menu == "Home":
    buy_me_a_coffee_button('homenshum', bg_color="#6f4e37", font_color="#fcf9f8", coffee_color="#376f4e")
    home_page()

if menu == "1. Chat for All Files and URLs":
    chatallfiles_page()
