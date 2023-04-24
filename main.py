import tkinter
import customtkinter 
from pytube import YouTube


def startDownload():
    try:
        ylink=link.get()
        yobject=YouTube(ylink,on_progress_callback=onprogress)
        video=yobject.streams.get_highest_resolution()
        title.configure(text=yobject.title, text_color='dark-blue')
        feedback.configure(text='')
        video.download()
        feedback.configure(text="Download completed successfully!!!",text_color="green")
    except:
        feedback.configure(text="Download error",text_color="red")

#progrss function
def onprogress(stream,chunk,bytes_remaining):
    totalsize=stream.filesize()
    bytes_downloaded=totalsize-bytes_remaining
    percentageOfCompletion=bytes_downloaded/totalsize*100
    per=str(int(percentageOfCompletion))
    pcentage.configure(text=per + "%")
    pcentage.update()

    #update progessnr
    progressbar.set(float(percentageOfCompletion/100))


    
#setting ap the system colour scheme
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("system")

#setting our app
app=customtkinter.CTk()
app.geometry("720*480")
app.title("Youtube Downloader")

#adding ui elements 
title=customtkinter.CTkLabel(app,text="Insert youtube link here")
title.pack(padx=10,pady=10)

#link input
input=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40,textvariable=input)
link.pack()


#finished download feedback
feedback=customtkinter.CTkLabel(app,text="")
feedback.pack()

#progressbar
pcentage=customtkinter.CTkLabel(app,text="0%")
pcentage.pack()

progressbar=customtkinter.CTkProgressBar(app,width=400)
progressbar.set(0)
progressbar.pack(padx=10,pady=10)


#Download button
download=customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)

#run the app
app.mainloop()

