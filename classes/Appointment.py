class Appointment:
    def __init__(self, idAppointment, idCalendar, idPatient, idDoctor, appointmentType, reason):
        self.idAppointment = idAppointment
        self.idCalendar = idCalendar  # int
        self.idPatient = idPatient  # int
        self.idDoctor = idDoctor  # int
        self.appointmentType = appointmentType # string
        self.reason = reason # string

    def getIDCalendar(self):
        return self.idCalendar

    def getIDDoctor(self):
        return self.idDoctor

    def getPatientID(self):
        return self.idPatient

    def getType(self):
        return self.appointmentType

    def getReason(self):
        return self.reason

    def getIDAppointment(self):
        return self.idAppointment