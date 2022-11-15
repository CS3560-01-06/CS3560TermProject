import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def forgetWidget(widget):
    widget.grid_forget()


def mainWindow(window, lList, bList, eList):
    w = 325
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(window, text="Hospital Login")
    label.grid(row=0, column=0)
    lList.append(label)
    empButton = Button(window, text="Employee Login", command=lambda a=window, b=lList, c=bList, d=eList: employeeLogin(a, b, c, d))
    empButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(empButton)
    patButton = Button(window, text="Patient Login", command=lambda a=window, b=lList, c=bList, d=eList: patientLogin(a, b, c, d))
    patButton.grid(row=2, column=0, sticky=N+S+E+W)
    bList.append(patButton)
    exitButton = Button(window, text="Exit Program", command=lambda x=window: exitProgram(x))
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
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

    user = username
    user.set("")
    password = passww
    password.set("")
    headerLabel = Label(window, text="Employee Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    lList.append(headerLabel)
    uLabel = Label(window, text="Username")
    uLabel.grid(row=1, column=0)
    lList.append(uLabel)
    uEntry = Entry(window, textvariable=user)
    uEntry.grid(row=1, column=1)
    uEntry.focus()
    eList.append(uEntry)
    pLabel = Label(window, text="Password")
    pLabel.grid(row=2, column=0)
    lList.append(pLabel)
    pEntry = Entry(window, textvariable=password, show='*')
    pEntry.grid(row=2, column=1, sticky=N+S+E+W)
    eList.append(pEntry)
    exitButton = Button(window, text="Cancel", command=lambda a=window, b=lList, c=bList, d=eList: exitLogin(a, b, c, d))
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)
    loginButton = Button(window, text="Login", command=lambda a=window, b=lList, c=bList, d=eList, e=user, f=password: employeeCheck(a, b, c, d, e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    bList.append(loginButton)

    window.bind('<Return>', lambda event: employeeCheck(window, lList, bList, eList, user, password))


def patientLogin(window, lList, bList, eList):
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

    user = username
    password = passww

    user.set("")
    password.set("")
    headerLabel = Label(window, text="Patient Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    lList.append(headerLabel)
    uLabel = Label(window, text="Username")
    uLabel.grid(row=1, column=0)
    lList.append(uLabel)
    uEntry = Entry(window, textvariable=user)
    uEntry.grid(row=1, column=1)
    uEntry.focus()
    eList.append(uEntry)
    pLabel = Label(window, text="Password")
    pLabel.grid(row=2, column=0)
    lList.append(pLabel)
    pEntry = Entry(window, textvariable=password, show='*')
    pEntry.grid(row=2, column=1, sticky=N+S+E+W)
    eList.append(pEntry)
    exitButton = Button(window, text="Cancel",
                        command=lambda a=window, b=lList, c=bList, d=eList: exitLogin(a, b, c, d))
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)
    loginButton = Button(window, text="Login", command=lambda a=window, b=lList, c=bList, d=eList, e=user, f=password: patientCheck(a, b, c, d, e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    bList.append(loginButton)

    window.bind('<Return>', lambda event: patientCheck(window, lList, bList, eList, user, password))


def patientCheck(window, lList, bList, eList, username, password):
    if username.get() != "patient" and password.get() != "password":
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(window, lList, bList, eList, 1)
    else:
        print("Patient View")
        patientView(window, lList, bList, eList)


def patientView(window, lList, bList, eList):
    w = 325
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

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()
    name = "Patient"

    patientLabel = Label(window, text="Welcome, " + name)
    patientLabel.grid(row=0, column=0)
    lList.append(patientLabel)
    maButton = Button(window, text="Make Appointment")
    maButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(maButton)
    vaButton = Button(window, text="View Appointment")
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(vaButton)
    logoutButton = Button(window, text="Logout", command=lambda a=window, b=lList, c=bList, d=eList: userLogout(a, b, c, d))
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)


def employeeCheck(window, lList, bList, eList, username, password):
    if username.get() != "clerk" and password.get() != "password" or username.get() != "doctor" and password.get() != "password":
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(window, lList, bList, eList, 0)
    elif username.get() == "doctor" and password.get() == "password":
        print("Doctor View")
        doctorView(window, lList, bList, eList)
    elif username.get() == "clerk" and password.get() == "password":
        print("Clerk View")
        clerkView(window, lList, bList, eList)


def doctorView(window, lList, bList, eList):
    w = 325
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

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()
    name = "Doctor"

    doctorLabel = Label(window, text="Welcome, " + name)
    doctorLabel.grid(row=0, column=0)
    lList.append(doctorLabel)
    vaButton = Button(window, text="View Appointments")
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0), ipadx=100)
    bList.append(vaButton)
    logoutButton = Button(window, text="Logout", command=lambda a=window, b=lList, c=bList, d=eList: userLogout(a, b, c, d))
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)

def clerkView(window, lList, bList, eList):
    w = 400
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

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()
    name = "Clerk"

    clerkLabel = Label(window, text="Welcome, " + name)
    clerkLabel.grid(row=0, column=0)
    lList.append(clerkLabel)
    maButton = Button(window, text="Make Appointment for Patient")
    maButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(maButton)
    vaButton = Button(window, text="View Appointment for Patient")
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(vaButton)
    logoutButton = Button(window, text="Logout", command=lambda a=window, b=lList, c=bList, d=eList: userLogout(a, b, c, d))
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)


def exitProgram(window):
    logoutMSG = tkinter.messagebox.askquestion('Close?', 'Do you want to close the program?')
    if logoutMSG == 'yes':
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

def logout(window, lList, bList, eList, num):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()

    if num == 0:
        employeeLogin(window, lList, bList, eList)
    else:
        patientLogin(window, lList, bList, eList)

def userLogout(window, lList, bList, eList):
    logoutMSG = tkinter.messagebox.askquestion('Logout?', 'Do you wish to logout?')

    if logoutMSG == 'yes':
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
    global username
    global passww
    username = StringVar()
    passww = StringVar()
    root.title("Hospital Scheduling System")
    mainWindow(root, labelList, buttonList, entryList)

    root.mainloop()


if __name__ == "__main__":
    main()
