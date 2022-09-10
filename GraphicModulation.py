from PIL import ImageTk, Image
def ImageResize(ImageSource,h,w):
    image = ImageSource.resize((h,w), Image.ANTIALIAS)
    Tk_ready_Image = ImageTk.PhotoImage(image)
    return Tk_ready_Image
