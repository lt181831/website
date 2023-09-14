from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieur1(ur1):
    r = requests.get(ur1)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS----
lottie_coding = "https://lottie.host/f630e80a-ec02-41d6-8218-5dd3c4433192/MJoGFd6G1v.json"

img_contact_form = Image.open("/Users/lauren/website/songofach.PNG")
img_contact_form2 = Image.open("/Users/lauren/website/all.PNG")
#can do another image the same way ("images/title")
#-----HEADER SECTION -------
with st.container():
    st.subheader("Hi, I am Lauren :wave:")
    st.title("I am Currently Looking for a Summer 2024 Internship Program!")
    st.write(" I am looking to gain hands-on experience working on real projects and tasks, build connections with professionals, aquire useful skills and experience, and foster practical expertise working in a professional environment. ")
    st.write("[My Resume >](https://www.dropbox.com/scl/fi/ovi7skey1f23o9gpofat1/LAUREN-INTERNSHIP-RESUME.pdf?rlkey=ubekrz9c829kgf4az2n855hwy&dl=0)")

# -----WHAT I DO -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Current Activities and Interests")
        st.write("##")
        st.write(
                     """ 
                    - I am currently an Undergraduate Course Assistant, and I am having so much fun with it!! 
                    - I just recently ran a half-marathon and have my sites set on running a marathon next year!
                    - My friends and I have recently exchanged our love of social deduction games for the Unsolved Case Files game series. I would highly reccommend!
                    - Lately, my guilty pleasure has been playing Just Dance any moment I have free time!
                    - I have a love for baking, and most recently, I made seven layer bars, almond butter-date bark, and of course chocolate chip cookies. 
                    
                    """
                     )
                # st.write add another link here if need

    with right_column:
        st_lottie(lottie_coding, height=300, key= "coding")

#--- PROJECTS ----
with st.container ():
    st.write("---")
    st.header("Current Reads")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    # the two makes the second clolumn twice as big as first box

    with image_column:
        #insert image
        #7:10 in video shows to put photos in file that you want on website
        st.image(img_contact_form2, width=200)

    with text_column:
        st.subheader("A Little Life")
        st.write(
            """
             Aspects of this book that have enhanced my professional development:
             - Character Development and Tenacity
             - Interpersonal Dynamics
             - Ethical Considerations
             - Emotional Intelligence
             - Diversity and Inclusion

             In summary, "A Little Life" has enriched my understanding of human nature, resilience, and the complexities of life's journey. It has reinforced my commitment to personal and professional growth, ethical decision-making, and fostering a supportive and inclusive work environment."
             
            """
            )
       #if want another link: st.markdown("[Title](link)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, width=200) #or other image
    with text_column:
        st.subheader("A Song of Achilles")
        st.write(
            """
            I have chosen to revisit this book due to its exquisite beauty, captivating narrative,
            and its ability to evoke both profound sadness and deep fufillment simultaneously.

            Aspects of this book that have enhanced my professional development:
            - Leadership and Loyalty
            - Resilience and Determination
            - Adaptability
            - Effective Communication
            - Ethical Decsion-Making

            Overall, "The Song of Achilles" has provided me with valuable insights into human nature, relationships, and leadership, all of which I believe are essential in the business world. It has reinforced my commitment to personal growth and continuous learning, which I bring to my professional endeavors."
            
            """
            )
       # st.markdown("[video title](link)")


# ---- CONTACT -------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/lt181831@utexas.edu" method="POST">
         <input type="hidden" name="_captcha" value="false">
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

css_code = """
/* Style inputs with type="text", select elements and textareas */
input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}

/* hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
"""

st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

