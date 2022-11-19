class Cal():
    def __init__(self, idCalendar, date, time):
        self.idCalendar = idCalendar # int
        self.date = date # int
        self.time = time
    def getIDCalendar(self):
        return self.idCalendar

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time