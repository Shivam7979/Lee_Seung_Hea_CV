import streamlit as st

# Set the page layout
st.set_page_config(page_title="Lee Seung Hea - CV", layout="centered")

# Display CV Content
st.title("Lee, Seung Hea")
st.write("**Major(s), Republic of Korea Air Force**")
st.write("22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea")
st.write("Phone: +82-10-9258-5409   |   Email: seunghea.lee.rokaf@gmail.com")
st.write("---")

# Research Interests
st.header("Research Interests")
st.write("- Ergonomics/Process Design/System Modeling")
st.write("- AI for Aviation")
st.write("- Sensitivity Analysis")
st.write("- Military Operations Research")

# Education
st.header("Education")
st.write("**University of Sussex, Brighton, United Kingdom**")
st.write("Master of Science in Sustainable Development | 03/2022-03/2024")
st.write("**Korea Air Force Academy, Cheongju, Korea**")
st.write("Bachelor of Science in Military / Military Arts | 02/2011-02/2015")

# Scholarship
st.header("Scholarship")
st.write("Full Scholarship for Ph.D., Republic of Korea Air Force | Granted (09/2025-)")

# Military Experience
st.header("Military Experience")
st.write("**Air Force Headquarters, Gyeryong, Korea**")
st.write("Protocol Officer, Secretary Office to the Chief of Staff (CSAF) | 12/2022-Present")
st.write("- Facilitated communication between senior Air Force leadership and external agencies.")
st.write("**UN Mission in South Sudan (UNMISS), South Sudan**")
st.write("Military Observer, UNMISS | 10/2020-10/2021")
st.write("- Conducted patrols, supported humanitarian efforts.")
st.write("**Air Force Special Missions Wing, Seoul, Korea**")
st.write("Flight Operations Officer, C-130 Aircraft Flight Crew | 04/2016-09/2020, 01/2022-12/2022")
st.write("- Oversaw scheduling, led mission planning for tactical operations.")

# Major Deployments Table
st.header("Major Deployments")
st.write("""
| Role | Location | Date |
|------|----------|------|
| Current Flight Operations Officer, U.S.-ROK Command Post Exercise | Okinawa, Japan | 08/2019 |
| Airlift Package Lead, RF-Alaska (International Joint Exercise) | Alaska, US | 05/2019 |
| Cooperation Officer/Flight Crew, Humanitarian Disaster Relief Mission | Palu, Indonesia | 11/2018 |
| Mission Planning Officer/Flight Crew, RF-Alaska (International Joint Exercise) | Alaska, US | 10/2018 |
""")

# Research Experience
st.header("Research Experience")
st.write("**Korea Air Force Academy, Cheongju, Korea**")
st.write("Undergraduate Student | 09/2014-02/2015")
st.write("Graduation Thesis: 'The Role of Propaganda in World War I'")

# Publication
st.header("Publication")
st.write("Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming. *Military Forum*, 118(0), 103-132.")

# Accomplishments
st.header("Accomplishments")
st.subheader("Qualification Certificates")
st.write("- Squadron Officer Course, Air University | 09/2024")
st.write("- Female Military Officers Course, UN Women | 07/2021")
st.write("- Specialized Training on UN Military Observer | 06/2020")
st.subheader("Awards")
st.write("- Promotion to Major, ROK Air Force | 08/2024")
st.write("- Service Achievement Citation (Airdrop Mission Support) | 12/2023")

# Languages and Computer Skills
st.header("Languages & Computer Skills")
st.write("Languages: Korean (Native), English (Fluent), Spanish (Basic), Chinese (Basic)")
st.write("Programming: Python, R, HTML")

# Option to download as PDF via browser
st.write("---")
st.write("To save as a PDF, use your browser’s print feature (Ctrl+P or Command+P on Mac) and select 'Save as PDF'.")
