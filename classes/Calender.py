import Doctor

class Calender(Doctor):
    TIMES = ['9:00AM','9:30AM','10:00AM','10:30AM','11:00AM','11:30AM','12:00PM','12:30PM',
             '1:00PM','1:30PM','2:00PM','2:30PM','3:00PM','3:30PM','4:00PM','4:30PM','5:00PM']

    def __init__(self,callID,date):
        self.callID = callID # int
        self.date = date # int

    def getAvailableTimes(self):
        return self.TIMES

    def removeTime(self, time: str):
        if time in self.TIMES:
            self.TIMES.remove(time)