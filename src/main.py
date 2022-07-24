import streamlit as st
from summary import summary_text
from da_client import text_to_image
import io
from PIL import Image
import glob

st.title("DiscoArt StoryBoard")

story_title = st.text_input("Give a title to this story")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))

    text = stringio.read()

ok = st.button("GO!")

if ok:
    chapters_summarized = summary_text(text)
    print(chapters_summarized)

    for ind,chapter in enumerate(chapters_summarized):
        
        text_to_image(chapter, story_title, ind)

        st.text(f"Chapter {ind}")
       
        data = Image.open(glob.glob(story_title + f'-Chapter-{ind}/*-done-*.png')[0])
    

        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(data, width=300)
        with col2:
            st.write(chapter[0]["summary_text"])
        