import tkinter as tk
from pytube import YouTube
import webbrowser

def download_video():
    url = entry.get()
    quality = quality_var.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res = quality).first()
        stream.download(output_path="Downloads")
        webbrowser.open(stream.default_filename)
        label.config(text="Successfully Done")
    except Exception as e:
        label.config(text="Error")


window = tk.Tk()
window.title("youtube Downloader")
window.geometry("300x400")
window.configure(background="gray")
label = tk.Label(window, text="Enter the link:")
label.config(bg="#FF5722")
label.pack(side="top")
entry = tk.Entry(window)
entry.pack()
quality_var = tk.StringVar(window)
quality_var.set("720p")
quality_label = tk.Label(window, text = "resolution:")
quality_label.place(x=115, y=70)
quality_menu = tk.OptionMenu(window, quality_var, "144p", "360p", "720p", "1080p")
quality_menu.place(x=112, y=92)
quality_menu.config(bg="#CCA42A")
download_button = tk.Button(window, text = "Download", command=download_video)
download_button.pack(side="bottom", pady=25)
download_button.config(bg="green")
window.mainloop()

