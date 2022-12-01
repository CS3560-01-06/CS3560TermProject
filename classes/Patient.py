from classes.Account import Account


class Patient(Account):
    def __init__(self, accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress, patientID, status, insuranceType):
        super().__init__(accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress)
        self.patientID = patientID # int
        self.status = status # boolean
        self.insuranceType = insuranceType # string

    def getPatientID(self):
        return self.patientID

