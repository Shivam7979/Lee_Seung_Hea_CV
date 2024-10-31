import streamlit as st

# Display CV content (replace with your actual content)
st.title("Lee, Seung Hea")
st.subheader("Major(s), Republic of Korea Air Force")

st.text("Address: 22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea")
st.text("Phone: +82-10-9258-5409          Email: seunghea.lee.rokaf@gmail.com")

# Add a divider
st.markdown("---")

# Add download button
with open('Lee_Seung_Hea_CV.pdf', 'rb') as file:
    pdf_bytes = file.read()

st.download_button(
    label="Download CV",
    data=pdf_bytes,
    file_name="Lee_Seung_Hea_CV.pdf",
    mime='application/octet-stream'
)
