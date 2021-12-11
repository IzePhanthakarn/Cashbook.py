from ttkbootstrap import Style
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import time

style = Style(theme="superhero")
mainWindow = style.master
mainWindow.title("Cash Book")
mainWindow.geometry("1280x720")

# do function when click "calculat" button (save the list entered by the user and calculate the total price).


def calculateClick():
    try:
        paylist = en1.get()
        price = float(en2.get())
        textList1 = lebelList1.cget("text")
        textList2 = lebelList2.cget("text")
        textList3 = lebelList3.cget("text")
        textList4 = lebelList4.cget("text")
        textList5 = lebelList5.cget("text")
        textList6 = lebelList6.cget("text")
        textList7 = lebelList7.cget("text")
        textList8 = lebelList8.cget("text")
        textList9 = lebelList9.cget("text")
        textTotal1 = lebelTotal1.cget("text")
        textTotal2 = lebelTotal2.cget("text")
        textTotal3 = lebelTotal3.cget("text")
        textTotal4 = lebelTotal4.cget("text")
        textTotal5 = lebelTotal5.cget("text")
        textTotal6 = lebelTotal6.cget("text")
        textTotal7 = lebelTotal7.cget("text")
        textTotal8 = lebelTotal8.cget("text")
        textTotal9 = lebelTotal9.cget("text")

        try:
            intTotal2 = float(textTotal1) + price
            intTotal3 = float(textTotal2) + price
            intTotal4 = float(textTotal3) + price
            intTotal5 = float(textTotal4) + price
            intTotal6 = float(textTotal5) + price
            intTotal7 = float(textTotal6) + price
            intTotal8 = float(textTotal7) + price
            intTotal9 = float(textTotal8) + price
        except:
            pass

        if (textList1 == ""):
            lebelList1.configure(text="1. " + paylist)
            lebelPrice1.configure(text=price)
        elif (textList2 == ""):
            lebelList2.configure(text="2. " + paylist)
            lebelPrice2.configure(text=price)
        elif (textList3 == ""):
            lebelList3.configure(text="3. " + paylist)
            lebelPrice3.configure(text=price)
        elif (textList4 == ""):
            lebelList4.configure(text="4. " + paylist)
            lebelPrice4.configure(text=price)
        elif (textList5 == ""):
            lebelList5.configure(text="5. " + paylist)
            lebelPrice5.configure(text=price)
        elif (textList6 == ""):
            lebelList6.configure(text="6. " + paylist)
            lebelPrice6.configure(text=price)
        elif (textList7 == ""):
            lebelList7.configure(text="7. " + paylist)
            lebelPrice7.configure(text=price)
        elif (textList8 == ""):
            lebelList8.configure(text="8. " + paylist)
            lebelPrice8.configure(text=price)
        elif (textList9 == ""):
            lebelList9.configure(text="9. " + paylist)
            lebelPrice9.configure(text=price)

        if (textTotal1 == ""):
            lebelTotal1.configure(text=price)
        elif (textTotal2 == ""):
            lebelTotal2.configure(text=intTotal2)
        elif (textTotal3 == ""):
            lebelTotal3.configure(text=intTotal3)
        elif (textTotal4 == ""):
            lebelTotal4.configure(text=intTotal4)
        elif (textTotal5 == ""):
            lebelTotal5.configure(text=intTotal5)
        elif (textTotal6 == ""):
            lebelTotal6.configure(text=intTotal6)
        elif (textTotal7 == ""):
            lebelTotal7.configure(text=intTotal7)
        elif (textTotal8 == ""):
            lebelTotal8.configure(text=intTotal8)
        elif (textTotal9 == ""):
            lebelTotal9.configure(text=intTotal9)
        lebelError.configure(text="")

    except:
        lebelError.configure(text="Price should be only number")

# do function when click "Clear All" button (clears all lists entered by the user).


def clearAllClick():
    lebelList1.configure(text="")
    lebelPrice1.configure(text="")
    lebelTotal1.configure(text="")
    lebelList2.configure(text="")
    lebelPrice2.configure(text="")
    lebelTotal2.configure(text="")
    lebelList3.configure(text="")
    lebelPrice3.configure(text="")
    lebelTotal3.configure(text="")
    lebelList4.configure(text="")
    lebelPrice4.configure(text="")
    lebelTotal4.configure(text="")
    lebelList5.configure(text="")
    lebelPrice5.configure(text="")
    lebelTotal5.configure(text="")
    lebelList6.configure(text="")
    lebelPrice6.configure(text="")
    lebelTotal6.configure(text="")
    lebelList7.configure(text="")
    lebelPrice7.configure(text="")
    lebelTotal7.configure(text="")
    lebelList8.configure(text="")
    lebelPrice8.configure(text="")
    lebelTotal8.configure(text="")
    lebelList9.configure(text="")
    lebelPrice9.configure(text="")
    lebelTotal9.configure(text="")
    lebelError.configure(text="")

# do function when click "Delete 1 item" button (deletes 1 entry that the user entered last).


def clearClick():
    textList1 = lebelList1.cget("text")
    textList2 = lebelList2.cget("text")
    textList3 = lebelList3.cget("text")
    textList4 = lebelList4.cget("text")
    textList5 = lebelList5.cget("text")
    textList6 = lebelList6.cget("text")
    textList7 = lebelList7.cget("text")
    textList8 = lebelList8.cget("text")
    textList9 = lebelList9.cget("text")
    if (textList9 != ""):
        lebelList9.configure(text="")
        lebelPrice9.configure(text="")
        lebelTotal9.configure(text="")
    elif (textList8 != ""):
        lebelList8.configure(text="")
        lebelPrice8.configure(text="")
        lebelTotal8.configure(text="")
    elif (textList7 != ""):
        lebelList7.configure(text="")
        lebelPrice7.configure(text="")
        lebelTotal7.configure(text="")
    elif (textList6 != ""):
        lebelList6.configure(text="")
        lebelPrice6.configure(text="")
        lebelTotal6.configure(text="")
    elif (textList5 != ""):
        lebelList5.configure(text="")
        lebelPrice5.configure(text="")
        lebelTotal5.configure(text="")
    elif (textList4 != ""):
        lebelList4.configure(text="")
        lebelPrice4.configure(text="")
        lebelTotal4.configure(text="")
    elif (textList3 != ""):
        lebelList3.configure(text="")
        lebelPrice3.configure(text="")
        lebelTotal3.configure(text="")
    elif (textList2 != ""):
        lebelList2.configure(text="")
        lebelPrice2.configure(text="")
        lebelTotal2.configure(text="")
    elif (textList1 != ""):
        lebelList1.configure(text="")
        lebelPrice1.configure(text="")
        lebelTotal1.configure(text="")
    lebelError.configure(text="")

# do function when click "Download" button (list the information in a text file named with the user-entered date information and download it).


def downloadClick():
    try:
        inputDay = int(enDay.get())
        inputMonth = int(enMonth.get())
        inputYear = enYear.get()
        if ((inputDay <= 31) & (inputDay >= 1) & (inputMonth <= 12) & (inputMonth >= 1)):
            if (inputMonth == 1):
                strMonth = "Jan"
            elif (inputMonth == 2):
                strMonth = "Fab"
            elif (inputMonth == 3):
                strMonth = "Mar"
            elif (inputMonth == 4):
                strMonth = "Apr"
            elif (inputMonth == 5):
                strMonth = "May"
            elif (inputMonth == 6):
                strMonth = "Jun"
            elif (inputMonth == 7):
                strMonth = "Jul"
            elif (inputMonth == 8):
                strMonth = "Aug"
            elif (inputMonth == 9):
                strMonth = "Sep"
            elif (inputMonth == 10):
                strMonth = "Oct"
            elif (inputMonth == 11):
                strMonth = "Nov"
            elif (inputMonth == 12):
                strMonth = "Dec"
            strDay = str(inputDay)
            strYear = "20"+inputYear
            thisDay = strDay+"-"+strMonth+"-"+strYear
            print(thisDay)
            print(type(thisDay))
            textList1 = lebelList1.cget("text")
            textList2 = lebelList2.cget("text")
            textList3 = lebelList3.cget("text")
            textList4 = lebelList4.cget("text")
            textList5 = lebelList5.cget("text")
            textList6 = lebelList6.cget("text")
            textList7 = lebelList7.cget("text")
            textList8 = lebelList8.cget("text")
            textList9 = lebelList9.cget("text")
            textPrice1 = lebelPrice1.cget("text")
            textPrice2 = lebelPrice2.cget("text")
            textPrice3 = lebelPrice3.cget("text")
            textPrice4 = lebelPrice4.cget("text")
            textPrice5 = lebelPrice5.cget("text")
            textPrice6 = lebelPrice6.cget("text")
            textPrice7 = lebelPrice7.cget("text")
            textPrice8 = lebelPrice8.cget("text")
            textPrice9 = lebelPrice9.cget("text")
            textTotal1 = lebelTotal1.cget("text")
            textTotal2 = lebelTotal2.cget("text")
            textTotal3 = lebelTotal3.cget("text")
            textTotal4 = lebelTotal4.cget("text")
            textTotal5 = lebelTotal5.cget("text")
            textTotal6 = lebelTotal6.cget("text")
            textTotal7 = lebelTotal7.cget("text")
            textTotal8 = lebelTotal8.cget("text")
            textTotal9 = lebelTotal9.cget("text")
            cFile = open("%s.txt" % thisDay, 'w')
            print(cFile)
            cFile.write("Revenue Accounts".center(140, " ")+"\n")
            cFile.write("".center(140, "-")+"\n")
            cFile.write("{:100s} {:20s} {:20s}\n".format(
                "List", "Price", "Total"))
            cFile.write("".center(140, "-")+"\n")
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList1, str(textPrice1), str(textTotal1)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList2, str(textPrice2), str(textTotal2)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList3, str(textPrice3), str(textTotal3)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList4, str(textPrice4), str(textTotal4)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList5, str(textPrice5), str(textTotal5)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList6, str(textPrice6), str(textTotal6)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList7, str(textPrice7), str(textTotal7)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList8, str(textPrice8), str(textTotal8)))
            cFile.write("{:100s} {:21s} {:10s}\n".format(
                textList9, str(textPrice9), str(textTotal9)))
            lebelError.configure(text="")
        else:
            lebelError.configure(
                text="day should be 1-31, month should be 1-12")

    except:
        lebelError.configure(text="Date should be only number")

# do function when click "Today" button (list the information in a text file named with the current date and download it).


def dateClick():
    thisTime = time.localtime()
    stTime = time.asctime(thisTime)
    timeList = list(stTime.split(" "))
    thisDay = timeList[2] + "-" + timeList[1] + "-" + timeList[4]
    textList1 = lebelList1.cget("text")
    textList2 = lebelList2.cget("text")
    textList3 = lebelList3.cget("text")
    textList4 = lebelList4.cget("text")
    textList5 = lebelList5.cget("text")
    textList6 = lebelList6.cget("text")
    textList7 = lebelList7.cget("text")
    textList8 = lebelList8.cget("text")
    textList9 = lebelList9.cget("text")
    textPrice1 = lebelPrice1.cget("text")
    textPrice2 = lebelPrice2.cget("text")
    textPrice3 = lebelPrice3.cget("text")
    textPrice4 = lebelPrice4.cget("text")
    textPrice5 = lebelPrice5.cget("text")
    textPrice6 = lebelPrice6.cget("text")
    textPrice7 = lebelPrice7.cget("text")
    textPrice8 = lebelPrice8.cget("text")
    textPrice9 = lebelPrice9.cget("text")
    textTotal1 = lebelTotal1.cget("text")
    textTotal2 = lebelTotal2.cget("text")
    textTotal3 = lebelTotal3.cget("text")
    textTotal4 = lebelTotal4.cget("text")
    textTotal5 = lebelTotal5.cget("text")
    textTotal6 = lebelTotal6.cget("text")
    textTotal7 = lebelTotal7.cget("text")
    textTotal8 = lebelTotal8.cget("text")
    textTotal9 = lebelTotal9.cget("text")
    cFile = open("%s.txt" % thisDay, 'w')
    print(cFile)
    cFile.write("Revenue Accounts".center(140, " ") + "\n")
    cFile.write("".center(140, "-") + "\n")
    cFile.write("{:100s} {:20s} {:20s}\n".format("List", "Price", "Total"))
    cFile.write("".center(140, "-") + "\n")
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList1, str(textPrice1), str(textTotal1)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList2, str(textPrice2), str(textTotal2)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList3, str(textPrice3), str(textTotal3)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList4, str(textPrice4), str(textTotal4)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList5, str(textPrice5), str(textTotal5)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList6, str(textPrice6), str(textTotal6)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList7, str(textPrice7), str(textTotal7)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList8, str(textPrice8), str(textTotal8)))
    cFile.write("{:100s} {:21s} {:10s}\n".format(
        textList9, str(textPrice9), str(textTotal9)))
    lebelError.configure(text="")


def enterClick(event):
    calculateClick()


def remove1(event):
    clearClick()


def exit(event):
    mainWindow.destroy()


mainWindow.bind("<Return>", enterClick)
mainWindow.bind("<Delete>", remove1)
mainWindow.bind("<Escape>", exit)

# GUI part
cashimg = ImageTk.PhotoImage(Image.open("money.png").resize((100, 100)))
img1 = ttk.Label(mainWindow, image=cashimg)
img1.place(x=705, y=5)

headLebel = ttk.Label(mainWindow, text="Cash Book", font=(
    "Helvetica 30 bold"), anchor=tk.CENTER)
headLebel.place(x=465, y=30, width=220)

mynameLebel = ttk.Label(mainWindow, text='"by Ize"', font=(
    "Helvetica 12 bold"), anchor=tk.CENTER)
mynameLebel.place(x=1100, y=30, width=220)


lebelList = ttk.Label(mainWindow, text="List", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList.place(x=200, y=100)

lebelPrice = ttk.Label(mainWindow, text="Price", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice.place(x=850, y=100, width=120)

lebelTotal = ttk.Label(mainWindow, text="Total", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal.place(x=1020, y=100, width=120)

en1 = ttk.Entry(mainWindow, font=("Helvetica 20 bold"), foreground='white')
en1.place(x=200, y=140, width=600, height=50)

en2 = ttk.Entry(mainWindow, font=("Helvetica 20 bold"), foreground='white')
en2.place(x=850, y=140, width=120, height=50)

calculateButton = ttk.Button(mainWindow, text="Calculate", cursor="hand2", style=(
    "success.Outline.TButton"), command=calculateClick)
calculateButton.place(x=1030, y=145, width=100, height=40)

calculateButton = ttk.Button(mainWindow, text="Delete 1 item", cursor="hand2", style=(
    "danger.TButton"), command=clearClick)
calculateButton.place(x=945, y=665, width=150, height=40)

calculateButton = ttk.Button(mainWindow, text="Clear All", cursor="hand2", style=(
    "danger.TButton"), command=clearAllClick)
calculateButton.place(x=1110, y=665, width=150, height=40)

lebelList1 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList1.place(x=200, y=210, width=600, height=50)

lebelPrice1 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice1.place(x=850, y=210, width=120, height=50)

lebelTotal1 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal1.place(x=1020, y=210, width=120, height=50)

lebelList2 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList2.place(x=200, y=260, width=600, height=50)

lebelPrice2 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice2.place(x=850, y=260, width=120, height=50)

lebelTotal2 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal2.place(x=1020, y=260, width=120, height=50)

lebelList3 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList3.place(x=200, y=310, width=600, height=50)

lebelPrice3 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice3.place(x=850, y=310, width=120, height=50)

lebelTotal3 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal3.place(x=1020, y=310, width=120, height=50)

lebelList4 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList4.place(x=200, y=360, width=600, height=50)

lebelPrice4 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice4.place(x=850, y=360, width=120, height=50)

lebelTotal4 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal4.place(x=1020, y=360, width=120, height=50)

lebelList5 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList5.place(x=200, y=410, width=600, height=50)

lebelPrice5 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice5.place(x=850, y=410, width=120, height=50)

lebelTotal5 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal5.place(x=1020, y=410, width=120, height=50)

lebelList6 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList6.place(x=200, y=460, width=600, height=50)

lebelPrice6 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice6.place(x=850, y=460, width=120, height=50)

lebelTotal6 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal6.place(x=1020, y=460, width=120, height=50)

lebelList7 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList7.place(x=200, y=510, width=600, height=50)

lebelPrice7 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice7.place(x=850, y=510, width=120, height=50)

lebelTotal7 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal7.place(x=1020, y=510, width=120, height=50)

lebelList8 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList8.place(x=200, y=560, width=600, height=50)

lebelPrice8 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice8.place(x=850, y=560, width=120, height=50)

lebelTotal8 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal8.place(x=1020, y=560, width=120, height=50)

lebelList9 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebelList9.place(x=200, y=610, width=600, height=50)

lebelPrice9 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelPrice9.place(x=850, y=610, width=120, height=50)

lebelTotal9 = ttk.Label(mainWindow, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebelTotal9.place(x=1020, y=610, width=120, height=50)

lebelDate = ttk.Label(mainWindow, text="Write Date",
                      font=("Helvetica 15 bold"), anchor=tk.CENTER)
lebelDate.place(x=20, y=630, width=180, height=40)

lebelDateSign = ttk.Label(mainWindow, text="/",
                          font=("Helvetica 28 bold"), anchor=tk.CENTER)
lebelDateSign.place(x=70, y=662, width=15, height=40)

lebelDateSign2 = ttk.Label(
    mainWindow, text="/", font=("Helvetica 28 bold"), anchor=tk.CENTER)
lebelDateSign2.place(x=134, y=662, width=15, height=40)

enDay = ttk.Entry(mainWindow, font=("Helvetica 20 bold"), foreground='white')
enDay.place(x=20, y=665, width=48, height=40)

enMonth = ttk.Entry(mainWindow, font=("Helvetica 20 bold"), foreground='white')
enMonth.place(x=86, y=665, width=47, height=40)

enYear = ttk.Entry(mainWindow, font=("Helvetica 20 bold"), foreground='white')
enYear.place(x=150, y=665, width=48, height=40)

dateButton = ttk.Button(mainWindow, text="Download", cursor="hand2", style=(
    "success.TButton"), command=downloadClick)
dateButton.place(x=220, y=665, width=160, height=40)

downloadButton = ttk.Button(mainWindow, text="Today", cursor="hand2", style=(
    "success.TButton"), command=dateClick)
downloadButton.place(x=395, y=665, width=160, height=40)

lebelError = ttk.Label(mainWindow, text="", font=(
    "Helvetica 13 bold"), anchor=tk.CENTER)
lebelError.place(x=575, y=665, width=350, height=40)

# style configuration part
style.configure('success.Outline.TButton', font=("Helvetica", 13, "bold"))
style.configure('danger.TButton', font=("Helvetica", 15, "bold"))
style.configure('success.TButton', font=("Helvetica", 12, "bold"))

# open window loop
mainWindow.mainloop()
