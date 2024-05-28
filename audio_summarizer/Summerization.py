import streamlit as st
from audio_text import Text 
from llm_prompt import LLM
import os 
from pytube import YouTube
from moviepy.editor import *



st.markdown("<h2 style='text-align: center;'>🤖 AI Video / Audio Summarizer 📋</h2>", unsafe_allow_html=True)

st.caption("👉🏽 Get Summary of Video/ YouTube Video / Audio 👈🏽")


def response(text):
    llm_model = LLM()
    prompt = llm_model.summerization_prompt(text)
    llm = llm_model.get_llm().invoke(prompt)
    return llm



link = st.text_input("🎬 YouTube Video URL : ")

st.markdown(
    "<h4 style='text-align: center;'>OR</h4>",
    unsafe_allow_html=True)

file = st.file_uploader("Upload Video / Audio", type=["mp3", "mp4"])
if file != None:
    file_name = file.name.split(".")[-1]
    if file_name == "mp3":
        audio = file.read()
        result = Text().ConvertIntoText(filename = audio)
        st.info("Please wait few moments ....")
        res = response(result)
        st.subheader("Summary : ")
        st.info(res)
    elif file_name == "mp4":
        video = file.read()
        with open(file.name,"wb") as f:
            f.write(video)
        clip = AudioFileClip(filename = file.name)
        audio_filename = "".join(file.name.split(".")[:-1])
        clip.write_audiofile(audio_filename + ".mp3")
        result = Text().ConvertIntoText(filename = audio_filename + ".mp3")
        st.info("Please wait few moments ....")
        res = response(result)
        st.subheader("Summary : ")
        st.info(res)     

    else:
        st.error("Unsupported file uploded.")

if link != "":
    button = st.button("Process with URL")
    if button:
        try:
            file_name = 'temp1'
            yt = YouTube(link)
            video_stream = yt.streams.get_audio_only()
            video_stream.download(filename=file_name+".mp4")
            clip = AudioFileClip(file_name+'.mp4')
            clip.write_audiofile(file_name+'.mp3')
            result = Text().ConvertIntoText(filename = file_name+".mp3")
            st.info("Please wait few moments ....")
            res = response(result)
            st.subheader("Summary : ")
            st.info(res)
        except Exception as e:
            st.error(f"Error downloading audio: {e}")
        # summary = "This will be the summary"
        # st.info(f"Summary : \n{summary}")
