import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def forgetWidget(widget):
    widget.grid_forget()


def mainWindow(window, lList, bList, eList):
    w = 292
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(window, text="Hospital Login")
    label.grid(row=0, column=1)
    lList.append(label)
    empButton = Button(window, text="Employee Login", command=lambda a=window, b=lList, c=bList, d=eList: employeeLogin(a, b, c, d))
    empButton.grid(row=1, column=0, padx=(5, 0))
    bList.append(empButton)
    patButton = Button(window, text="Patient Login", command=patientLogin)
    patButton.grid(row=1, column=3)
    bList.append(patButton)
    exitButton = Button(window, text="Exit Program", command=lambda x=window: exitProgram(x))
    exitButton.grid(row=2, column=1)
    bList.append(exitButton)


def employeeLogin(window, lList, bList, eList):
    w = 225
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    lList.clear()
    bList.clear()

    user = StringVar()
    user.set("")
    password = StringVar()
    password.set("")

    headerLabel = Label(window, text="Employee Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    lList.append(headerLabel)
    uLabel = Label(window, text="Username")
    uLabel.grid(row=1, column=0)
    lList.append(uLabel)
    uEntry = Entry(window, textvariable=user)
    uEntry.grid(row=1, column=1)
    eList.append(uEntry)
    pLabel = Label(window, text="Password")
    pLabel.grid(row=2, column=0)
    lList.append(pLabel)
    pEntry = Entry(window, textvariable=password)
    pEntry.grid(row=2, column=1)
    eList.append(pEntry)
    exitButton = Button(window, text="Cancel", command=lambda a=window, b=lList, c=bList, d=eList: exitLogin(a, b, c, d))
    exitButton.grid(row=3, column=0)
    bList.append(exitButton)
    loginButton = Button(window, text="Login")
    loginButton.grid(row=3, column=1)
    bList.append(loginButton)


def patientLogin():
    print("Patient Login")


def exitProgram(window):
    print("Exiting Program...")
    window.destroy()


def exitLogin(window, lList, bList, eList):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()

    mainWindow(window, lList, bList, eList)

def main():
    root = Tk()
    labelList = []
    buttonList = []
    entryList = []

    root.title("Hospital Scheduling System")
    mainWindow(root, labelList, buttonList, entryList)

    root.mainloop()


if __name__ == "__main__":
    main()
