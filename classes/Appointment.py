import Doctor
import Patient

class Appointment(Doctor,Patient):
    def __init__(self,appointmentType, reason, time):
        self.appointmentType = appointmentType # string
        self.reason = reason # string
        self.time = time # int
