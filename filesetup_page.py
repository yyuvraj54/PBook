from sys import flags
from textwrap import fill
from tkinter import *

import scrollbar
from tkinter import ttk
from PIL import Image
import GraphicModulation
import itemselection
import fileOprations


page=Tk()
page.title("Private Book")
newfile=0

#Default settings
size=[700,600]
navframecolor='#013D7A'
font=('oswald bold',12)

page.minsize(f"{size[0]}",f"{size[1]}")
#page.maxsize(f"{size[0]}",f"{size[1]}")
page.config(bg='white')

# NAVBAR

mainFrame=Frame(page)
mainFrame.pack(fill=BOTH,expand=True)
Navframe=Frame(mainFrame,height=80,width=f"{size[0]}",bg=navframecolor)
Navframe.pack(fill=X,side=TOP,anchor=NW)
MainLogo = Image.open('icons/logo.png')
logoImage = GraphicModulation.ImageResize(MainLogo,38,38)

logoframe=Frame(Navframe,bg=navframecolor)
logoframe.pack(side=LEFT,padx=10)
logo_label=Label(logoframe,image=logoImage,background=navframecolor)
logo_label.pack(side=LEFT)
logoText=Label(logoframe,text="Name (Unknow)",background=navframecolor,font=font,fg='white')
logoText.pack(side=LEFT)


separator = ttk.Separator(mainFrame, orient='horizontal')
separator.pack(fill='x',pady=5,padx=20)




#create New file
tempbg="white"
buttonbg="white"

newframe=scrollbar.ScrollableFrameHorizontal(mainFrame,bg=tempbg)
newframe.pack(fill=X,side=TOP)

FrameTemplate=Frame(newframe.scrollable_frame)
FrameTemplate.pack()

inframe=Frame(FrameTemplate,bg=tempbg)
inframe.pack(fill=BOTH,expand=True,pady=5,padx=15)

Temp=Label(inframe,text="Start with a template",font=font)
Temp.pack(pady=10,anchor=NW,side=TOP)


startNewbutton=itemselection.file(inframe,label="New file",image="icons//newfile.png",height=100,width=85)
startNewbutton.pack(anchor=NW)


# Recent
recentbg="white"
saveframe=scrollbar.ScrollableFrameHorizontal(mainFrame,bg=recentbg)
saveframe.pack(fill=X,side=TOP)

FrameTemplate2=Frame(saveframe.scrollable_frame)
FrameTemplate2.pack()

inframe2=Frame(FrameTemplate2,bg=recentbg)
inframe2.pack(fill=BOTH,expand=True,pady=5,padx=15)


Recent=Label(inframe2,text="Recents",font=font)
Recent.pack(pady=10,anchor=NW,side=TOP)

files=fileOprations.TextFileNames()
print(len(files))
if len(files)==0:
    l=Label(inframe2,text="No Recent file created",bg='black',fg="white")
    l.pack(side=BOTTOM)
else:
    pass
bottomframe=Frame(mainFrame,bg='red')
bottomframe.pack(fill=X,expand=True,side=BOTTOM,anchor=SW)



flag=0
def closetab():
    page.destroy()

def newfile():
    flag=1
    page.destroy()
    return flags

    

CreateNewFilebutton=Button(bottomframe,text='New file',relief=FLAT,command=newfile)
CreateNewFilebutton.pack(side=RIGHT,padx=15,pady=10)

Cancelbutton=Button(bottomframe,text='Cancel',relief=FLAT,command=closetab)
Cancelbutton.pack(side=RIGHT,padx=15,pady=10)



page.mainloop()




#import os
#os.system('python3 main_page.py')
