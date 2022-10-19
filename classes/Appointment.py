import Doctor
import Patient

class Appointment(Doctor,Patient):
    def __init__(self,appointmentType, reason, time):
        self.appointmentType = appointmentType
        self.reason = reason
        self.time = time
