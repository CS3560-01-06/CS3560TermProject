from classes.Account import Account


class Staff(Account):
    def __init__(self, accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress, staffID, jobType):
        super().__init__(accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress)
        self.staffID = staffID # int
        self.jobType = jobType # string
