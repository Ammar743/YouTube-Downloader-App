import tkinter as tk
import customtkinter
from pytube import YouTube
from tkinter import messagebox

def start_download():
    try:
        youtube_link = entry.get()
        youtube_object = YouTube(youtube_link, on_progress_callback = on_prgress)
        video = youtube_object.streams.get_highest_resolution()
        title.configure(text = youtube_object.title)
        if video is not None:
            video.download()
            finish_label.configure(text="Download Complete, The video has been successfully downloaded.", text_color = "white")
        else:
            raise Exception("Unable to find video stream")
    except Exception as e:
        print(f"Error: {e}")
        finish_label.configure(text = "Error, Invalid YouTube link.", text_color = "red")

def on_prgress(stream , chunk, bytes_remaining):
    total_size = stream.filesize 
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    percentage.configure(text = per + "%") 
    percentage.update()
    
    # Update progress bar
    progressBar.set(float(percentage_of_compeletion) / 100)  


# System setting-Light mode/ Dark mode
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert The YouTube Link")
title.pack(padx=10, pady=(120,5))

# Link input
url_var = tk.StringVar()
entry = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
entry.pack(padx=10, pady=5)

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()


# show percentage of the downlowad
percentage =customtkinter.CTkLabel(app, text= "0%")
percentage.pack(padx=10, pady=(10, 0))

# Progressbar
progressBar = customtkinter.CTkProgressBar(app, width= 400, height= 30)
progressBar.set(0)
progressBar.pack(padx = 10, pady = (2, 10))

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=start_download)
download_button.pack()



# Run app
app.mainloop()
