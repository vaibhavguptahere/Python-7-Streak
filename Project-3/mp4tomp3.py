"""Convert Video(mp4) to Audio(mp3)"""


# pip install moviepy
# pip install tkinter
# Library used- Moviepy and tkinter

# moviepy.editor- Module of moviepy library generally used in video editing
import moviepy.editor

# provides a GUI(Graphical User Interface) file dialog to allow the user to select a file from their system
from tkinter.filedialog import *

# askopenfilename- This function opens a file dialog box that allows the user to browse and select a file
vid = askopenfilename()

# It will load the selected video file
video = moviepy.editor.VideoFileClip(vid)

# This extracts the audio track from the video object and assigns it to the aud variable.
aud = video.audio

# This will save the audio file as an mp3 format to the folder where the video was present.
aud.write_audiofile("demo.mp3")
