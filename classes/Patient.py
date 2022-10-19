import Account


class Patient(Account):
    def __init__(self, patientID, status, insuranceType):
        self.patientID = patientID # int
        self.status = status # boolean
        self.insuranceType = insuranceType # string
