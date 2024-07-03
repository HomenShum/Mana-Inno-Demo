import sys
from pathlib import Path

# Add the parent directory to the PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
import pandas as pd
import base64

def home_page():
    st.title("💡 Welcome to Mana Innovation - AI Tool Demo! 🚀")

    st.divider()

    st.header(f"🙌 Nice to meet you! 😊") 
    st.markdown("""
        **GovAssist Navigation Helper** - Enhance your document and website navigation experience. Our tool is designed to help you effortlessly find your way through complex documents and intricate website processes.

        We understand the importance of efficient navigation in saving time and reducing frustration. That's why we're dedicated to improving your ability to quickly locate the information you need and complete tasks with ease.

        Stay tuned as we continue to refine our navigation tools. Your feedback is invaluable to us as we strive to make your document and website navigation as smooth as possible. Thank you for your support! 😊    
        """)
    
    st.divider()

    #################### Descriptions #####################################
    st.header("📝 What does it do?")

    # description column
    desc_col1, desc_col2, _ = st.columns(3)

    with desc_col1:
        with st.container():
            st.subheader("GovAssist AI Tool")
            st.write("This is a full suite solution for works using PDF, Excel, JPG, and more!")
            st.write("It includes:")
            st.write("Optical Character Recognition (OCR)")
            st.write("Text Summarization")
            st.write("Text Translation")
            st.write("Web Scraping")

    with desc_col2:
        with open("assets/images/mana_innovation_logo.jpg", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        col1_img = "data:image/png;base64," + encoded.decode("utf-8")

        col1_Clicked = card(
            title="Mana Innovation",
            text="Click for Balloons! 🎈",
            image=col1_img,
        )

    if col1_Clicked:
        st.balloons()


        
    st.divider()
    #################### Documentation ####################################
    st.header("📚 Documentation")

    st.markdown("""
    **GovAssist AI Tool Documentation**

    **Objective:** The GovAssist AI Tool is designed to enhance government service websites by providing an AI-driven chatbot for citizen inquiries. It supports PDF upload, chat functionalities, and web scraping data.

    **Key Features:**
    - PDF Upload and Chat: Allows users to upload PDFs and interact with the chatbot to extract and summarize information.
    - Web Scraping: Extracts relevant data from specified web pages to provide up-to-date information.
    - Local Data Processing: Ensures all data is processed and stored locally within the Kingdom of Saudi Arabia, with data deletion after user sessions.
    - Language Support: Fully supports Arabic language for all functionalities.

    **Deliverables:**
    1. A functional demo with PDF upload and chat functionalities.
    2. Web scraping functionality for relevant data.
    3. Framework and documentation for switching from OpenAI to a local open-source LLM for production usage.
    4. Documentation on usage and backend architecture, including a high-level tutorial.

    **Infrastructure:** All infrastructure is built and maintained locally within the Kingdom of Saudi Arabia to comply with data storage and deletion requirements.

    **Examples and Tutorials:**

    ### Example 1: GovAssist AI Tool in Action
    This is a video demonstration of the GovAssist AI Tool in action. The tool allows you to extract text from images, PDFs, and Excel files. It also enables users to interact with the chatbot for summarization and translation.

    [Video Placeholder]

    If you have any questions, feel free to reach out to us at [contact email here].
    """)
    # 3rd column
    third_col1, _, _ = st.columns(3)
    with third_col1:
        st.markdown("### Example 1: GovAssist AI Tool in Action")
        govassist_demo_video_file = open('assets/videos/Demo_Parsely_Mana.mp4', 'rb')
        govassist_demo_video_bytes = govassist_demo_video_file.read()
        st.video(govassist_demo_video_bytes)
        st.info("This is a video demonstration of the GovAssist AI Tool in action. The tool allows you to extract text from images, PDFs, and Excel files. It also enables users to interact with the chatbot for summarization and translation.")
        
        st.write("If you have any questions, feel free to reach out to us at [contact email here]")
