from pytube import YouTube
from pytube import Playlist
yt = Playlist(str(input("Enter the video link: ")))
destination = str(input("Enter the destination: "))
yt.download_all(destination)
print("Number of videos in playlist:%s"%len(yt.video_urls))
print("\video Has been successfully downloaded")
