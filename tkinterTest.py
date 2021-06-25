import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=297, height=297)
canvas.grid(columnspan=9, rowspan=9)

for i in range(10):
    canvas.create_line(0, i*33, 300, i*33)
    canvas.create_line(i*33, 0, i*33, 300)


for i in range(9):
    for j in range(9):
        instructions = tk.Label(root, text="1").grid(column=j, row=i)

canvas = tk.Canvas(root, width=297, height=100).grid(columnspan=9, rowspan=3)

goText = tk.StringVar()
goBtn = tk.Button(root, textvariable=goText, bg="gray", fg="white", width=10, bd=0)
goText.set("Go")
goBtn.grid(column=0, row=9, columnspan=9)


root.mainloop()