from pytube import YouTube

url = "https://www.youtube.com/watch?v=HmegNIOA94U"


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")



youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print("  ", stream)


stream = youtube_video.streams.get_highest_resolution()
print("Steam vidéo: ", stream)
print("Téléchargement...")
stream.download()
print("OK")
