import streamlit as st
from summary import summary_text
from clients import text_to_image
import io
from PIL import Image
import glob


with st.sidebar:
    backend = st.selectbox(
        "Choose a Backend",
        ("DiscoArt", "DALLE-Flow")
    )
    if backend == "DiscoArt":
        server = st.text_input("Insert Server Url",
                "grpc://0.0.0.0:51001",
            )

    elif backend == "DALLE-Flow":
        server = st.text_input("Insert Server Url",
                "grpcs://dalle-flow.dev.jina.ai",
            )
    
    else:
        pass

    style = st.radio(
            "Choose a style",
            ('Sketch', 'Cartoon', 'Realistic')
            )
        

st.title("StoryBoard Creator")

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
        
        st.text(f'Chapter {ind+1}')
        data = []
        if backend == "DiscoArt":
            text_to_image(backend, server, chapter, story_title, ind, style)
            data.append(Image.open(glob.glob(f'../{story_title}'
                                             f'-Chapter-{ind}/*-done-*.png')[0]))
            data.append(Image.open(glob.glob(f'../{story_title}'
                                             f'-Chapter-{ind}/*-done-*.png')[1]))
    
        elif backend == "DALLE-Flow":
            text_to_image(backend, server, chapter, story_title, ind, style)
            data.append(Image.open(glob.glob((f'{story_title}'
                                             f'-Chapter-{ind}.png'))[0]))
        else:
            pass

        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(data[0], width=200)          
        with col2:
            st.write(chapter[0]['summary_text'])
        