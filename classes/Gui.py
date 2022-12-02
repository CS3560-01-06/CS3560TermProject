import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date, timedelta, datetime
import textwrap
from classes import settings


def wrap(string, length=40):
    return '\n'.join(textwrap.wrap(string, length))


def forgetWidget(widget):
    widget.grid_forget()


def mainWindow():
    settings.window.title("Hospital Scheduling System")

    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    style = ttk.Style()
    style.configure('Treeview', rowheight=50)

    label = Label(settings.window, text="Hospital Login")
    label.grid(row=0, column=0)
    settings.lList.append(label)
    empButton = Button(settings.window, text="Employee Login", command=employeeLogin)
    empButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    settings.bList.append(empButton)
    patButton = Button(settings.window, text="Patient Login", command=patientLogin)
    patButton.grid(row=2, column=0, sticky=N+S+E+W)
    settings.bList.append(patButton)
    exitButton = Button(settings.window, text="Exit Program", command=exitProgram)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    settings.bList.append(exitButton)

    settings.updateLists()
    settings.window.mainloop()



def employeeLogin():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    settings.lList.clear()
    settings.bList.clear()

    user = settings.username
    user.set("")
    password = settings.passww
    password.set("")
    headerLabel = Label(settings.window, text="Employee Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    settings.lList.append(headerLabel)
    uLabel = Label(settings.window, text="Username")
    uLabel.grid(row=1, column=0)
    settings.lList.append(uLabel)
    uEntry = Entry(settings.window, textvariable=user)
    uEntry.grid(row=1, column=1)
    uEntry.focus()
    settings.eList.append(uEntry)
    pLabel = Label(settings.window, text="Password")
    pLabel.grid(row=2, column=0)
    settings.lList.append(pLabel)
    pEntry = Entry(settings.window, textvariable=password, show='*')
    pEntry.grid(row=2, column=1, sticky=N+S+E+W)
    settings.eList.append(pEntry)
    exitButton = Button(settings.window, text="Cancel", command=exitLogin)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    settings.bList.append(exitButton)
    loginButton = Button(settings.window, text="Login", command=lambda e=user, f=password: employeeCheck(e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    settings.bList.append(loginButton)

    settings.window.bind('<Return>', lambda event: employeeCheck(user, password))


def patientLogin():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    settings.lList.clear()
    settings.bList.clear()

    user = settings.username
    password = settings.passww

    user.set("")
    password.set("")
    headerLabel = Label(settings.window, text="Patient Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    settings.lList.append(headerLabel)
    uLabel = Label(settings.window, text="Username/Email Address")
    uLabel.grid(row=1, column=0)
    settings.lList.append(uLabel)
    uEntry = Entry(settings.window, textvariable=user)
    uEntry.grid(row=1, column=1)
    uEntry.focus()
    settings.eList.append(uEntry)
    pLabel = Label(settings.window, text="Password")
    pLabel.grid(row=2, column=0)
    settings.lList.append(pLabel)
    pEntry = Entry(settings.window, textvariable=password, show='*')
    pEntry.grid(row=2, column=1, sticky=N+S+E+W)
    settings.eList.append(pEntry)
    exitButton = Button(settings.window, text="Cancel", command=exitLogin)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    settings.bList.append(exitButton)
    loginButton = Button(settings.window, text="Login", command=lambda e=user, f=password: patientCheck(e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    settings.bList.append(loginButton)

    settings.window.bind('<Return>', lambda event: patientCheck(user, password))


def patientCheck(username, password):
    count = 0
    for pat in range(0, len(settings.patient)):
        if str(settings.patient[pat].getUsername()) == username.get() and str(settings.patient[pat].getPassword()) == password.get():
            count = count + 1
            global currentPatient
            currentPatient = settings.patient[pat]

    if count == 0:
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(1)
    else:
        print("Patient View")
        patientView()


def patientView():
    settings.updateLists()

    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    name = currentPatient.getName()

    patientLabel = Label(settings.window, text="Welcome, " + name)
    patientLabel.grid(row=0, column=0)
    settings.lList.append(patientLabel)
    maButton = Button(settings.window, text="Make Appointment", command=makeAppointment)
    maButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    settings.bList.append(maButton)
    vaButton = Button(settings.window, text="View Appointment", command=viewAppointments)
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0))
    settings.bList.append(vaButton)
    logoutButton = Button(settings.window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    settings.bList.append(logoutButton)

    settings.window.unbind_all('<Return>')

def makeAppointment():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    settings.lList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headLabel = Label(settings.window, text="Make an Appointment")
    headLabel.grid(row=0, column=0)
    settings.lList.append(headLabel)

    searchDocButton = Button(settings.window, text="Search Doctors", command=searchDoctor)
    searchDocButton.grid(row=1, column=0)
    settings.bList.append(searchDocButton)

    searchSpecButton = Button(settings.window, text="Search Specialty", command=searchSpecialty)
    searchSpecButton.grid(row=2, column=0)
    settings.bList.append(searchSpecButton)

    cancelButton = Button(settings.window, text="Cancel", command=patientView)
    cancelButton.grid(row=3, column=0)
    settings.bList.append(cancelButton)


def searchDoctor():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.idList.clear()

    headerLabel = Label(settings.window, text="Search for Doctor")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Name", "Specialty")
    doctorTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    doctorTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    doctorTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    for doctor in settings.doctors:
        settings.idList.append(doctor.getDoctorID())
        doctorTree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))
    doctorTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(doctorTree)

    searchLabel = Label(settings.window, text="Search Name")
    searchLabel.grid(row=2, column=0)
    settings.lList.append(searchLabel)
    global search
    search = StringVar()
    search.set("")

    searchEntry = Entry(settings.window, textvariable=search)
    searchEntry.grid(row=2, column=1)
    settings.eList.append(searchEntry)

    updateButton = Button(settings.window, text="Update Search", command=lambda x=doctorTree, y=search: searchDoctorUpdate(x, y))
    updateButton.grid(row=2, column=2)
    settings.bList.append(updateButton)

    cancelButton = Button(settings.window, text="Cancel", command=patientView)
    cancelButton.grid(row=3, column=0)
    settings.bList.append(cancelButton)

    confirmButton = Button(settings.window, text="Confirm", command=lambda x=doctorTree: confirmDoctor(x))
    confirmButton.grid(row=3, column=1)
    settings.bList.append(confirmButton)


def searchDoctorUpdate(tree, search):
    settings.idList.clear()
    count = 0
    for item in tree.get_children():
        tree.delete(item)

    for doctor in settings.doctors:
        if search.get() in str(doctor.getName()) :
            count = count + 1
            settings.idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))

    if count == 0:
        for doctor in settings.doctors:
            settings.idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))


def searchSpecialty():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.idList.clear()

    headerLabel = Label(settings.window, text="Search for Specialty")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Specialty", "Name")
    specTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    specTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    specTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    for doctor in settings.doctors:
        settings.idList.append(doctor.getDoctorID())
        specTree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))
    specTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(specTree)

    searchLabel = Label(settings.window, text="Search Specialty")
    searchLabel.grid(row=2, column=0)
    settings.lList.append(searchLabel)

    global search
    search = StringVar()
    search.set("")

    searchEntry = Entry(settings.window, textvariable=search)
    searchEntry.grid(row=2, column=1)
    settings.eList.append(searchEntry)

    updateButton = Button(settings.window, text="Update Search", command=lambda x=specTree, y=search: searchSpecUpdate(x, y))
    updateButton.grid(row=2, column=2)
    settings.bList.append(updateButton)

    cancelButton = Button(settings.window, text="Cancel", command=patientView)
    cancelButton.grid(row=3, column=0)
    settings.bList.append(cancelButton)

    confirmButton = Button(settings.window, text="Confirm", command=lambda x=specTree: confirmSpecialty(x))
    confirmButton.grid(row=3, column=1)
    settings.bList.append(confirmButton)

def searchSpecUpdate(tree, search):
    settings.idList.clear()
    count = 0
    for item in tree.get_children():
        tree.delete(item)

    for doctor in settings.doctors:
        if search.get() in str(doctor.getSpecialty()):
            count = count + 1
            settings.idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))

    if count == 0:
        for doctor in settings.doctors:
            settings.idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))

def confirmDoctor(tree):
    try:
        temp = tree.selection()[0]
        for doctor in settings.doctors:
            for id in settings.idList:
                if doctor.getDoctorID() == id and tree.item(temp)['values'][0] == str(doctor.getName()) and tree.item(temp)['values'][1] == str(doctor.getSpecialty()):
                    global currentDoctor
                    currentDoctor = doctor
                    showDCalendar()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")


def showDCalendar():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.cList.clear()
    dmax = date(2022, 11, 15) + timedelta(days=365)
    cal = Calendar(settings.window, selectmode="day", mindate=date.today() + timedelta(days=1), maxdate=dmax, date_pattern="yyyy-mm-dd", disableddaybackground="grey", locale="en_US")
    cal.grid(row=0, column=0)
    settings.cList.append(cal)

    dateConfirm = Button(settings.window, text="Confirm Date", command=confirmDate)
    dateConfirm.grid(row=1, column=1)
    settings.bList.append(dateConfirm)

    cancelButton = Button(settings.window, text="Cancel", command=lambda x=1: calCancel(x))
    cancelButton.grid(row=1, column=0)
    settings.bList.append(cancelButton)

def calCancel(num):
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.cList.clear()

    if num != 0:
        searchSpecialty()
    else:
        searchDoctor()

def confirmDate():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    count = 0
    for cal in settings.calendars:
        if str(settings.cList[0].get_date()) == str(cal.getDate()):
            for avail in settings.availability:
                if str(avail.getIDCalendar()) == str(cal.getIDCalendar()) and str(currentDoctor.getDoctorID()) == str(avail.getIDDoctor()) and str(avail.getAvail()) != str(0):
                    print(str(avail.getIDAvail()) + " " + str(cal.getTime()) + " " + str(avail.getAvail()))
                    dateConfirm = Button(settings.window, text="Confirm Time: " + str(cal.getTime()), command=lambda x=cal, y=avail: finalizeAppointment(x, y))
                    dateConfirm.grid(row=count, column=0)
                    settings.bList.append(dateConfirm)
                    count = count + 1
    cancelButton = Button(settings.window, text="Cancel", command=showDCalendar)
    cancelButton.grid(row=count, column=0)
    settings.bList.append(cancelButton)

def finalizeAppointment(cal, avail):
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    global currentDate
    currentDate = cal

    global currentAvail
    currentAvail = avail

    currentAvail.setAvail(0)

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    strOp = [
        "New Appointment",
        "Follow-up"
    ]
    str1 = StringVar()
    str1.set(strOp[0])
    dateLabel = Label(settings.window, text=str(currentDate.getDate()))
    dateLabel.grid(row=0, column=0)
    settings.lList.append(dateLabel)

    timeLabel = Label(settings.window, text=str(currentDate.getTime()))
    timeLabel.grid(row=1, column=0)
    settings.lList.append(timeLabel)

    doctorLabel = Label(settings.window, text=str(currentDoctor.getName()) + "\nSpecialty: " + str(currentDoctor.getSpecialty()))
    doctorLabel.grid(row=2, column=0)
    settings.lList.append(doctorLabel)

    reasonDrop = OptionMenu(settings.window, str1, *strOp)
    reasonDrop.grid(row=3, column=0)
    global currentDrop
    currentDrop = reasonDrop

    textbox = Text(settings.window, height=5, width=52)
    textbox.grid(row=4, column=0)
    global currentText
    currentText = textbox

    cancel = Button(settings.window, text="Cancel", command=confirmDate)
    cancel.grid(row=5, column=0)
    settings.bList.append(cancel)

    confirm = Button(settings.window, text="Confirm", command=lambda x=str1, y=textbox: showConfirm(x, y))
    confirm.grid(row=5, column=1)
    settings.bList.append(confirm)

def showConfirm(drop, text):
    global currentDrop
    global currentText

    try:
        for i in range(0, len(settings.bList)):
            forgetWidget(settings.bList[i])

        for i in range(0, len(settings.lList)):
            forgetWidget(settings.lList[i])

        forgetWidget(currentDrop)
        forgetWidget(currentText)

        settings.connectSQL()
        sql = "INSERT IGNORE INTO Appointment (idCalendar, idDoctor, idPatient, appointmentType, reason) VALUES (%s, %s, %s, %s, %s)"
        val = (currentDate.getIDCalendar(), currentDoctor.getDoctorID(), currentPatient.getPatientID(), drop.get(), text.get("1.0", "end-1c"))
        cursor = settings.connector.cursor()
        cursor.execute(sql, val)

        settings.connector.commit()

        sql = "UPDATE Availability SET isAvailable = %s WHERE idAvailability = %s"
        val = (currentAvail.getAvail(), currentAvail.getIDAvail())
        cursor.execute(sql, val)
        settings.connector.commit()

        cursor.close()
        settings.closeSQL()

        patientView()
    except len(currentText.get("1.0", "end-1c")) > 99:
        tkinter.messagebox.showerror("Error", "Max Length 100 characters")


def confirmSpecialty(tree):
    try:
        temp = tree.selection()[0]
        for doctor in settings.doctors:
            for id in settings.idList:
                if doctor.getDoctorID() == id and tree.item(temp)['values'][1] == str(doctor.getName()) and tree.item(temp)['values'][0] == str(doctor.getSpecialty()):
                    global currentDoctor
                    currentDoctor = doctor
                    showSCalendar()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")

def showSCalendar():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.cList.clear()
    dmax = date.today() + timedelta(days=365)
    cal = Calendar(settings.window, selectmode="day", mindate=date.today() + timedelta(days=1), maxdate=dmax, date_pattern="yyyy-mm-dd", disableddaybackground="grey", locale="en_US")
    cal.grid(row=0, column=0)
    settings.cList.append(cal)

    dateConfirm = Button(settings.window, text="Confirm Date", command=confirmSDate)
    dateConfirm.grid(row=1, column=1)
    settings.bList.append(dateConfirm)

    cancelButton = Button(settings.window, text="Cancel", command=lambda x=0: calCancel(x))
    cancelButton.grid(row=1, column=0)
    settings.bList.append(cancelButton)

def confirmSDate():
    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    count = 0
    for cal in settings.calendars:
        if str(settings.cList[0].get_date()) == str(cal.getDate()):
            for avail in settings.availability:
                if str(avail.getIDCalendar()) == str(cal.getIDCalendar()) and str(currentDoctor.getDoctorID()) == str(avail.getIDDoctor()) and str(avail.getAvail()) != str(0):
                    print(str(avail.getIDAvail()) + " " + str(cal.getTime()) + " " + str(avail.getAvail()))
                    dateConfirm = Button(settings.window, text="Confirm Time: " + str(cal.getTime()), command=lambda x=cal, y=avail: finalizeSAppointment(x, y))
                    dateConfirm.grid(row=count, column=0)
                    settings.bList.append(dateConfirm)
                    count = count + 1
    cancelButton = Button(settings.window, text="Cancel", command=showSCalendar)
    cancelButton.grid(row=count, column=0)
    settings.bList.append(cancelButton)

def finalizeSAppointment(cal, avail):
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    global currentDate
    currentDate = cal

    global currentAvail
    currentAvail = avail

    currentAvail.setAvail(0)

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    strOp = [
        "New Appointment",
        "Follow-up"
    ]
    str1 = StringVar()
    str1.set(strOp[0])
    dateLabel = Label(settings.window, text=str(currentDate.getDate()))
    dateLabel.grid(row=0, column=0)
    settings.lList.append(dateLabel)

    timeLabel = Label(settings.window, text=str(currentDate.getTime()))
    timeLabel.grid(row=1, column=0)
    settings.lList.append(timeLabel)

    doctorLabel = Label(settings.window, text=str(currentDoctor.getName()) + "\nSpecialty: " + str(currentDoctor.getSpecialty()))
    doctorLabel.grid(row=2, column=0)
    settings.lList.append(doctorLabel)

    reasonDrop = OptionMenu(settings.window, str1, *strOp)
    reasonDrop.grid(row=3, column=0)
    global currentDrop
    currentDrop = reasonDrop

    textbox = Text(settings.window, height=5, width=52)
    textbox.grid(row=4, column=0)
    global currentText
    currentText = textbox

    cancel = Button(settings.window, text="Cancel", command=confirmSDate)
    cancel.grid(row=5, column=0)
    settings.bList.append(cancel)

    confirm = Button(settings.window, text="Confirm", command=lambda x=str1, y=textbox: showConfirm(x, y))
    confirm.grid(row=5, column=1)
    settings.bList.append(confirm)


def viewAppointments():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headerLabel = Label(settings.window, text="View Appointments")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)
    cols = ("Appointment Number", "Date", "Time", "Doctor Name", "Specialty", "Appointment Type", "Reason")
    appointTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Appointment Number", text="Appointment Number", anchor=tkinter.CENTER)
    appointTree.column("Appointment Number", minwidth=150, width=150)
    appointTree.heading("Date", text="Date", anchor=tkinter.CENTER)
    appointTree.column("Date", minwidth=75, width=75)
    appointTree.heading("Time", text="Time", anchor=tkinter.CENTER)
    appointTree.column("Time", minwidth=75, width=75)
    appointTree.heading("Doctor Name", text="Name", anchor=tkinter.CENTER)
    appointTree.column("Doctor Name", minwidth=150, width=150)
    appointTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    appointTree.column("Specialty", minwidth=100, width=100)
    appointTree.heading("Appointment Type", text="Appointment Type", anchor=tkinter.CENTER)
    appointTree.column("Appointment Type", minwidth=150, width=150)
    appointTree.heading("Reason", text="Reason", anchor=tkinter.CENTER)
    appointTree.column("Reason", minwidth=200, width=200)
    for appointment in settings.appointments:
        for cal in settings.calendars:
            for doc in settings.doctors:
                if str(appointment.getIDCalendar()) == str(cal.getIDCalendar()) and str(appointment.getIDDoctor()) == str(doc.getDoctorID()) and str(appointment.getPatientID()) == str(currentPatient.getPatientID()):
                    appointTree.insert("", tkinter.END, values=(str(appointment.getIDAppointment()), (cal.getDate()), str(cal.getTime()), str(doc.getName()), str(doc.getSpecialty()), str(appointment.getType()), wrap(str(appointment.getReason()))))
    appointTree.grid(row=1, column=0)
    settings.tList.append(appointTree)

    cancelButton = Button(settings.window, text="Cancel", command=patientView)
    cancelButton.grid(row=2, column=0)
    settings.bList.append(cancelButton)

    editButton = Button(settings.window, text="Remove Appointment", command=lambda x=appointTree, y=0: removeAppointment(x, y))
    editButton.grid(row=2, column=1)
    settings.bList.append(editButton)


def removeAppointment(tree, num):
    try:
        temp = tree.selection()[0]

        try:
            answer = tkinter.messagebox.askyesno("Confirm?", "Remove the selected appointment?")
            global currentAvail
            global currentAppointment
            if answer:
                for appointment in settings.appointments:
                    if str(tree.item(temp)['values'][0]) == str(appointment.getIDAppointment()):
                        currentAppointment = appointment

                for avail in settings.availability:
                    if str(currentAppointment.getIDCalendar()) == str(avail.getIDCalendar()) and str(
                            currentAppointment.getIDDoctor()) == str(avail.getIDDoctor()):
                                currentAvail = avail
                                currentAvail.setAvail(1)

                settings.connectSQL()
                cursor = settings.connector.cursor()

                sql = "UPDATE Availability SET isAvailable = %s WHERE idAvailability = %s"
                val = (currentAvail.getAvail(), currentAvail.getIDAvail())
                cursor.execute(sql, val)
                settings.connector.commit()

                sql = "DELETE FROM Appointment WHERE idDoctor = %s and idCalendar = %s and idPatient = %s"
                val = (currentAppointment.getIDDoctor(), currentAppointment.getIDCalendar(), currentAppointment.getPatientID())
                cursor.execute(sql, val)
                settings.connector.commit()

                cursor.close()
                settings.closeSQL()

                if num == 0:
                    patientView()
                elif num == 1:
                    doctorView()
                else:
                    clerkView()
        except datetime.strptime(str(tree.item(temp)['values'][1]), '%Y-%m-%m').date() < date.today():
            tkinter.messagebox.showerror("Error", "Appointment Already Passed")
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")

def employeeCheck(username, password):
    count = 0
    for doctor in settings.doctors:
        if str(doctor.getUsername()) == username.get() and str(doctor.getPassword()) == password.get() or str(doctor.getEmail()) == username.get() and str(doctor.getPassword()) == password.get():
            count = count + 1
            global currentDoctor
            currentDoctor = doctor
            doctorView()
            break

    if count == 0:
        for employee in settings.employees:
            if employee.getUsername() == username.get() and employee.getPassword() == password.get() or employee.getEmail() == username.get() and employee.getPassword() == password.get():
                count = count + 1
                global currentEmployee
                currentEmployee = employee
                clerkView()
                break

    if count == 0:
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(0)


def doctorView():
    settings.window.unbind_all('<Return>')
    settings.updateLists()

    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    name = currentDoctor.getName()

    doctorLabel = Label(settings.window, text="Welcome, " + name)
    doctorLabel.grid(row=0, column=0)
    settings.lList.append(doctorLabel)
    vaButton = Button(settings.window, text="View Appointments", command=viewDoctorAppointments)
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0), ipadx=100)
    settings.bList.append(vaButton)
    logoutButton = Button(settings.window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    settings.bList.append(logoutButton)


def viewDoctorAppointments():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headerLabel = Label(settings.window, text="View Appointments")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Appointment Number", "Date", "Time", "Patient Name", "Appointment Type", "Reason")
    appointTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Appointment Number", text="Appointment Number", anchor=tkinter.CENTER)
    appointTree.column("Appointment Number", minwidth=150, width=150)
    appointTree.heading("Date", text="Date", anchor=tkinter.CENTER)
    appointTree.column("Date", minwidth=75, width=75)
    appointTree.heading("Time", text="Time", anchor=tkinter.CENTER)
    appointTree.column("Time", minwidth=75, width=75)
    appointTree.heading("Patient Name", text="Patient Name", anchor=tkinter.CENTER)
    appointTree.column("Patient Name", minwidth=150, width=150)
    appointTree.heading("Appointment Type", text="Appointment Type", anchor=tkinter.CENTER)
    appointTree.column("Appointment Type", minwidth=150, width=150)
    appointTree.heading("Reason", text="Reason", anchor=tkinter.CENTER)
    appointTree.column("Reason", minwidth=200, width=200)
    for appointment in settings.appointments:
        for cal in settings.calendars:
            for pat in settings.patient:
                if str(appointment.getIDCalendar()) == str(cal.getIDCalendar()) and str(appointment.getIDDoctor()) == str(currentDoctor.getDoctorID()) and str(appointment.getPatientID()) == str(pat.getPatientID()):
                    appointTree.insert("", tkinter.END, values=(str(appointment.getIDAppointment()), (cal.getDate()), str(cal.getTime()), str(pat.getName()), str(appointment.getType()), wrap(str(appointment.getReason()))))
    appointTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(appointTree)

    cancelButton = Button(settings.window, text="Cancel", command=doctorView)
    cancelButton.grid(row=2, column=0)
    settings.bList.append(cancelButton)

    editButton = Button(settings.window, text="Remove Appointment", command=lambda x=appointTree, y=1: removeAppointment(x, y))
    editButton.grid(row=2, column=1)
    settings.bList.append(editButton)


def clerkView():
    settings.window.unbind_all('<Return>')
    settings.updateLists()
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    name = currentEmployee.getName()

    clerkLabel = Label(settings.window, text="Welcome, " + name)
    clerkLabel.grid(row=0, column=0)
    settings.lList.append(clerkLabel)
    maButton = Button(settings.window, text="Make Appointment for Patient", command=selectMAPatient)
    maButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    settings.bList.append(maButton)
    vaButton = Button(settings.window, text="View Appointment for Patient", command=selectVAPatient)
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0))
    settings.bList.append(vaButton)
    logoutButton = Button(settings.window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    settings.bList.append(logoutButton)


def selectMAPatient():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headerLabel = Label(settings.window, text="Select Patient")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Patient ID", "Name")
    appointTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Patient ID", text="Patient ID", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    for pat in settings.patient:
        appointTree.insert("", tkinter.END, values=(pat.getPatientID(), pat.getName()))
    appointTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(appointTree)

    cancelButton = Button(settings.window, text="Cancel", command=clerkView)
    cancelButton.grid(row=2, column=0)
    settings.bList.append(cancelButton)

    confirmButton = Button(settings.window, text="Confirm Patient", command=lambda x=appointTree: getMAPatient(x))
    confirmButton.grid(row=2, column=1)
    settings.bList.append(confirmButton)


def getMAPatient(tree):
    try:
        temp = tree.selection()[0]
        for pat in settings.patient:
            if str(pat.getPatientID()) == str(tree.item(temp)['values'][0]):
                global currentPatient
                currentPatient = pat
        makePatientAppointment()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")

def selectVAPatient():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headerLabel = Label(settings.window, text="Select Patient")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Patient ID", "Name")
    appointTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Patient ID", text="Patient ID", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    for pat in settings.patient:
        appointTree.insert("", tkinter.END, values=(pat.getPatientID(), pat.getName()))
    appointTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(appointTree)

    cancelButton = Button(settings.window, text="Cancel", command=clerkView)
    cancelButton.grid(row=2, column=0)
    settings.bList.append(cancelButton)

    confirmButton = Button(settings.window, text="Confirm Patient", command=lambda x=appointTree: getVAPatient(x))
    confirmButton.grid(row=2, column=1)
    settings.bList.append(confirmButton)

def getVAPatient(tree):
    try:
        temp = tree.selection()[0]
        for pat in settings.patient:
            if str(pat.getPatientID()) == str(tree.item(temp)['values'][0]):
                global currentPatient
                currentPatient = pat
        viewPatientAppointments()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")

def makePatientAppointment():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headLabel = Label(settings.window, text="Make an Appointment for " + str(currentPatient.getName()))
    headLabel.grid(row=0, column=0)
    settings.lList.append(headLabel)

    searchDocButton = Button(settings.window, text="Search Doctors", command=searchPatientDoctor)
    searchDocButton.grid(row=1, column=0)
    settings.bList.append(searchDocButton)

    searchSpecButton = Button(settings.window, text="Search Specialty", command=searchPatientSpecialty)
    searchSpecButton.grid(row=2, column=0)
    settings.bList.append(searchSpecButton)

    cancelButton = Button(settings.window, text="Cancel", command=selectMAPatient)
    cancelButton.grid(row=3, column=0)
    settings.bList.append(cancelButton)


def searchPatientDoctor():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.idList.clear()

    headerLabel = Label(settings.window, text="Search for Doctor")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Name", "Specialty")
    doctorTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    doctorTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    doctorTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    for doctor in settings.doctors:
        settings.idList.append(doctor.getDoctorID())
        doctorTree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))
    doctorTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(doctorTree)

    searchLabel = Label(settings.window, text="Search Name")
    searchLabel.grid(row=2, column=0)
    settings.lList.append(searchLabel)
    global search
    search = StringVar()
    search.set("")

    searchEntry = Entry(settings.window, textvariable=search)
    searchEntry.grid(row=2, column=1)
    settings.eList.append(searchEntry)

    updateButton = Button(settings.window, text="Update Search", command=lambda x=doctorTree, y=search: searchDoctorUpdate(x, y))
    updateButton.grid(row=2, column=2)
    settings.bList.append(updateButton)

    cancelButton = Button(settings.window, text="Cancel", command=clerkView)
    cancelButton.grid(row=3, column=0)
    settings.bList.append(cancelButton)

    confirmButton = Button(settings.window, text="Confirm", command=lambda x=doctorTree: confirmCDoctor(x))
    confirmButton.grid(row=3, column=1)
    settings.bList.append(confirmButton)


def confirmCDoctor(tree):
    try:
        temp = tree.selection()[0]
        for doctor in settings.doctors:
            for id in settings.idList:
                if doctor.getDoctorID() == id and tree.item(temp)['values'][0] == str(doctor.getName()) and tree.item(temp)['values'][1] == str(doctor.getSpecialty()):
                    global currentDoctor
                    currentDoctor = doctor
                    showDCCalendar()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")


def showDCCalendar():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.cList.clear()
    dmax = date.today() + timedelta(days=365)
    cal = Calendar(settings.window, selectmode="day", mindate=date.today() + timedelta(days=1), maxdate=dmax, date_pattern="yyyy-mm-dd", disableddaybackground="grey", locale="en_US")
    cal.grid(row=0, column=0)
    settings.cList.append(cal)

    dateConfirm = Button(settings.window, text="Confirm Date", command=confirmCDate)
    dateConfirm.grid(row=1, column=1)
    settings.bList.append(dateConfirm)

    cancelButton = Button(settings.window, text="Cancel", command=lambda x=0: calCCancel(x))
    cancelButton.grid(row=1, column=0)
    settings.bList.append(cancelButton)

def calCCancel(num):
    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.cList.clear()

    if num != 0:
        searchPatientSpecialty()
    else:
        searchPatientDoctor()

def confirmCDate():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    count = 0
    for cal in settings.calendars:
        if str(settings.cList[0].get_date()) == str(cal.getDate()):
            for avail in settings.availability:
                if str(avail.getIDCalendar()) == str(cal.getIDCalendar()) and str(currentDoctor.getDoctorID()) == str(avail.getIDDoctor()) and str(avail.getAvail()) != str(0):
                    print(str(avail.getIDAvail()) + " " + str(cal.getTime()) + " " + str(avail.getAvail()))
                    dateConfirm = Button(settings.window, text="Confirm Time: " + str(cal.getTime()), command=lambda x=cal, y=avail: finalizeCAppointment(x, y))
                    dateConfirm.grid(row=count, column=0)
                    settings.bList.append(dateConfirm)
                    count = count + 1
    cancelButton = Button(settings.window, text="Cancel", command=showDCCalendar)
    cancelButton.grid(row=count, column=0)
    settings.bList.append(cancelButton)

def finalizeCAppointment(cal, avail):
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    global currentDate
    currentDate = cal

    global currentAvail
    currentAvail = avail

    currentAvail.setAvail(0)

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    strOp = [
        "New Appointment",
        "Follow-up"
    ]
    str1 = StringVar()
    str1.set(strOp[0])
    dateLabel = Label(settings.window, text=str(currentDate.getDate()))
    dateLabel.grid(row=0, column=0)
    settings.lList.append(dateLabel)

    timeLabel = Label(settings.window, text=str(currentDate.getTime()))
    timeLabel.grid(row=1, column=0)
    settings.lList.append(timeLabel)

    doctorLabel = Label(settings.window, text=str(currentDoctor.getName()) + "\nSpecialty: " + str(currentDoctor.getSpecialty()))
    doctorLabel.grid(row=2, column=0)
    settings.lList.append(doctorLabel)

    reasonDrop = OptionMenu(settings.window, str1, *strOp)
    reasonDrop.grid(row=3, column=0)
    global currentDrop
    currentDrop = reasonDrop

    textbox = Text(settings.window, height=5, width=52)
    textbox.grid(row=4, column=0)
    global currentText
    currentText = textbox

    confirm = Button(settings.window, text="Confirm", command=lambda x=str1, y=textbox: showCConfirm(x, y))
    confirm.grid(row=5, column=0)
    settings.bList.append(confirm)

def showCConfirm(drop, text):
    global currentDrop
    global currentText

    try:
        for i in range(0, len(settings.bList)):
            forgetWidget(settings.bList[i])

        for i in range(0, len(settings.lList)):
            forgetWidget(settings.lList[i])

        forgetWidget(currentDrop)
        forgetWidget(currentText)

        settings.connectSQL()
        sql = "INSERT IGNORE INTO Appointment (idCalendar, idDoctor, idPatient, appointmentType, reason) VALUES (%s, %s, %s, %s, %s)"
        val = (currentDate.getIDCalendar(), currentDoctor.getDoctorID(), currentPatient.getPatientID(), drop.get(), text.get("1.0", "end-1c"))
        cursor = settings.connector.cursor()
        cursor.execute(sql, val)

        settings.connector.commit()

        sql = "UPDATE Availability SET isAvailable = %s WHERE idAvailability = %s"
        val = (currentAvail.getAvail(), currentAvail.getIDAvail())
        cursor.execute(sql, val)
        settings.connector.commit()

        cursor.close()
        settings.closeSQL()

        clerkView()
    except len(currentText.get("1.0", "end-1c")) > 99:
        tkinter.messagebox.showerror("Error", "Max Character length 100")

def searchPatientSpecialty():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.idList.clear()

    headerLabel = Label(settings.window, text="Search for Specialty")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Specialty", "Name")
    specTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    specTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    specTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    for doctor in settings.doctors:
        settings.idList.append(doctor.getDoctorID())
        specTree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))
    specTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(specTree)

    searchLabel = Label(settings.window, text="Search Specialty")
    searchLabel.grid(row=2, column=0)
    settings.lList.append(searchLabel)

    global search
    search = StringVar()
    search.set("")

    searchEntry = Entry(settings.window, textvariable=search)
    searchEntry.grid(row=2, column=1)
    settings.eList.append(searchEntry)

    updateButton = Button(settings.window, text="Update Search", command=lambda x=specTree, y=search: searchSpecUpdate(x, y))
    updateButton.grid(row=2, column=2)
    settings.bList.append(updateButton)

    cancelButton = Button(settings.window, text="Cancel", command=clerkView)
    cancelButton.grid(row=3, column=0)
    settings.bList.append(cancelButton)

    confirmButton = Button(settings.window, text="Confirm", command=lambda x=specTree: confirmCSpecialty(x))
    confirmButton.grid(row=3, column=1)
    settings.bList.append(confirmButton)


def confirmCSpecialty(tree):
    try:
        temp = tree.selection()[0]
        for doctor in settings.doctors:
            for id in settings.idList:
                if doctor.getDoctorID() == id and tree.item(temp)['values'][1] == str(doctor.getName()) and tree.item(temp)['values'][0] == str(doctor.getSpecialty()):
                    global currentDoctor
                    currentDoctor = doctor
                    showSCCalendar()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")


def showSCCalendar():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    settings.cList.clear()
    dmax = date.today() + timedelta(days=365)
    cal = Calendar(settings.window, selectmode="day", mindate=date.today() + timedelta(days=1), maxdate=dmax, date_pattern="yyyy-mm-dd", disableddaybackground="grey", locale="en_US")
    cal.grid(row=0, column=0)
    settings.cList.append(cal)

    dateConfirm = Button(settings.window, text="Confirm Date", command=confirmSCDate)
    dateConfirm.grid(row=1, column=1)
    settings.bList.append(dateConfirm)

    cancelButton = Button(settings.window, text="Cancel", command=lambda x=1: calCCancel(x))
    cancelButton.grid(row=1, column=0)
    settings.bList.append(cancelButton)

def confirmSCDate():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()
    count = 0
    for cal in settings.calendars:
        if str(settings.cList[0].get_date()) == str(cal.getDate()):
            for avail in settings.availability:
                if str(avail.getIDCalendar()) == str(cal.getIDCalendar()) and str(currentDoctor.getDoctorID()) == str(avail.getIDDoctor()) and str(avail.getAvail()) != str(0):
                    print(str(avail.getIDAvail()) + " " + str(cal.getTime()) + " " + str(avail.getAvail()))
                    dateConfirm = Button(settings.window, text="Confirm Time: " + str(cal.getTime()), command=lambda x=cal, y=avail: finalizeSCAppointment(x, y))
                    dateConfirm.grid(row=count, column=0)
                    settings.bList.append(dateConfirm)
                    count = count + 1
    cancelButton = Button(settings.window, text="Cancel", command=showSCCalendar)
    cancelButton.grid(row=count, column=0)
    settings.bList.append(cancelButton)

def finalizeSCAppointment(cal, avail):
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    global currentDate
    currentDate = cal

    global currentAvail
    currentAvail = avail

    currentAvail.setAvail(0)

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    for i in range(0, len(settings.cList)):
        forgetWidget(settings.cList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    strOp = [
        "New Appointment",
        "Follow-up"
    ]
    str1 = StringVar()
    str1.set(strOp[0])
    dateLabel = Label(settings.window, text=str(currentDate.getDate()))
    dateLabel.grid(row=0, column=0)
    settings.lList.append(dateLabel)

    timeLabel = Label(settings.window, text=str(currentDate.getTime()))
    timeLabel.grid(row=1, column=0)
    settings.lList.append(timeLabel)

    doctorLabel = Label(settings.window, text=str(currentDoctor.getName()) + "\nSpecialty: " + str(currentDoctor.getSpecialty()))
    doctorLabel.grid(row=2, column=0)
    settings.lList.append(doctorLabel)

    reasonDrop = OptionMenu(settings.window, str1, *strOp)
    reasonDrop.grid(row=3, column=0)
    global currentDrop
    currentDrop = reasonDrop

    textbox = Text(settings.window, height=5, width=52)
    textbox.grid(row=4, column=0)
    global currentText
    currentText = textbox

    cancel = Button(settings.window, text="Cancel", command=confirmSCDate)
    cancel.grid(row=5, column=0)
    settings.bList.append(cancel)

    confirm = Button(settings.window, text="Confirm", command=lambda x=str1, y=textbox: showCConfirm(x, y))
    confirm.grid(row=5, column=1)
    settings.bList.append(confirm)


def viewPatientAppointments():
    w, h = settings.window.winfo_screenwidth(), settings.window.winfo_screenheight()
    settings.window.geometry("%dx%d+0+0" % (w, h))

    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    for i in range(0, len(settings.tList)):
        forgetWidget(settings.tList[i])

    settings.lList.clear()
    settings.tList.clear()
    settings.bList.clear()
    settings.eList.clear()

    headerLabel = Label(settings.window, text="View Appointments")
    headerLabel.grid(row=0, column=0)
    settings.lList.append(headerLabel)

    cols = ("Appointment Number", "Date", "Time", "Patient Name", "Doctor Name", "Specialty", "Appointment Type", "Reason")
    appointTree = ttk.Treeview(settings.window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Appointment Number", text="Appointment Number", anchor=tkinter.CENTER)
    appointTree.column("Appointment Number", minwidth=150, width=150)
    appointTree.heading("Date", text="Date", anchor=tkinter.CENTER)
    appointTree.column("Date", minwidth=75, width=75)
    appointTree.heading("Time", text="Time", anchor=tkinter.CENTER)
    appointTree.heading("Patient Name", text="Patient Name", anchor=tkinter.CENTER)
    appointTree.column("Patient Name", minwidth=150, width=150)
    appointTree.heading("Doctor Name", text="Doctor Name", anchor=tkinter.CENTER)
    appointTree.column("Doctor Name", minwidth=150, width=150)
    appointTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    appointTree.column("Specialty", minwidth=100, width=100)
    appointTree.heading("Appointment Type", text="Appointment Type", anchor=tkinter.CENTER)
    appointTree.column("Appointment Type", minwidth=150, width=150)
    appointTree.heading("Reason", text="Reason", anchor=tkinter.CENTER)
    appointTree.column("Reason", minwidth=200, width=200)
    for appointment in settings.appointments:
        for cal in settings.calendars:
            for doc in settings.doctors:
                if str(appointment.getIDCalendar()) == str(cal.getIDCalendar()) and str(appointment.getIDDoctor()) == str(doc.getDoctorID()) and str(appointment.getPatientID()) == str(currentPatient.getPatientID()):
                    appointTree.insert("", tkinter.END, values=(str(appointment.getIDAppointment()), (cal.getDate()), str(cal.getTime()), str(currentPatient.getName()), str(doc.getName()), str(doc.getSpecialty()), str(appointment.getType()), wrap(str(appointment.getReason()))))
    appointTree.grid(row=1, column=0, columnspan=2)
    settings.tList.append(appointTree)

    cancelButton = Button(settings.window, text="Cancel", command=clerkView)
    cancelButton.grid(row=2, column=0)
    settings.bList.append(cancelButton)

    editButton = Button(settings.window, text="Remove Appointment", command=lambda x=appointTree, y=2: removeAppointment(x, y))
    editButton.grid(row=2, column=1)
    settings.bList.append(editButton)


def exitProgram():
    logoutMSG = tkinter.messagebox.askquestion('Close?', 'Do you want to close the program?')
    if logoutMSG == 'yes':
        settings.window.destroy()


def exitLogin():
    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    settings.lList.clear()
    settings.bList.clear()
    settings.eList.clear()

    mainWindow()

def logout(num):
    for i in range(0, len(settings.bList)):
        forgetWidget(settings.bList[i])

    for i in range(0, len(settings.lList)):
        forgetWidget(settings.lList[i])

    for i in range(0, len(settings.eList)):
        forgetWidget(settings.eList[i])

    settings.lList.clear()
    settings.bList.clear()
    settings.eList.clear()

    if num == 0:
        employeeLogin()
    else:
        patientLogin()

def userLogout():
    logoutMSG = tkinter.messagebox.askquestion('Logout?', 'Do you wish to logout?')

    if logoutMSG == 'yes':
        for i in range(0, len(settings.bList)):
            forgetWidget(settings.bList[i])

        for i in range(0, len(settings.lList)):
            forgetWidget(settings.lList[i])

        for i in range(0, len(settings.eList)):
            forgetWidget(settings.eList[i])

        settings.lList.clear()
        settings.bList.clear()
        settings.eList.clear()

        mainWindow()