import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Default Button for prewritten text
        self.btn1 = Button(self.master, text="Default HTML Page", width=30, height=2, command = self.defaultHTML)
        self.btn1.grid(row= 4, column= 1, columnspan=1, padx = (5, 5) , pady = (5, 5), sticky='e')
        
        # Button for Submit Custom text
        self.btn2 = Button(self.master, text="Submit Custom Text", width=30, height=2, command = self.customHTML)
        self.btn2.grid(row=4, column=2, columnspan=1, padx = (5, 5), pady = (5, 5), sticky='e')

        # Label for window explaining the buttons
        self.label = Label(self.master, text="Enter custom text or click the Default HTML button")
        self.label.grid(row=2, column=1, columnspan=2, padx=(5, 5), pady=(5, 5), sticky='w')
        
        # Entry for Submitting the custom text
        self.custom_text = StringVar()
        self.custom_text = Entry(self.master, textvariable = self.custom_text, width=95)
        self.custom_text.grid(row= 3, column=1, padx= (10, 10), pady = (10, 10))
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>{htmlText}</h1>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # New function for the input text
    def customHTML(self):
        htmlText = self.custom_text.get()
        htmlFile = open("index.html", "w")
        htmlContent = f"<html>\n<body>\n<h1>{htmlText}</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
