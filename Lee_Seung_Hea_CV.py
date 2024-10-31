import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Shivam - Digital CV", layout="centered", initial_sidebar_state="collapsed")

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
            text-align: left;
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
            border: 1px solid black;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
        }}
    </style>
""", unsafe_allow_html=True)

# Personal Information
st.markdown("<p class='main-heading'>Shivam</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-heading'>MBA Student, University of East London</p>", unsafe_allow_html=True)
st.markdown("<p class='content'>Address: London, UK<br>Phone: +44-1234-567890<br>Email: shivam.email@example.com</p>", unsafe_allow_html=True)

# Divider
st.markdown("<hr>", unsafe_allow_html=True)

# Section 1: Research Interests
st.markdown("<p class='sub-heading'>RESEARCH INTERESTS</p>", unsafe_allow_html=True)
st.markdown("""
<ul class='content'>
    <li>Digital Marketing Strategies</li>
    <li>AI in Hospitality</li>
    <li>Customer Experience Optimization</li>
</ul>
""", unsafe_allow_html=True)

# Section 2: Education
st.markdown("<p class='sub-heading'>EDUCATION</p>", unsafe_allow_html=True)
st.markdown("<p class='content'><b>University of East London</b>, London, UK<br>MBA (2024-2025)</p>", unsafe_allow_html=True)
st.markdown("<p class='content'><b>Kishinchand Chellaram College</b>, Mumbai, India<br>Bachelor of Management Studies in Marketing (2023)</p>", unsafe_allow_html=True)

# Section 3: Work Experience
st.markdown("<p class='sub-heading'>WORK EXPERIENCE</p>", unsafe_allow_html=True)
st.markdown("""
<p class='content'><b>Purplle.com</b>, Mumbai, India<br>
Key Account Executive Intern (Oct 2023 - Apr 2024)<br>
- Managed key accounts, optimized client communication, and resolved issues promptly.</p>

<p class='content'><b>SASSFI</b>, Mumbai, India<br>
Marketing Assistant Intern (Aug 2023 - Sep 2023)<br>
- Assisted in executing marketing campaigns, conducted market research, and supported strategic development.</p>
""", unsafe_allow_html=True)

# Section 4: Major Projects
st.markdown("<p class='sub-heading'>MAJOR PROJECTS</p>", unsafe_allow_html=True)
st.markdown("""
<p class='content'><b>lululemon Omnichannel Marketing Simulation</b><br>
Developed a digital and omnichannel marketing strategy and an integrated plan for MIRROR.</p>

<p class='content'><b>University of East London: Megatrends Impact on Amazon</b><br>
A group seminar activity analyzing the impact of megatrends (2020-2030) on Amazon’s strategy.</p>
""", unsafe_allow_html=True)

# Section 5: Skills
st.markdown("<p class='sub-heading'>SKILLS</p>", unsafe_allow_html=True)
st.markdown("""
<ul class='content'>
    <li><b>Technical Skills:</b> Google Apps, Microsoft 365, SEO Optimization, Canva, Streamlit, Python (in progress)</li>
    <li><b>Soft Skills:</b> Communication, Leadership, Multitasking, Strategic Thinking</li>
</ul>
""", unsafe_allow_html=True)

# Section 6: Major Deployments (Table Example)
st.markdown("<p class='sub-heading'>DEPLOYMENTS</p>", unsafe_allow_html=True)
deployments_data = {
    "Deployments": [
        "Project Lead, Digital Marketing for Client X",
        "Collaborator, AI Integration for Hospitality Software",
        "Analyst, Customer Data Optimization Project"
    ],
    "Date": ["08/2023", "05/2023", "02/2023"]
}

deployments_df = pd.DataFrame(deployments_data)
st.table(deployments_df.style.hide_index())

# Section 7: Accomplishments
st.markdown("<p class='sub-heading'>ACCOMPLISHMENTS</p>", unsafe_allow_html=True)
st.markdown("""
<p class='content'><b>Completed</b> SEO Certification, HubSpot Academy (2023)<br>
<b>Head of Administration</b>, KC College Cultural Committee (2022-2023)</p>
""", unsafe_allow_html=True)

# Section 8: Languages and Computer Skills
st.markdown("<p class='sub-heading'>LANGUAGES & COMPUTER SKILLS</p>", unsafe_allow_html=True)
st.markdown("<p class='content'>English (Fluent), Hindi (Native), Basic Python, Streamlit, Advanced Google Apps</p>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='content' style='text-align:center;'>For further inquiries, contact me at shivam.email@example.com</p>", unsafe_allow_html=True)
