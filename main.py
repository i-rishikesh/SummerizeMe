import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import base64
from io import BytesIO

load_dotenv()  
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """Generate comprehensive notes based on the content of the provided YouTube video URL. Summarize the video into structured notes including headings, subheadings, and key points. Ensure that all important topics and details are covered in the notes. The notes should be well-organized and easy to understand. If the video is in Hindi, please keep the notes in English Language."""

def extract_transcript_details(youtube_video_url, language="en"):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

def get_binary_file_downloader_html(bin_file, file_label='File', file_name='file'):
    """
    Generates a link to download the given binary file.
    
    Parameters:
        bin_file: bytes - The binary file to download.
        file_label: str - Label of the download link (default: 'File').
        file_name: str - Name of the file to download (default: 'file').
    
    Returns:
        str: HTML code for downloading the file.
    """
    bin_file_base64 = base64.b64encode(bin_file.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_file_base64}" download="{file_name}">{file_label}</a>'
    return href

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

language = st.selectbox("Select Video Language:", ["en","hi"])


if youtube_link:
    try:
        video_id = youtube_link.split("=")[1]
        st.video(f"https://www.youtube.com/watch?v={video_id}")

    except IndexError:
        st.warning("Invalid YouTube URL. Please enter a valid URL.")

if st.button("Get Detailed Notes"): 
    try:
        transcript_text = extract_transcript_details(youtube_link, language)
    except Exception as e:
        st.error(f"Error extracting transcript: {str(e)}")
        st.stop()

    if transcript_text:
        st.markdown("## Original Transcript:")
        st.write(transcript_text)

        summary = generate_gemini_content(transcript_text, prompt)
        
        summaries = summary.split("\n")
        
        st.markdown("## Detailed Notes:")
        for s in summaries:
            st.write(s)

        st.markdown("## Export the notes:")
        download_text = "\n".join(summaries)
        st.markdown(get_binary_file_downloader_html(download_text, file_label="Download Text", file_name="summary.txt"), unsafe_allow_html=True)

        # st.markdown(get_binary_file_downloader_html(download_text, file_label="Download PDF", file_name="summary.pdf"), unsafe_allow_html=True)
        # pdf_bytes = text_to_pdf(download_text)
        # download_pdf(pdf_bytes)