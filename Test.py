from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import webbrowser
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
   
    Arrayofscript = data.replace('\n', '').split(",")
    Filename = 1
    language = 'en'
    indexno = 0
    Arrayofscript = list(Arrayofscript)
    if Arrayofscript[-1] == " ":
    
        del Arrayofscript[-1]
        zz = 1
   
    for i in Arrayofscript:
        Filename = int(Filename)
        myobj = gTTS(text=Arrayofscript[indexno], lang=language, slow=False)
        Filename = str(Filename)
        myobj.save(Filename+".mp3")
        Filename = int(Filename)
        Filename = Filename + 1
        indexno = indexno + 1
        zz = 1

    Label(ws,text="Converted successfully",background="powderblue",height=10).pack()
    tf.close()

def callback(url):
    webbrowser.open_new(url)


ws = Tk()
ws.title("RII")
ws.geometry("400x450")
ws['bg']='powderblue'

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)


Button(ws, text="Convert",command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)
Label( ws, text="Copyrighted by A. Sharan" ,background="powderblue" ).pack(side="bottom")
msg = Message( ws, text="Click on Convert and selcet the script you want to convert, RII will convert them into seprate audio files for you to use when needed. Click this for documentation" ,cursor="hand2",width=100,background="powderblue" )
msg.pack(side="top")
msg.bind("<Button-1>", lambda e:
    callback("https://ksindustriz.com"))
ws.mainloop()