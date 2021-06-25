import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("PDF Text Extract")

canvas = tk.Canvas(root, width=600, height=300).grid(columnspan=3, rowspan=3)

#logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text")
instructions.grid(columnspan=3, column=0, row=1)

def openFile():
    browseText.set("loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a File", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        #textbox
        textBox = tk.Text(root, height=10, width=50, padx=15, pady=15)
        textBox.insert(1.0, page_content)
        textBox.grid(column=1, row=3)

        browseText.set("Browse")
    else:
        browseText.set("Browse")

#Browse Button
browseText = tk.StringVar()
browseBtn = tk.Button(root, textvariable=browseText, command=lambda:openFile(), bg="#20bebe", fg="white", height=2, width=10, bd=0)
browseText.set("Browse")
browseBtn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250).grid(columnspan=3)

root.mainloop()