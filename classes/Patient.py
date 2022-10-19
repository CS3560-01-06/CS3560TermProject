import Account


class Patient(Account):
    def __init__(self, patientID, status, insuranceType):
        self.patientID = patientID
        self.status = status
        self.insuranceType = insuranceType
