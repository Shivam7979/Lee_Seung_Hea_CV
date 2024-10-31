import streamlit as st

st.set_page_config(page_title="Lee, Seung Hea CV", page_icon=":wave:", layout="centered")
with open("Lee_Seung_Hea_CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

primary_color = "#333333"  # Dark gray for headings
secondary_color = "#666666"  # Lighter gray for body text

 
st.download_button(
    label="📄 Download CV",
    data=PDFbyte,
    file_name="Lee_Seung_Hea_CV.pdf",
    mime="application/pdf"
)


st.title("Lee, Seung Hea")
st.subheader("Major(s), Republic of Korea Air Force")
st.write("**Phone no.:** +82-10-9258-5409")
st.write("**Email:** [seunghea.lee.rokaf@gmail.com](mailto:seunghea.lee.rokaf@gmail.com)")
st.write("**Address:** 22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea")


st.write("---")

# Research Interests Section
st.header("Research Interests")
st.write("- Ergonomics/Process Design/System Modeling")
st.write("- AI for Aviation")
st.write("- Sensitivity Analysis")
st.write("- Military Operations Research")

# Education Section
st.header("Education")

# University of Sussex
st.subheader("University of Sussex, Brighton, United Kingdom")
st.write("**Master of Science in Sustainable Development**")
st.write("03/2022 - 03/2024")

# Korea Air Force Academy
st.subheader("Korea Air Force Academy*, Cheongju, Korea")
st.write("- An educational institution for cadets, equivalent to the United States Air Force Academy (USAFA)")
st.write("**Bachelor of Science in Military / Military Arts**")
st.write("02/2011 - 02/2015")

# Scholarship Section
st.header("Scholarship")
st.write("- FULL SCHOLARSHIP for Ph.D., Republic of Korea Air Force")
st.write("  GRANTED (09/2025)")

# Military Experience Section
st.header("Military Experience")

# Air Force Headquarters
st.subheader("Air Force Headquarters, Gyeryong, Korea")
st.write("12/2022 - Present")
st.write("- Facilitated communication and collaboration between senior Air Force leadership and external agencies to strengthen partnerships and achieve organizational goals.")

# UN Mission in South Sudan
st.subheader("UN Mission in South Sudan (UNMISS), South Sudan")
st.write("10/2020 - 10/2021")
st.write("- Gathering intelligence through patrols and site visits, facilitating communication between conflicting parties, supporting humanitarian efforts.")

# Air Force Special Missions Wing
st.subheader("Air Force Special Missions Wing, Seoul, Korea")
st.write("04/2016 - 09/2020, 01/2022 - 12/2022")
st.write("- Oversaw the daily and weekly scheduling and execution of flight operations for an entire flight wing.")
st.write("- Managed and approved civilian flights in the vicinity of Air Base, conducting risk assessments and ensuring safety compliance.")
st.write("- Led mission planning and execution for tactical flight operations, with a focus on low-level flying, ensuring precise route navigation and mission success.")
st.write("- **Flight Information**")
st.write("Rating: Master Navigator")
st.write("Hours Flown: Over 1,000")
st.write("Aircrafts Flown: C-130H, T-103, KT-1")

# Major Deployments Table
st.subheader("Major Deployments")

# Create a custom CSS style to remove numbering and add a border
st.markdown("""
<style>
.rt-table {
    border-collapse: collapse;
    border: 2px solid black; /* Add a dark border */
}
.rt-tr-group {
    border-bottom: 1px solid black; /* Add a bottom border to group rows */
}
.rt-td, .rt-th {
    border: 1px solid black; /* Add borders to cells */
    padding: 8px;
}
.rt-th {
    background-color: #f2f2f2; /* Add a light gray background to header cells */
}
</style>
""", unsafe_allow_html=True)

st.write("""
| Role | Location | Date |
|------|----------|------|
| Current Flight Operations Officer, U.S.-ROK Command Post Exercise | Okinawa, Japan | 08/2019 |
| Airlift Package Lead, RF-Alaska (International Joint Exercise) | Alaska, US | 05/2019 |
| Cooperation Officer/Flight Crew, Humanitarian Disaster Relief Mission | Palu, Indonesia | 11/2018 |
| Mission Planning Officer/Flight Crew, RF-Alaska (International Joint Exercise) | Alaska, US | 10/2018 |
""")


# Research Experience Section
st.header("Research Experience")
st.subheader("Korea Air Force Academy, Cheongju, Korea")
st.write("09/2014 - 02/2015")
st.write("Undergraduate student (Professors: Dr. Changboo Kang, Dr. Jung-sik Um)")
st.write("Graduation Thesis: “The Role of Propaganda in World War I”")

# Publication Section
st.header("Publication")
st.write("Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming the Satellites of Neighboring Countries Threatening the Korean Peninsula. Military Forum, 118(0), 103-132. 06/2024")


# Research Experience Section
st.header("Research Experience")
st.subheader("Korea Air Force Academy, Cheongju, Korea")
st.write("09/2014 - 02/2015")
st.write("Undergraduate student (Professors: Dr. Changboo Kang, Dr. Jung-sik Um)")
st.write("Graduation Thesis: “The Role of Propaganda in World War I”")

# Publication Section
st.header("Publication")
st.write("Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming the Satellites of Neighboring Countries Threatening the Korean Peninsula. Military Forum, 118(0), 103-132. 06/2024")

# Accomplishments Section
st.header("Accomplishments")

# Qualification Certificates
st.subheader("Qualification Certificates")
st.write("- Squadron Officer Course, Air University (09/2024)")
st.write("- Female Military Officers Course, UN Women (07/2021)")
st.write("- Specialized Training on UN Military Observer, Peacekeeping Operation Center (06/2020)")
st.write("- Electronic Warfare Course, Tactical Flight Wing (06/2018)")
st.write("- Instrument Pilot Instructor Course, Aviation Safety Agency (09/2017)")
st.write("- Joint Force Coordinator Course, Tactical Air Control Group (07/2017)")

# Awards
st.subheader("Awards")
st.write("- Selected for Promotion from Captain to Major in 2024, ROK Air Force (08/2024)")
st.write("- Service Achievement Citation(Airdrop Mission Support), Special Warfare Commander, ROK Army (12/2023)")
st.write("- Service Achievement Citation (Overseas Mission), Joint Chiefs of Staff (10/2021)")
st.write("- Service Achievement Citation(UN Mission), Sector Commander, UN Mission in South Sudan (09/2021)")
st.write("- Service Achievement Award(Outstanding Performance in Flight), Chief of Staff, ROK Air Force (12/2019)")
st.write("- Service Achievement Citation(International Exercise), Chief of Staff, ROK Air Force (02/2019)")
st.write("- Service Achievement Citation(Aerospace Exhibition), Wing Commander Citation , ROK Air Force (12/2017)")

# Languages & Computer Skills
st.header("Languages & Computer Skills")

# Languages
st.subheader("Languages")
st.write("- Korean (Native)")
st.write("- English (Fluent)")
st.write("- Spanish (Basic)")
st.write("- Chinese (Basic)")

# Computer Skills
st.subheader("Computer Skills")
st.write("- Programming Language: Python, R, HTML")
