# SummarizeME

This project aims to convert YouTube video into detailed notes using the Gemini AI model. It provides a streamlined interface for users to input a YouTube video URL, select the video's language, and generate comprehensive notes based on the video content.

## Prerequisites

Ensure you have Python installed on your system. You will also need to install the required libraries listed in `requirements.txt` using the following command:

```bash
pip install -r requirements.txt
```

## Features

- Accepts a YouTube video URL as input.
- Supports English and Hindi languages for video transcripts.
- Displays the video thumbnail for visual reference.
- Extracts the transcript from the provided YouTube video.
- Utilizes the Gemini AI model to generate detailed notes based on the video content.
- Allows users to download the original transcript and the generated notes as a text file.

## How to Use

1. Run the Streamlit app by executing the following command in your terminal:

```bash
streamlit run main.py
```

2. Enter a valid YouTube video URL in the text input field.

3. Select the language of the video (English or Hindi) from the dropdown menu.

4. Click the "Get Detailed Notes" button to initiate the transcript extraction and note generation process.

5. Once completed, the original transcript and detailed notes will be displayed on the app interface.

6. You can download the generated notes as a text file by clicking the "Download Text" button.

## File Structure

- `main.py`: Contains the Streamlit application code.
- `requirements.txt`: Lists the required Python libraries and their versions.

## Usage Notes

- Ensure that you have a stable internet connection to fetch the YouTube video details and transcript.
- This application relies on external APIs such as YouTubeTranscriptApi and the Gemini AI model, so any changes or disruptions in these services may affect functionality.

## Contributing

Contributions to this project are welcome! You can contribute by improving the UI, adding language support, optimizing code, or fixing bugs. Fork the repository, make your changes, and submit a pull request with a detailed description of your modifications.
