#https://www.youtube.com/watch?v=VqgUkExPvLY&ab_channel=CodingIsFun

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="NIU's Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<styple>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
    
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_neoi7cp3.json")
img_contact_form = Image.open("images/1.png")
img_lottie_animation = Image.open("images/2.png")

# ---- HEADER SECTION----
with st.container():
    st.subheader("Hi, I am NIU (Neil)  :wave:")
    st.title("A Machine Learning practitioner with a Focus on Healthcare")
    st.write("I am passionate about machine learning ,math, and building applicantions")
    st.write("[Learn More>](https://github.com/niuneo)")
    
# ----WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
                """
                A DataScience/ML practitioner, designing reusable data pipelines:
                - Know-how: 6+ yrs Hands-on Python, R, Matlab, SAS, GAMS; Proficient in Data Structures & Algorithms
                - Know-why: Statistical Learning, Math Modeling, Optimisation; Trained in Process_Systems_Engineering
                - Know-what: Domains: 10+ ys BioPharma (R&D+Commercial), Operations Mgmt, Process Control; Dr. Eng.
                Phone: +32 (0) 489409738; Email: niuhongxing@gmail.com)
                """
        )
        st.write("[LinkedIn page >] (https://www.linkedin.com/in/hongxing-neil-niu-b3386837/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Publications1")
        st.write(
                """
                Research articles in peer-reviewed journals
                """
        )
        st.markdown("[Google Scholar...](https://scholar.google.com/citations?user=HbMg5Z0AAAAJ&hl=en)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Publications2")
        st.write(
                """
                Research articles in peer-reviewed journals
                """
        )
        st.markdown("[Google Scholar...](https://scholar.google.com/citations?user=HbMg5Z0AAAAJ&hl=en)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
             
    # Documenation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/niuhongxing@gmail.com" method="POST">
         <input type = "hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        
            