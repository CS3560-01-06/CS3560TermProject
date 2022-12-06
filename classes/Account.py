class Account:
    def __init__(self, accountID, name, age, gender, dateOfBirth, phoneNumber, username, password, emailAddress):
        self.accountID = accountID
        self.name = name # string
        self.age = age # int
        self.gender = gender # string
        self.dateOfBirth = dateOfBirth # int
        self.phoneNumber = phoneNumber # int
        self.username = username # string
        self.password = password # string
        self.emailAddress = emailAddress # string

    def login(self):
        return

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getName(self):
        return self.name

    def getEmail(self):
        return self.emailAddress