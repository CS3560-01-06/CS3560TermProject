import Account


class Staff(Account):
    def __init__(self, staffID, activeStaff, jobType):
        self.staffID = staffID
        self.activeStaff = activeStaff
        self.jobType = jobType
