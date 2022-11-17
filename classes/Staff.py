from classes.Account import Account


class Staff(Account):
    def __init__(self, staffID, activeStaff, jobType):
        self.staffID = staffID # int
        self.activeStaff = activeStaff # boolean
        self.jobType = jobType # string
