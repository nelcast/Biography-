from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
biography_file = current_dir / "assets" / "MY BIOGRAHPY(jhonel b. castaños).pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Biograpy | Jhonel B. Castaños"
PAGE_ICON = ":page_facing_up:"
NAME = "Jhonel B. Castaños"
DESCRIPTION = """
A 1st year Computer Engineering student at Surigao National State University
"""
BIRTH_DATE = "Birth Date :August,10,2006"
BIRTH_PLACE = "Birth Place :Surigao City"
EMAIL = "jcastanos@ssct.edu.ph"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/jhonel.b.castanos",
    "Instagram": "https://www.instagram.com/jhon.3l?igsh=MWl0dTFrbXp4cjBxOA==",
    "GitHub": "https://github.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#---PROFIL PIC and DOCUMENT ---
with open(css_file) as f:
    main_css = f.read()
    st.markdown("<style>{}</style>".format(main_css), unsafe_allow_html=True)
with open(biography_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---Insert Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(BIRTH_DATE)
    st.write(BIRTH_PLACE)
    st.download_button(
        label="📄Download_Biography",
        data=PDFbyte,
        file_name=biography_file.name,
        mime="application/octet-stream",        
    )
    st.write("📨", EMAIL)

#-- Social LInks ----
st.write("---")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- About Me---
st.write("#")
st.subheader("About Me")
st.write("---")
st.write(
    """
    Jhonel B. Castaños is an 18-year-old student with a passion for technology and innovation. Born in August 10, 2006 in Surigao City.
    He is originally from Mapawa, Maragusan, Davao de Oro,but he currently lives in Kaskag, Washington, Surigao del Norte, while studying Computer Engineering at Surigao del Norte State University.  
    Jhonel chose Computer Engineering because of his strong interest in technology and solving problems. 

    He is dedicated to learning how computer systems work and how they can be improved to meet the needs of the modern world. 
    Through his studies, he aims to build the skills and knowledge needed to succeed in the field of technology.  
    Although he lives away from his permanent home, Jhonel stays connected to his roots in Mapawa, Maragusan, Davao de Oro.

    This connection shapes his character, teaching him to balance the challenges of living in a new place while staying true to his values and identity.  
    Jhonel looks forward to a future where he can use his education to make a meaningful impact in computer engineering. 
    He hopes to create innovative solutions that help others while proudly representing his community and inspiring others to follow their dreams.
    """    
)

#---- Educational Attainment-----
st.write("#")
st.subheader("Educational Attainment")
st.write("---")
st.write(
    """
- 🏫 Elementary School :(Mapawa,Maragusan,Davao de Oro  Elementary School) Yr:2013-2018
- 🏫 High School :(Mapawa,Maragusan,Davao de Oro National High School ) Yr:2018-2022
- 📖 Senior High School:(Surigao City National High School) Yr:2022-2024
- 🏛️ College :(Surigao Del Norte State University) Yr:2024--

"""
)

#----Achievement----
st.write("#")
st.subheader(" Achievement")
st.write("---")
st.write(
    """
- 🎖️ Elementary School :(Graduate with Perfect Attendance)
- 🎖️ High School :(Graduate with Perfect Attendance )
- 👩🏻‍🎓 Senior High School :(Graduate with Honors and an AY Foundation Awardee)
"""
)

comment = st.text_input("You`re Comment about me", " ")

