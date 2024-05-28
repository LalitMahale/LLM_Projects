import os 
from pytube import YouTube
from moviepy.editor import *

class Youtube:
    def __init__(self, video_url):
        self.cwd = os.getcwd()
        self.video_url = video_url

    def GetYoutubeAudio(self):
        try:
            yt = YouTube(self.video_url)
            video_stream = yt.streams.get_audio_only()
            video_stream.download(filename='temp_audio')
            clip = AudioFileClip('temp_audio.mp3')
            clip.write_audiofile('temp_audio.mp3')
        except Exception as e:
            print(f"Error downloading audio: {e}")

if __name__ == "__main__":
    video_url = "https://youtu.be/yF5G46kSKR4?si=KRtErfxdZ7qU3i9M"  # Input your YouTube video link here
    Youtube(video_url=video_url).GetYoutubeAudio()
