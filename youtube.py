from tkinter import *
from pytube import YouTube

win = Tk()
win.geometry('500x300')
win.resizable(0,0)
win.title("Youtube Video Downloader")

Label(win,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(win, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

link_enter = Entry(win, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(win, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(win,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

win.mainloop()
