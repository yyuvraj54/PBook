from tkinter import *
from PIL import Image
import GraphicModulation

class file(Frame):
  def __init__(self,main_window,image="icons//file.png",label=None,filePath=None,height=40,width=45):
      Frame.__init__(self,main_window,image=None,label=None,filePath=None,height=40,width=45)
      self.image=image
      self.label=label
      self.filePath=filePath
      self.filephoto = Image.open(image)
      self.fileimage = GraphicModulation.ImageResize(self.filephoto,width,height)


      self.button=Button(self,image=self.fileimage,bd=0)
      self.textlabel=Label(self,text=self.label)

      self.button.grid(row=0,column=0)
      self.textlabel.grid(row=1,column=0)




'''
def newfile_boject(page):
    global filelogo,logo_file
    file = Image.open('icons/newfile.png')
    filelogo = GraphicModulation.ImageResize(file,100,130)
    logo_file=Label(page,image=filelogo,background='white',bg="blue")
    logo_file.pack(side=LEFT)

'''



if __name__=="__main__":

    page=Tk()
    but=file(page,label="clickMe")
    but1=file(page,label="clickMe")
    but2=file(page,label="clickMe")
    but.pack()
    but2.pack()
    but1.pack()


    page.mainloop()

    
