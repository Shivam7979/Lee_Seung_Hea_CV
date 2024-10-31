import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Lee, Seung Hea - Digital CV", layout="centered", initial_sidebar_state="collapsed")

# Define theme colors
background_color = "#f8f9fa"  # Lighter background color
heading_color = "#2a9d8f"
subheading_color = "#264653"
text_color = "#333333"
highlight_color = "#e9c46a"

# Set custom CSS for styling
st.markdown(f"""
    <style>
        body {{
            background-color: {background_color};
        }}
        .main-heading {{
            font-size: 32px;
            font-weight: bold;
            color: {heading_color};
            text-align: center;
        }}
        .sub-heading {{
            font-size: 24px;
            font-weight: bold;
            color: {subheading_color};
            text-align: center;
        }}
        .content {{
            color: {text_color};
            font-size: 18px;
            text-align: left;  /* Changed to left for content */
        }}
        .highlight {{
            color: {highlight_color};
        }}
        hr {{
            border: 0;
            height: 1px;
            background-color: {highlight_color};
            margin: 20px 0;
        }}
        table {{
            border: 1px solid black;  /* Black border for table */
        }}
        th, td {{
            border: 1px solid black;  /* Black border for table cells */
            padding: 8px;
        }}
    </style>
""", unsafe_allow_html=True)

# Name and Contact Information
st.markdown("<p class='main-heading'>Lee, Seung Hea</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-heading'>Major(s), Republic of Korea Air Force</p>", unsafe_allow_html=True)
st.markdown("<p class='content'>Address: 22-80, Jangseungbaegi-ro 174beon-gil, Papyeong-myeon, Paju-si, Gyeonggi-do, Republic of Korea<br>Phone: +82-10-9258-5409<br>Email: seunghea.lee.rokaf@gmail.com</p>", unsafe_allow_html=True)

# Divider
st.markdown("<hr>", unsafe_allow_html=True)

# Section 1: Research Interests
st.markdown("<p class='sub-heading'>RESEARCH INTERESTS</p>", unsafe_allow_html=True)
st.markdown("""
<ul class='content'>
    <li>Ergonomics/Process Design/System Modeling</li>
    <li>AI for Aviation</li>
    <li>Sensitivity Analysis</li>
    <li>Military Operations Research</li>
</ul>
""", unsafe_allow_html=True)

# Section 2: Education
st.markdown("<p class='sub-heading'>EDUCATION</p>", unsafe_allow_html=True)
st.markdown("<p class='content'><b>University of Sussex</b>, Brighton, United Kingdom (03/2022-03/2024)<br>Master of Science in Sustainable Development</p>", unsafe_allow_html=True)
st.markdown("<p class='content'><b>Korea Air Force Academy</b>, Cheongju, Korea (02/2011-02/2015)<br>*An educational institution for cadets, equivalent to the United States Air Force Academy (USAFA)<br>Bachelor of Science in Military / Military Arts</p>", unsafe_allow_html=True)

# Section 3: Scholarship
st.markdown("<p class='sub-heading'>SCHOLARSHIP</p>", unsafe_allow_html=True)
st.markdown("<p class='content'>FULL SCHOLARSHIP for Ph.D., Republic of Korea Air Force<br>GRANTED (09/2025-)</p>", unsafe_allow_html=True)

# Section 4: Military Experience
st.markdown("<p class='sub-heading'>MILITARY EXPERIENCE</p>", unsafe_allow_html=True)
st.markdown("""
<p class='content'><b>Air Force Headquarters</b>, Gyeryong, Korea (12/2022-Present)<br>
Protocol Officer, Secretary Office to the Chief of Staff (CSAF)<br>
- Facilitated communication and collaboration between senior Air Force leadership and external agencies to strengthen partnerships and achieve organizational goals.</p>

<p class='content'><b>UN Mission in South Sudan (UNMISS)</b>, South Sudan (10/2020-10/2021)<br>
Military Observer, UNMISS<br>
- Gathering intelligence through patrols and site visits, facilitating communication between conflicting parties, supporting humanitarian efforts.</p>

<p class='content'><b>Air Force Special Missions Wing</b>, Seoul, Korea (04/2016-09/2020, 01/2022-12/2022)<br>
Flight Operations Officer, C-130 Aircraft Flight Crew, Special Operations Flight Squadron<br>
- Oversaw the daily and weekly scheduling and execution of flight operations for an entire flight wing.<br>
- Managed and approved civilian flights in the vicinity of Air Base, conducting risk assessments and ensuring safety compliance.<br>
- Led mission planning and execution for tactical flight operations, with a focus on low-level flying, ensuring precise route navigation and mission success.<br>
Rating: Master Navigator<br>
Hours Flown: Over 1,000<br>
Aircrafts Flown: C-130H, T-103, KT-1</p>
""", unsafe_allow_html=True)

# Section 5: Major Deployments (Table)
st.markdown("<p class='sub-heading'>Major Deployments</p>", unsafe_allow_html=True)
# Adjusted for no serial number and right-aligned dates
deployments_data = {
    "Deployments": [
        "Current Flight Operations Officer, U.S.-ROK Command Post Exercise",
        "Airlift Package Lead, RF-Alaska (International Joint Exercise)",
        "Cooperation Officer/Flight Crew, Humanitarian Disaster Relief Mission",
        "Mission Planning Officer/Flight Crew, RF-Alaska (International Joint Exercise)"
    ],
    "Location": ["Okinawa, Japan", "Alaska, US", "Palu, Indonesia", "Alaska, US"],
    "Date": ["08/2019", "05/2019", "11/2018", "10/2018"]
}

# Create a DataFrame for the table
deployments_df = pd.DataFrame(deployments_data)

# Create a table with right-aligned dates and no first column
st.table(deployments_df.style.hide_index())  # Hides the index (serial number) column

# Section 6: Research Experience
st.markdown("<p class='sub-heading'>RESEARCH EXPERIENCE</p>", unsafe_allow_html=True)
st.markdown("<p class='content'><b>Korea Air Force Academy</b>, Cheongju, Korea (09/2014-02/2015)<br>Undergraduate student (Professors: Dr. Changboo Kang, Dr. Jung-sik Um)<br>*Graduation Thesis*: 'The Role of Propaganda in World War I'</p>", unsafe_allow_html=True)

# Section 7: Publications
st.markdown("<p class='sub-heading'>PUBLICATIONS</p>", unsafe_allow_html=True)
st.markdown("<p class='content'>Lee, Y.S., Lee, S.H., Lee, D.S. (2024). A Study on the Satellite Radio Analysis System for Jamming the Satellites of Neighboring Countries Threatening the Korean Peninsula. Military Forum, 118(0), 103-132. 06/2024</p>", unsafe_allow_html=True)

# Section 8: Accomplishments
st.markdown("<p class='sub-heading'>ACCOMPLISHMENTS</p>", unsafe_allow_html=True)
st.markdown("<p class='content'><b>Qualification Certificates</b><br>Squadron Officer Course, Air University (09/2024)<br>Female Military Officers Course, UN Women (07/2021)<br>Specialized Training on UN Military Observer, Peacekeeping Operation Center (06/2020)<br>Electronic Warfare Course, Tactical Flight Wing (06/2018)<br>Instrument Pilot Instructor Course, Aviation Safety Agency (09/2017)<br>Joint Force Coordinator Course, Tactical Air Control Group (07/2017)</p>", unsafe_allow_html=True)

# Section 9: Awards
st.markdown("<p class='sub-heading'>AWARDS</p>", unsafe_allow_html=True)
st.markdown("""
<p class='content'>Selected for Promotion from Captain to Major in 2024, ROK Air Force (08/2024)<br>
Service Achievement Citation (Airdrop Mission Support), Special Warfare Commander, ROK Army (12/2023)<br>
Service Achievement Citation (Overseas Mission), Joint Chiefs of Staff (10/2021)<br>
Service Achievement Citation (UN Mission), Sector Commander, UN Mission in South Sudan (09/2021)<br>
Service Achievement Award (Outstanding Performance in Flight), Chief of Staff, ROK Air Force (12/2019)<br>
Service Achievement Citation (International Exercise), Chief of Staff, ROK Air Force (02/2019)<br>
Service Achievement Citation (Aerospace Exhibition), Wing Commander Citation, ROK Air Force (12/2017)</p>
""", unsafe_allow_html=True)

# Section 10: Languages and Computer Skills
st.markdown("<p class='sub-heading'>LANGUAGES & COMPUTER SKILLS</p>", unsafe_allow_html=True)
st.markdown("<p class='content'>Korean (Native), English (Fluent),
