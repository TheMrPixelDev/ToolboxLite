from dialog import Dialog
import os
import time

def download_mp4():

    youtubelink = str(input("Please enter a valid youtube link: "))

    if youtubelink != None and youtubelink != " " and youtubelink != "":
        print(f"Starting download '{youtubelink}'...Please wait...")
        try:
            os.system(f'youtube-dl.exe -f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best\" \"{youtubelink}\"')
        except Exception as e:
            print("An error occured: " + e)
    else:
        print("Please enter a valid link...")
        download_mp4()

def download_mp3():
    
    youtubelink = str(input("Please enter a valid youtube link: "))

    if youtubelink != None and youtubelink != " " and youtubelink != "":
        print(f"Starting download of '{youtubelink}'...Please wait...")
        try:
            os.system(f'youtube-dl -x --audio-format mp3 --prefer-ffmpeg \"{youtubelink}\"')
        except Exception as e:
            print("An error occured: " + e)
    else:
        print("Please enter a valid link...")
        download_mp4()

def youtube_dl_dialog():

    from main import mainDialog

    os.system('cls')
    result = os.system("youtube-dl --version")
    if result != 0:
        print("To use this Tool you need to have youtube-dl and ffmpeg installed and added to PATH.")
        time.sleep(3)
        mainDialog()
    elif result == 0:
        yt_dialog = Dialog("Chose a function of youtube-dl:")
        yt_dialog.setOptions(("Download only MP3-Audio", download_mp3),("Download whole Video as MP4",download_mp4),("<-- Back", mainDialog))
        yt_dialog.show()
