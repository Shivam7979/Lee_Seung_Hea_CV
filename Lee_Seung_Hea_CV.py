import streamlit as st
import pdfkit

# Title and Header
st.title("Lee, Seung Hea")
st.write("Major(s), Republic of Korea Air Force")
st.write("22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea")
st.write("Phone: +82-10-9258-5409 | Email: seunghea.lee.rokaf@gmail.com")
st.markdown("---")

# Research Interests
st.header("RESEARCH INTERESTS")
st.write("""
- Ergonomics/Process Design/System Modeling  
- AI for Aviation  
- Sensitivity Analysis  
- Military Operations Research  
""")
st.markdown("---")

# Education Section
st.header("EDUCATION")
st.write("**University of Sussex**, Brighton, United Kingdom")
st.write("Master of Science in Sustainable Development")
st.write("03/2022 - 03/2024", align="right")

st.write("**Korea Air Force Academy**, Cheongju, Korea")
st.write("*An educational institution for cadets, equivalent to the United States Air Force Academy (USAFA)*")
st.write("Bachelor of Science in Military / Military Arts")
st.write("02/2011 - 02/2015", align="right")
st.markdown("---")

# Scholarship Section
st.header("SCHOLARSHIP")
st.write("**FULL SCHOLARSHIP for Ph.D., Republic of Korea Air Force**")
st.write("GRANTED(09/2025 - )", align="right")
st.markdown("---")

# Military Experience Section
st.header("MILITARY EXPERIENCE")
st.write("**Air Force Headquarters**, Gyeryong, Korea")
st.write("Protocol Officer, Secretary Office to the Chief of Staff (CSAF)")
st.write("""
- Facilitated communication and collaboration between senior Air Force leadership and external agencies to strengthen partnerships and achieve organizational goals.
""")
st.write("12/2022 - Present", align="right")

st.write("**UN Mission in South Sudan (UNMISS), South Sudan**")
st.write("Military Observer, UNMISS")
st.write("""
- Gathered intelligence through patrols and site visits, facilitating communication between conflicting parties, supporting humanitarian efforts.
""")
st.write("10/2020 - 10/2021", align="right")

st.write("**Air Force Special Missions Wing**, Seoul, Korea")
st.write("Flight Operations Officer, C-130 Aircraft Flight Crew, Special Operations Flight Squadron")
st.write("""
- Oversaw the daily and weekly scheduling and execution of flight operations for an entire flight wing.
- Managed and approved civilian flights in the vicinity of Air Base, conducting risk assessments and ensuring safety compliance.
""")
st.write("04/2016 - 09/2020, 01/2022 - 12/2022", align="right")

# Table for Major Deployments
st.subheader("Major Deployments")
deployments = [
    ["Current Flight Operations Officer, U.S.-ROK Command Post Exercise", "Okinawa, Japan", "08/2019"],
    ["Airlift Package Lead, RF-Alaska (International Joint Exercise)", "Alaska, US", "05/2019"],
    ["Cooperation Officer/Flight Crew, Humanitarian Disaster Relief Mission", "Palu, Indonesia", "11/2018"]
]
st.write("| Role | Location | Date |")
st.write("|------|----------|------|")
for role, location, date in deployments:
    st.write(f"| {role} | {location} | {date} |")

st.markdown("---")

# Research Experience
st.header("RESEARCH EXPERIENCE")
st.write("**Korea Air Force Academy**, Cheongju, Korea")
st.write("Undergraduate student (Professors: Dr. Changboo Kang, Dr. Jung-sik Um)")
st.write("Graduation Thesis: “The Role of Propaganda in World War I”")
st.write("09/2014 - 02/2015", align="right")
st.markdown("---")

# Publications
st.header("PUBLICATION")
st.write("Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming the Satellites of Neighboring Countries Threatening the Korean Peninsula. Military Forum, 118(0), 103-132.")
st.write("06/2024", align="right")
st.markdown("---")

# Accomplishments and Certifications
st.header("ACCOMPLISHMENTS")
st.write("**QUALIFICATION CERTIFICATES**")
certificates = [
    ["Squadron Officer Course, Air University", "09/2024"],
    ["Female Military Officers Course, UN Women", "07/2021"]
]
for cert, date in certificates:
    st.write(f"- {cert} ({date})")
st.markdown("---")

# Languages & Skills
st.header("LANGUAGES & COMPUTER SKILLS")
st.write("**Languages**: Korean (Native), English (Fluent), Spanish (Basic), Chinese (Basic)")
st.write("**Computer Skills**: Programming Language: Python, R, HTML")
st.markdown("---")

# PDF Download
if st.button("Download CV as PDF"):
    # Use pdfkit to generate PDF
    pdf_content = f"""
    Title: Lee, Seung Hea
    Content: {st}
    """
    pdfkit.from_string(pdf_content, "Lee_Seung_Hea_CV.pdf")
    with open("Lee_Seung_Hea_CV.pdf", "rb") as pdf_file:
        st.download_button(
            label="Download PDF",
            data=pdf_file,
            file_name="Lee_Seung_Hea_CV.pdf",
            mime="application/pdf"
        )
