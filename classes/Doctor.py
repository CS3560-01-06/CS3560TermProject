from classes.Staff import Staff

class Doctor(Staff):
    def __init__(self, accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress, staffID, jobType, doctorID, specialty):
        super().__init__(accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress, staffID, jobType)
        self.doctorID = doctorID
        self.specialty = specialty # string

    def getSpecialty(self):
        return self.specialty


    def getDoctorID(self):
        return self.doctorID