import tkinter as tk
import webbrowser
import pyperclip
import os
from PIL import ImageTk, Image

class PopUp():

    DirectoryAbove = "/".join(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").split("/")[:-1])
  
    def __init__(self, Header, Link, TextToCopy, CanCopy = True, AutoCloseIn = 0):
        self.SetUpUI(Header, Link, TextToCopy, CanCopy)
        self.window.focus_force()
        self.window.iconphoto(False, ImageTk.PhotoImage(file = PopUp.DirectoryAbove + "/Image/Logo/Icon.png", master=self.window))

        if AutoCloseIn != 0:
            print(f"Closing in {AutoCloseIn}s")
            self.window.after(int(AutoCloseIn * 1000), lambda: self.window.destroy())

        self.window.mainloop()
    
    def OpenLink(self, link):
        if (link == "__CLOSE__"): 
            self.window.destroy()
        else:
            webbrowser.open_new_tab(link)

    def SetUpUI(self, Header, Link, TextToCopy, CanCopy) -> None:
        self.window = tk.Tk()
        self.window.geometry("300x150")
        self.window["bg"] = "#121212"
        self.window.title(f"Unrealify - {Header}")
        self.window.resizable(False, False)

        self.HeaderLabel = tk.Label(master=self.window, text=Header.capitalize(), bg="#121212", font=("Yu Gothic Bold", 24 if (len(Header) <= 10) else (int(24 - (len(Header) - 10)))) if (int(24 - (len(Header) - 10))) > 10 else 10, foreground="#92DDC8")
        self.HeaderLabel.pack()
        
        self.DescriptionLabel = tk.Text(master=self.window, bg="#292929", foreground="white", font=("Yu Gothic", 10), borderwidth=0)
        self.DescriptionLabel.insert(tk.INSERT, TextToCopy)
        self.DescriptionLabel.place(x=10, y=50, width=220 if (CanCopy) else 280, height=50)

        if (CanCopy):
            self.CopyButton = tk.Button(master=self.window, text="Copy", command=lambda: [pyperclip.copy(TextToCopy)], bg="#292929", foreground="#FFF", borderwidth=0)
            self.CopyButton.place(x=290, rely=0.5, width=50, height=50, anchor="e")
        
        LinkButtonText = "Show In Browser"
        if (Link == "__CLOSE__"):
            LinkButtonText = "Close"

        self.LinkButton = tk.Button(master=self.window, text=LinkButtonText, command=lambda: [self.OpenLink(Link)], bg="#292929", foreground="#FFF", borderwidth=0)
        self.LinkButton.place(relx=0.5, rely=1, width=300, height=25, anchor="s")

if __name__ == "__main__":
    a2 = PopUp("uassetcompon", "__CLOSE__", "fdjkladsfjasjdhkfhjkfdhjhjkafdhjkhafkdshasfdhjafdshjdsfjafadsjkdsaf")