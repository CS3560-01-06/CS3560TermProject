import Doctor
import Calender

class Availability(Doctor, Calender):
    def __init__(self, isAvailable):
        self.isAvailable = isAvailable # boolean
