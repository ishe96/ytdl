from pytube import YouTube

def Download(link):
    youtubeObj = YouTube(link)
    youtubeObj = youtubeObj.streams.get_highest_resolution()

    try:
        youtubeObj.download()
    except:
        print("Sorry, download failed")

    print("Success, download is in progress")

link = input("Paste url link here : ")

Download(link)