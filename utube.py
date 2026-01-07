import yt_dlp

print("=== YouTube Downloader ===")

url = input("Dose to link tou YouTube: ")

options = {
    "format": "best",
    # "format": "bestvideo[height<=720]+bestaudio/best[height<=720]",
    "outtmpl": "%(title)s.%(ext)s",  # αποθήκευση στον ίδιο φάκελο με το αρχείο .py
}

try:
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


    print("✅ To video katevike epitixos!")

except Exception as e:
    print("❌ Sfalmα:", e)
