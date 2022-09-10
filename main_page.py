from tkinter import *
import datetime as dt
from  tkinter import font
import GraphicModulation
from PIL import ImageTk, Image
from tkinter import colorchooser
from tkinter import font


#defaults
h=1000
w=600
back='#2e2e2e'
buttonframe_color="#B00020"

front='white'

class windows:
    def __init__(self,main,*args, **kwargs): 
        self.highlightcolr='#308D46'      
        
        self.main=main
        geometry=self.GetGeometry()


        def hideit():
            print(self.settingFrame.winfo_viewable())
            if self.settingFrame.winfo_viewable():
                self.settingFrame.update()

                self.settingFrame.pack_forget()
                self.toolFrame.update()
            else:
                self.settingFrame.update()
                self.settingFrame.pack(pady=2,anchor=NW,side=TOP,fill=X)
                self.settingFrame.update()


        menubar = Menu(self.main)
        self.main.config(menu=menubar)
        file_menu = Menu(menubar)
        settings_menu = Menu(menubar)
        view_menu = Menu(menubar)
        
        menubar.add_cascade(label="File",menu=file_menu)
        menubar.add_cascade(label="Settings",menu=settings_menu)
        menubar.add_cascade(label="View",menu=view_menu)

        file_menu.add_command(label='Exit',command=self.main.destroy)

        settings_menu.add_cascade(label="Choose Writing Pad Color",command=self.writerpad_color)
        settings_menu.add_cascade(label="Select Text color",command=self.text_color)
        settings_menu.add_cascade(label="Choose Highlighter color",command=self.highlight_color)
        view_menu.add_cascade(label="Hide Settings tab",command=hideit)
        
        

        # self.backImage=PhotoImage(file="icons//background1.png")
        # self.imagelabel=Label(self.main,image=self.backImage)
        # self.imagelabel.place(relx=0,rely=0)

        self.textFrame=Frame(self.main,height=geometry[0]-50)
        self.textFrame.pack(fill=BOTH,side='left',expand=True)
        self.textFrame.pack_propagate(0)
        

        
        
        # self.textbox=Textbox.TEXTBOX(self.textFrame)
        # self.textbox.pack(fill=BOTH,side=TOP,expand=True)
        # self.textbox.pack_propagate(0)
        self.textbox=Text(self.textFrame,font=("Helvetica", 13),height=geometry[0]-100,wrap=WORD)
        self.textbox.pack(fill=BOTH,side=TOP)
        self.textbox.pack_propagate(0)
        
        propertyFrame=Frame(self.main,bg=back)

        



        global centreImage
        centre_icon = Image.open('icons/centre_icon.png')
        centreImage=GraphicModulation.ImageResize(centre_icon,15,17)
        #>>>>>>>>> BUTTON FRAME
        self.buttonframe=Frame(propertyFrame,bg=buttonframe_color)
        self.buttonframe.pack(pady=5,padx=5,anchor=NW,side=TOP,fill=X)
        self.l=Label(self.buttonframe,text='Edit Tool',fg="white",bg=buttonframe_color)
        self.l.pack(pady=5,side=TOP)
        

        
        
        self.boldbut=Button(self.buttonframe,text="B",font=("Helvetica", 13, font.BOLD),command=self.change_bold,bg=buttonframe_color,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0,borderwidth=0)
        self.boldbut.pack(padx=3,side='left',pady=5)
        
        
        self.colorchange=Button(self.buttonframe,bg=buttonframe_color,text='A',font=("Helvetica", 13),command=self.changetext_selected_color,relief=GROOVE,highlightbackground=back,fg=self.highlightcolr,highlightthickness=0,bd=0,borderwidth=0)
        self.colorchange.pack(padx=3,side='left',pady=5)

        

        self.leftText=Button(self.buttonframe,bg=buttonframe_color,text="LEFT",command=self.selected_text_left,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0)
        self.leftText.pack(padx=3,side='left',pady=5)

        self.centreText=Button(self.buttonframe,bg=buttonframe_color,image=centreImage,command=self.selected_text_centre,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0)
        self.centreText.pack(padx=3,side='left',pady=5)


        self.rightText=Button(self.buttonframe,bg=buttonframe_color,text="RIGHT",command=self.selected_text_right,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0)
        self.rightText.pack(padx=3,side='left',pady=5)

        

        def isSelectedI(e):
            x1= e.x+5
            y1= e.y+5

            writer_screen_width=self.textbox.winfo_width()
            writer_screen_height=self.textbox.winfo_height()
            print(x1,y1,writer_screen_width,writer_screen_height)
        
            if x1+150>=writer_screen_width:
                x1=x1-200
            if y1+100>=writer_screen_height:
                y1=y1-100

            if self.textbox.tag_ranges("sel"):
                

                propertyFrame.place(x=x1,y=y1)    
                propertyFrame.update()
                self.textbox.update()
                       
            else:
    
                try:
                    propertyFrame.place(x=1000,y=1000)
                    self.textbox.update()
                    propertyFrame.place_forget()
                    
                    
                    
                except:pass    
        self.textbox.bind('<ButtonRelease-1>',isSelectedI)

        


        self.toolFrame=Frame(self.main,bg=back)
        self.toolFrame.pack(anchor=NW,side='right',fill=BOTH)

            
        self.main.bind('<KeyRelease>',self.GetWordCount)
        self.showinformation(self.toolFrame)
        #self.textbox.bind("<Button-3>", self.showinformation(self.toolFrame))

        # global boldimage
        # boldbuttonImage = Image.open('icons/bold_icon.png')
        # boldimage=GraphicModulation.ImageResize(boldbuttonImage,48,55)

        # global highlightimage
        # highlightImage = Image.open('icons/highlight_icon.png')
        # highlightimage=GraphicModulation.ImageResize(highlightImage,48,55)

        
        settingsFrame_color='#47ABD8'
        self.settingFrame=Frame(self.toolFrame,bg=settingsFrame_color)
        self.settingFrame.pack(pady=2,anchor=NW,side=TOP,fill=X)
        Label(self.settingFrame,text='Settings Tool',fg="white",bg=settingsFrame_color).pack(pady=5,side=TOP)

        self.colorpickertoolButton=Button(self.settingFrame,text='choose highlight color',command=self.highlight_color,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0,bg=settingsFrame_color)
        self.colorpickertoolButton.pack(anchor=NW,pady=2,padx=2)

        self.changeWritercolor=Button(self.settingFrame,text='WriterPad Color',command=self.writerpad_color,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0,bg=settingsFrame_color)
        self.changeWritercolor.pack(anchor=NW,pady=2,padx=2)
        
        self.textcolor=Button(self.settingFrame,text='Text Color',command=self.text_color,relief=GROOVE,highlightbackground=back,highlightthickness=0,bd=0,bg=settingsFrame_color)
        self.textcolor.pack(anchor=NW,pady=2,padx=2)

        
        
    def selected_text_left(self):

        try:

            self.textbox.tag_configure("left_text", justify=LEFT)
            self.textbox.tag_configure("right_text", justify=RIGHT)
            self.textbox.tag_configure("centre_text", justify='center')
        
            
            if "left_text" in  self.textbox.tag_names("sel.first"):
                self.textbox.tag_remove("left_text","sel.first","sel.last")
            else:
                self.textbox.tag_remove("right_text","sel.first","sel.last")
                self.textbox.tag_remove("centre_text","sel.first","sel.last")
                self.textbox.tag_add("left_text","sel.first","sel.last")
        except:print("No Text Selected")  

    def selected_text_right(self):
        try:
            
            self.textbox.tag_configure("left_text", justify=LEFT)
            self.textbox.tag_configure("right_text", justify=RIGHT)
            self.textbox.tag_configure("centre_text", justify='center')
        
            
            if "right_text" in  self.textbox.tag_names("sel.first"):
                self.textbox.tag_remove("right_text","sel.first","sel.last")
            else:
                self.textbox.tag_remove("left_text","sel.first","sel.last")
                self.textbox.tag_remove("centre_text","sel.first","sel.last")
                self.textbox.tag_add("right_text","sel.first","sel.last")
        except:print("No Text Selected")  

    def selected_text_centre(self):

        try:
            
            self.textbox.tag_configure("left_text", justify=LEFT)
            self.textbox.tag_configure("right_text", justify=RIGHT)
            self.textbox.tag_configure("centre_text", justify='center')

           
            if "centre_text" in  self.textbox.tag_names("sel.first"):
                self.textbox.tag_remove("centre_text","sel.first","sel.last")
            else:
                self.textbox.tag_remove("left_text","sel.first","sel.last")
                self.textbox.tag_remove("right_text","sel.first","sel.last")
                self.textbox.tag_add("centre_text","sel.first","sel.last")
        except:print("No Text Selected")   
    def showinformation(self,frame):
        show_bg="grey"
        filename="None"
        global infoframe
        infoframe=Frame(frame,bg=show_bg)
        date=dt.datetime.now()
        todaytext=Label(infoframe,text=f"{date:%A, %B %d, %Y}",bg=show_bg,fg=front)
        todaytext.pack(anchor=NW)
        title=Label(infoframe,text=f"Title: {filename}",bg=show_bg,fg=front)
        title.pack(anchor=NW)

        
        self.wordCount=Label(infoframe,text=f"Words: {0}",bg=show_bg,fg=front)
        self.wordCount.pack(anchor=NW)
        self.lines=Label(infoframe,text=f"Lines: {0}",bg=show_bg,fg=front)
        self.lines.pack(anchor=NW)
        infoframe.pack(side=TOP,anchor=NW,fill=X)
    def change_bold(self):
            self.textbox.tag_configure("boldtext",font= self.textbox.cget("font")+" bold")
            try:
                if "boldtext" in  self.textbox.tag_names("sel.first"):
                    self.textbox.tag_remove("boldtext","sel.first","sel.last")
                else:
                    self.textbox.tag_add("boldtext","sel.first","sel.last")
                    
            except:
                print("No Text selected")
    def changetext_selected_color(self):
            try:
                self.textbox.tag_config("sel_text_color",foreground=self.highlightcolr)
                if "sel_text_color" in self.textbox.tag_names('sel.first'):
                    self.textbox.tag_remove("sel_text_color","sel.first","sel.last")
                else:
                    self.textbox.tag_add("sel_text_color","sel.first","sel.last")
            except:
                print('No text selected')     
    def Textproperty(self): 
            text_property=font.Font(font=self.textbox['font'])    
            if text_property.actual()['weight'] =='normal':
                self.textbox.configure(font=('Helvetica',15 , 'bold'))
            if text_property.actual()['weight'] == 'bold':
                self.textbox.configure(font=('Helvetica',13, 'normal'))
    def GetGeometry(self):
        self.main.update()
        rootHeight = main.winfo_height()
        rootWidth = main.winfo_width()
        v=(rootHeight,rootWidth)
        return v
    def GetWordCount(self,e):
        words = self.textbox.get("1.0","end-1c")
        list_of_charater=[*words]

        if words=="loren1000":
            text="""What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
The standard Lorem Ipsum passage, used since the 1500s
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
            self.textbox.insert(1.0,text)
        spacecount=list_of_charater.count(" ")
        linescount=list_of_charater.count("\n")
        tabcount=list_of_charater.count("   ")
        self.lines.config(text=f"Lines: {linescount}")
        self.wordCount.config(text=f"Words: {len(words)-spacecount-linescount-tabcount}")
    def highlight_color(self):
        
        color_code = colorchooser.askcolor(title ="Choose color")
        self.highlightcolr=color_code[1]
        self.colorpickertoolButton.config(fg=color_code[1])
        self.colorchange.config(fg=color_code[1])
        return color_code[1]
    def writerpad_color(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        if color_code[1]=="#FFFFFF":self.changeWritercolor.config(fg="black")
        else:self.changeWritercolor.config(fg=color_code[1])
        self.textbox.config(bg=color_code[1])
    def text_color(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        self.textcolor.config(fg=color_code[1])
        self.textbox.config(fg=color_code[1])
    def changeFontSize(self,new):
        self.textbox.tag_add("bt2", "sel.first", "sel.last")
        new_font = font.Font(font=self.textbox.cget("font"))
        size = new_font.actual()["size"]
        new_font.configure(size=new)
        self.textbox.tag_config("bt2", font=new_font)


    

  
            

if __name__=="__main__":
    main=Tk()
    main.geometry(f'{h}x{w}+200+200')    # set new geometry
    main.minsize(600,400)
    main.title("PrivateBook")
    main.config(bg=back)

    # main.wm_attributes("-transparent", True)
    # main.config(bg='systemTransparent')

    m=windows(main)   
    main.mainloop()

 