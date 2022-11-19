import tkinter.messagebox
from tkinter import messagebox

class Availability:
    def __init__(self, idAvailability, idDoctor, idCalendar, isAvailable):
        self.idAvailability = idAvailability
        self.idDoctor = idDoctor
        self.idCalendar = idCalendar
        self.isAvailable = isAvailable # boolean

    def getIDAvail(self):
        return self.idAvailability

    def getIDDoctor(self):
        return self.idDoctor

    def getIDCalendar(self):
        return self.idCalendar

    def getAvail(self):
        return self.isAvailable

    def setAvail(self, avail):
            self.isAvailable = avail