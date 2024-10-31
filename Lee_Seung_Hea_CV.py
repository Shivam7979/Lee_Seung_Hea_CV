import streamlit as st

# Set up the page with a centered layout
st.set_page_config(page_title="Lee, Seung Hea CV", page_icon=":wave:", layout="centered")


    # PDF Download Button directly below the profile image
    with open("Shivam Soni CV.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    st.download_button(
        label="📄 Download CV",
        data=PDFbyte,
        file_name="Lee_Seung_Hea_CV.pdf",
        mime="application/pdf"
    )

# Contact Information
with col2:
    st.title("Lee, Seung Hea")
    st.subtitle(“Major(s), Republic of Korea Air Force")
    st.write(“**Phone no.:** +82-10-9258-5409 ")
    st.write("**Email:** [seunghea.lee.rokaf@gmail.com)")
    st.write("**Address:** 22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea")

# Divider
st.write("---")
