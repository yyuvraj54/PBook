import tkinter as tk
from tkinter import ttk


class ScrollableFrameVertical(ttk.Frame):
    def __init__(self, container,bg='blue',height=100,width=300, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        if height==1:
            canvas = tk.Canvas(self,bg=bg,width=width)    
        else:
            canvas = tk.Canvas(self,bg=bg,height=height,width=width)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True,pady=5)
        scrollbar.pack(side="right", fill="y")

class ScrollableFrameHorizontal(ttk.Frame):
    def __init__(self, container,bg="red", *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self,bg=bg)
        scrollbar = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(xscrollcommand=scrollbar.set)

        canvas.pack(side="top", fill="both", expand=True,padx=5)
        scrollbar.pack(side="bottom", fill="x")

if __name__=="__main__":
    root = tk.Tk()
    frame = ScrollableFrameVertical(root)
    frame2= ScrollableFrameHorizontal(root)

    for i in range(50):
        ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

    for i in range(50):
        ttk.Label(frame2.scrollable_frame, text="Sample scrolling labelfsdkljklsdhfjkdshfsdkjfhsdjkfhsdjkfhsdjkfhsdjkfhsdjkfhsdkjfhsdkjfhsdkj").pack()

    frame.pack()
    frame2.pack()
    root.mainloop()