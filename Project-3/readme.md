
# Video to Audio Converter 🎥➡️🎶

This project is a **Video to Audio Converter** built with Python, allowing users to convert videos (mp4) into audio (mp3) format. This tool is ideal for creating audio files from videos such as tutorials, lectures, and music, making them accessible for on-the-go listening.

## 📌 Project Overview
- **Project Name:** Video to Audio Converter
- **Language:** Python
- **Libraries Used:** MoviePy, Tkinter
- **Functionality:** Select a video file and extract its audio as an mp3.

## 💻 Project Setup

### Prerequisites
To run this project, you need to install the following libraries:
1. **MoviePy** (for video and audio processing)
2. **Tkinter** (for GUI file selection)

Install the libraries using:
```bash
pip install moviepy
pip install tkinter
```

### Running the Project
1. Clone or download the repository.
2. Run the Python file (`video_to_audio_converter.py`) in your Python environment.

## 📖 Learning & Process

### Step-by-Step Process:
1. **File Selection:** Tkinter’s `askopenfilename()` opens a dialog for users to select a video file from their system.
2. **Video Loading:** The selected video file is loaded using `moviepy.editor.VideoFileClip()`.
3. **Audio Extraction:** Using MoviePy, the audio track is extracted and saved as an mp3 in the same folder as the video file.

### Key Learnings:
- **Working with MoviePy:** Learned how to load video files and perform audio extraction.
- **Building a GUI with Tkinter:** Used Tkinter to simplify the file selection process for users.
- **File Management in Python:** Gained experience saving output files programmatically in specific formats and locations.

## 📂 Project Structure
```
video_to_audio_converter/
│
├── video_to_audio_converter.py  # Main Python script
├── README.md                    # Project documentation
```

## 📷 Screenshots
Screenshots of the conversion process are available in the repository to demonstrate how it works step-by-step.

# 
![Logo](https://i.postimg.cc/tCZpTfcJ/img1.png)

#
![Logo](https://i.postimg.cc/ZRHK8dPq/img2.png)

# 
![Logo](https://i.postimg.cc/Jzj83XMW/img3.png)



---


