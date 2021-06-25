import tkinter as tk

sudokuArr = [   [4,0,0,0,0,8,0,0,2],
                [0,0,0,7,0,0,0,0,0],
                [0,0,0,0,9,1,0,7,0],
                [0,1,0,5,0,6,0,0,0],
                [6,0,0,0,0,4,0,9,0],
                [0,5,0,0,0,0,8,0,0],
                [3,4,0,0,0,2,0,0,1],
                [8,0,0,0,3,0,0,0,6],
                [0,2,0,8,1,0,0,0,0]  ]

labels = []

def printArr(arr):
    for i in arr:
        print(i)
    print("\n")

def sudokuFull(array):
    for i in array:
        for j in i:
            if j == 0:
                return False
    return True

def isCorrect(x,y,value):
    newSudoku = sudokuArr.copy()
    newSudoku[y][x] = value
    
    row = newSudoku[y].copy()
    del row[x]

    column = []
    for i in newSudoku:
        column.append(i[x])
    del column[y]

    box = []
    startCol = x - x % 3
    startRow = y - y % 3
    for i in range(3):
        for j in range(3):
            box.append(newSudoku[startRow+i][startCol+j])
    del box[3*(y%3)+(x%3)]

    if newSudoku[y][x] in row:
        return False
    elif newSudoku[y][x] in column:
        return False
    elif newSudoku[y][x] in box:
        return False
    else:
        return True

def solveSudoku(sudokuArr):
    for i in range(0,81):
        y=i//9
        x=i%9
        if sudokuArr[y][x] == 0:
            for value in range (1,10):
                if isCorrect(x,y,value):
                    sudokuArr[y][x]=value
                    if sudokuFull(sudokuArr):
                        print("Grid Complete and Checked")
                        return True
                    else:
                        if solveSudoku(sudokuArr):
                            return True
            break
    sudokuArr[y][x]=0

def start(goText):
    goText.set("Calculating")
    if(solveSudoku(sudokuArr)):
        print(sudokuArr)
        drawSudoku(sudokuArr)

def drawSudoku(sudokuArr):
    count = 0
    for i in sudokuArr:
        for j in i:
            labels[count]['text'] = j
            count = count + 1

def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=297, height=297)
    canvas.grid(columnspan=9, rowspan=9)

    for i in range(10):
        canvas.create_line(0, i*33, 300, i*33)
        canvas.create_line(i*33, 0, i*33, 300)

    for y in range(9):
        for x in range(9):
            label = tk.Label(root, text=str(x) + str(y))
            labels.append(label)
            label.grid(column=x, row=y)
    
    drawSudoku(sudokuArr)

    canvas = tk.Canvas(root, width=297, height=100).grid(columnspan=9, rowspan=3)

    goText = tk.StringVar()
    goBtn = tk.Button(root, textvariable=goText, command=lambda:start(goText), bg="gray", fg="white", width=10, bd=0)
    goText.set("Go")
    goBtn.grid(column=0, row=9, columnspan=9)

    root.mainloop()
    
if __name__ == "__main__":
    main()