import streamlit as st
from fpdf import FPDF
import base64

# Set the page layout
st.set_page_config(page_title="Lee Seung Hea - CV", layout="centered")

# Custom CSS for professional styling and colored headings
st.markdown("""
    <style>
        h1 {
            color: #2c3e50;  /* Navy Blue */
            font-weight: bold;
            text-align: center;
        }
        h2 {
            color: #1abc9c;  /* Teal Green */
            font-weight: bold;
        }
        h3 {
            color: #3498db;  /* Light Blue */
            font-weight: bold;
        }
        .content {
            text-align: left;
            color: #333333;
            font-size: 16px;
        }
        .contact-info {
            text-align: center;
            margin-top: -10px;
            font-size: 16px;
        }
        .right-align {
            position: absolute;
            top: 70px;
            right: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Function to create PDF and return downloadable link
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Lee, Seung Hea", ln=True, align="C")
    pdf.cell(200, 10, txt="Major(s), Republic of Korea Air Force", ln=True, align="C")
    pdf.cell(200, 10, txt="22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea", ln=True, align="C")
    pdf.cell(200, 10, txt="Phone: +82-10-9258-5409 | Email: seunghea.lee.rokaf@gmail.com", ln=True, align="C")
    pdf.ln(10)
    
    # Add sections
    sections = {
        "Research Interests": ["Ergonomics/Process Design/System Modeling", "AI for Aviation", "Sensitivity Analysis", "Military Operations Research"],
        "Education": [
            "University of Sussex, Brighton, United Kingdom",
            "Master of Science in Sustainable Development | 03/2022-03/2024",
            "Korea Air Force Academy, Cheongju, Korea",
            "Bachelor of Science in Military / Military Arts | 02/2011-02/2015"
        ],
        "Scholarship": ["Full Scholarship for Ph.D., Republic of Korea Air Force | Granted (09/2025-)"],
        "Military Experience": [
            "Air Force Headquarters, Gyeryong, Korea",
            "Protocol Officer, Secretary Office to the Chief of Staff (CSAF) | 12/2022-Present",
            "UN Mission in South Sudan (UNMISS), South Sudan",
            "Military Observer, UNMISS | 10/2020-10/2021",
            "Air Force Special Missions Wing, Seoul, Korea",
            "Flight Operations Officer, C-130 Aircraft Flight Crew | 04/2016-09/2020, 01/2022-12/2022"
        ],
        "Major Deployments": [
            ["Current Flight Operations Officer, U.S.-ROK Command Post Exercise", "Okinawa, Japan", "08/2019"],
            ["Airlift Package Lead, RF-Alaska (International Joint Exercise)", "Alaska, US", "05/2019"],
            ["Cooperation Officer/Flight Crew, Humanitarian Disaster Relief Mission", "Palu, Indonesia", "11/2018"],
            ["Mission Planning Officer/Flight Crew, RF-Alaska (International Joint Exercise)", "Alaska, US", "10/2018"]
        ],
        "Research Experience": [
            "Korea Air Force Academy, Cheongju, Korea",
            "Undergraduate Student | 09/2014-02/2015",
            "Graduation Thesis: 'The Role of Propaganda in World War I'"
        ],
        "Publication": ["Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming. *Military Forum*, 118(0), 103-132."],
        "Accomplishments": [
            "Qualification Certificates",
            "- Squadron Officer Course, Air University | 09/2024",
            "- Female Military Officers Course, UN Women | 07/2021",
            "- Specialized Training on UN Military Observer | 06/2020",
            "Awards",
            "- Promotion to Major, ROK Air Force | 08/2024",
            "- Service Achievement Citation (Airdrop Mission Support) | 12/2023"
        ],
        "Languages & Computer Skills": ["Languages: Korean (Native), English (Fluent), Spanish (Basic), Chinese (Basic)", "Programming: Python, R, HTML"]
    }

    for section, content in sections.items():
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt=section, ln=True)
        pdf.set_font("Arial", size=12)
        
        if section == "Major Deployments":
            for row in content:
                pdf.cell(70, 10, row[0], 0, 0)
                pdf.cell(60, 10, row[1], 0, 0)
                pdf.cell(40, 10, row[2], 0, 1)
        else:
            for item in content:
                pdf.cell(200, 10, txt=item, ln=True)
        pdf.ln(5)

    # Save PDF
    pdf_output = f"Lee_Seung_Hea_CV.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Contact Info with download button
st.title("Lee, Seung Hea")
st.write("**Major(s), Republic of Korea Air Force**")
st.markdown("""
<div class="contact-info">
    22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea<br>
    Phone: +82-10-9258-5409   |   Email: seunghea.lee.rokaf@gmail.com
</div>
""", unsafe_allow_html=True)

# Button to download CV as PDF
pdf_file = create_pdf()
with open(pdf_file, "rb") as f:
    pdf_data = f.read()
    b64 = base64.b64encode(pdf_data).decode()
    download_link = f'<a href="data:application/octet-stream;base64,{b64}" download="Lee_Seung_Hea_CV.pdf">Download CV</a>'
    st.markdown(f'<div class="right-align">{download_link}</div>', unsafe_allow_html=True)

# Render sections with colored headers
st.header("Research Interests")
st.write("- Ergonomics/Process Design/System Modeling")
st.write("- AI for Aviation")
st.write("- Sensitivity Analysis")
st.write("- Military Operations Research")

st.header("Education")
st.write("**University of Sussex, Brighton, United Kingdom**")
st.write("Master of Science in Sustainable Development | 03/2022-03/2024")
st.write("**Korea Air Force Academy, Cheongju, Korea**")
st.write("Bachelor of Science in Military / Military Arts | 02/2011-02/2015")

st.header("Scholarship")
st.write("Full Scholarship for Ph.D., Republic of Korea Air Force | Granted (09/2025-)")

st.header("Military Experience")
st.write("**Air Force Headquarters, Gyeryong, Korea**")
st.write("Protocol Officer, Secretary Office to the Chief of Staff (CSAF) | 12/2022-Present")
st.write("**UN Mission in South Sudan (UNMISS), South Sudan**")
st.write("Military Observer, UNMISS | 10/2020-10/2021")
st.write("**Air Force Special Missions Wing, Seoul, Korea**")
st.write("Flight Operations Officer, C-130 Aircraft Flight Crew | 04/2016-09/2020, 01/2022-12/2022")

st.header("Major Deployments")
st.write("""
| Role | Location | Date |
|------|----------|------|
| Current Flight Operations Officer, U.S.-ROK Command Post Exercise | Okinawa, Japan | 08/2019 |
| Airlift Package Lead, RF-Alaska (International Joint Exercise) | Alaska, US | 05/2019 |
| Cooperation Officer/Flight Crew, Humanitarian Disaster Relief Mission | Palu, Indonesia | 11/2018 |
| Mission Planning Officer/Flight Crew, RF-Alaska (International Joint Exercise) | Alaska, US | 10/2018 |
""")

st.header("Research Experience")
st.write("**Korea Air Force Academy, Cheongju, Korea**")
st.write("Undergraduate Student | 09/2014-02/2015")
st.write("Graduation Thesis: 'The Role of Propaganda in World War I'")

st.header("Publication")
st.write("Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming. *Military Forum*, 118(0), 103-132.")

st.header("Accomplishments")
st.write("**Qualification Certificates**")
st.write("- Squadron Officer Course, Air University | 09/2024")
st.write("- Female Military Officers Course, UN Women | 07/2021")
st.write("- Specialized Training on UN Military Observer | 06/2020")
st.write("**Awards**")
st.write("- Promotion to Major, ROK Air Force | 08/2024")
st.write("- Service Achievement Citation (Airdrop Mission Support) | 12/2023")

st.header("Languages & Computer Skills")
st.write("Languages: Korean (Native), English (Fluent), Spanish (Basic), Chinese (Basic)")
st.write("Programming: Python, R, HTML")
