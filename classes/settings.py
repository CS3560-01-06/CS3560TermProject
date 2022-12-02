from tkinter import *
from classes.Patient import Patient
from classes.Doctor import Doctor
from classes.Staff import Staff
from classes.Availability import Availability
from classes.Appointment import Appointment
from classes.Calender import Cal
import mysql.connector

connector = mysql.connector.connect(host='127.0.0.1', user='nick', password='nd26',
                                    database='3560sql', auth_plugin='mysql_native_password')
window = Tk()
lList = []
bList = []
eList = []
tList = []
cList = []
calendars = []
availability = []
patient = []
doctors = []
employees = []
idList = []
appointments = []
username = StringVar()
passww = StringVar()


def connectSQL():
    global connector
    connector = mysql.connector.connect(host='127.0.0.1', user='nick', password='nd26',
                                        database='3560sql', auth_plugin='mysql_native_password')

def closeSQL():
    if connector.is_connected():
        connector.close()

def getPatients():
    selectAccount = "select * from Account"
    cursor = connector.cursor()
    cursor.execute(selectAccount)
    records = cursor.fetchall()
    selectPatient = "select * from Patient"
    cursor.execute(selectPatient)
    records2 = cursor.fetchall()

    for row in records:
        for rrow in records2:
            if row[0] == rrow[1]:
                patient.append(
                    Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], rrow[0],
                            rrow[2], rrow[3]))

    cursor.close()

def getDoctors():
    selectAccount = "select * from Account"
    cursor = connector.cursor()
    cursor.execute(selectAccount)
    records = cursor.fetchall()
    selectStaff = "select * from Staff"
    cursor.execute(selectStaff)
    records2 = cursor.fetchall()
    selectDoctor = "select * from Doctor"
    cursor.execute(selectDoctor)
    records3 = cursor.fetchall()

    for row in records:
        for rrow in records2:
            for rrrow in records3:
                if row[0] == rrrow[2] and rrow[0] == rrrow[1]:
                    doctors.append(
                        Doctor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], rrow[0],
                               rrow[2], rrrow[0], rrrow[3]))

    cursor.close()

def getEmployees():
    selectAccount = "select * from Account"
    cursor = connector.cursor()
    cursor.execute(selectAccount)
    records = cursor.fetchall()
    selectStaff = "select * from Staff"
    cursor.execute(selectStaff)
    records2 = cursor.fetchall()

    for row in records:
        for rrow in records2:
            if row[0] == rrow[1]:
                employees.append(
                    Staff(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], rrow[0], rrow[2]))

    cursor.close()

def getAvailability():
    selectAvail = "select * from Availability"
    cursor = connector.cursor()
    cursor.execute(selectAvail)
    records = cursor.fetchall()

    for row in records:
        availability.append(Availability(row[0], row[1], row[2], row[3]))

    cursor.close()

def getCalendar():
    selectCal = "select * from Calendar"
    cursor = connector.cursor()
    cursor.execute(selectCal)
    records = cursor.fetchall()

    for row in records:
        calendars.append(Cal(row[0], row[1], row[2]))

    cursor.close()

def getAppointments():
    selectAvail = "select * from Appointment"
    cursor = connector.cursor()
    cursor.execute(selectAvail)
    records = cursor.fetchall()

    for row in records:
        appointments.append(Appointment(row[0], row[1], row[2], row[3], row[4], row[5]))

    cursor.close()

def updateLists():
    calendars.clear()
    availability.clear()
    patient.clear()
    doctors.clear()
    employees.clear()
    appointments.clear()

    connectSQL()
    getPatients()
    getDoctors()
    getEmployees()
    getAvailability()
    getCalendar()
    getAppointments()
    closeSQL()

