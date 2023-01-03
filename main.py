import tkinter as tk
from tkinter import filedialog
import pytube


def select_download_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory(parent=root, title='Please select a download path')
    return file_path


def download_video(url, download_path):
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    video.download(download_path)
    print(f'Video downloaded to {download_path}')


url = input('Enter the YouTube URL: ')
download_path = select_download_path()
download_video(url, download_path)
