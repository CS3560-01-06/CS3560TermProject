import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def forgetWidget(widget):
    widget.grid_forget()


def mainWindow():
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
    empButton = Button(window, text="Employee Login", command=employeeLogin)
    empButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(empButton)
    patButton = Button(window, text="Patient Login", command=patientLogin)
    patButton.grid(row=2, column=0, sticky=N+S+E+W)
    bList.append(patButton)
    exitButton = Button(window, text="Exit Program", command=exitProgram)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)


def employeeLogin():
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
    exitButton = Button(window, text="Cancel", command=exitLogin)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)
    loginButton = Button(window, text="Login", command=lambda e=user, f=password: employeeCheck(e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    bList.append(loginButton)

    window.bind('<Return>', lambda event: employeeCheck(user, password))


def patientLogin():
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
    exitButton = Button(window, text="Cancel", command=exitLogin)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)
    loginButton = Button(window, text="Login", command=lambda e=user, f=password: patientCheck(e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    bList.append(loginButton)

    window.bind('<Return>', lambda event: patientCheck(user, password))


def patientCheck(username, password):
    if username.get() != "patient" and password.get() != "password":
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(1)
    else:
        print("Patient View")
        patientView()


def patientView():
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
    logoutButton = Button(window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)


def employeeCheck(username, password):
    if username.get() != "clerk" and password.get() != "password" or username.get() != "doctor" and password.get() != "password":
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(0)
    elif username.get() == "doctor" and password.get() == "password":
        print("Doctor View")
        doctorView()
    elif username.get() == "clerk" and password.get() == "password":
        print("Clerk View")
        clerkView()


def doctorView():
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
    logoutButton = Button(window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)

def clerkView():
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
    logoutButton = Button(window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)

def makeAppointment():
    print()
def exitProgram():
    logoutMSG = tkinter.messagebox.askquestion('Close?', 'Do you want to close the program?')
    if logoutMSG == 'yes':
        window.destroy()


def exitLogin():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()

    mainWindow()

def logout(num):
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
        employeeLogin()
    else:
        patientLogin()

def userLogout():
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

        mainWindow()

def main():
    global window
    window = Tk()
    global lList
    lList = []
    global bList
    bList = []
    global eList
    eList = []
    global username
    global passww
    username = StringVar()
    passww = StringVar()
    window.title("Hospital Scheduling System")
    mainWindow()

    window.mainloop()


if __name__ == "__main__":
    main()
