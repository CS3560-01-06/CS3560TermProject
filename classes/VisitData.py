import Visit

class VisitLog():
    '''
    A VisitLog is used to track the number of times a certain Patient has visited the hospital
    It consists of a simple array of Visits, which can be appended to, but not deleted.
    '''
    def __init__(self, log=None):
        self.log = log if log != None else []
    
    def __len__(self):
        return len(self.log)

    def append(self, visit: Visit.Visit):
        self.log.append(visit)
    
    def append(self, date, time, description):
        self.log.append(Visit.Visit(date, time, description))
    
    def get_visit(self, index):
        if 0 <= index <= len(self.log):
            return str(self.log[index])
        else:
            raise IndexError(f"Index {index} out of bounds.")

class Visit():
    '''
    A Visit is an instance of a Patient visiting the hospital.
    It is the time, date, and description of a visit.
    These are meant to be immutable.
    '''
    def __init__(self, date: str, time: str, desc: str):
        self.date = date
        self.time = time
        self.desc = desc
        self.id = hash(self)
    
    def __hash__(self):
        return hash((self.date, self.time, self.description))

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.date == __o.date and self.time == __o.time and self.desc == __o.desc

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    
    def __str__(self):
        return f"Date:\t{self.date}\nTime:\t{self.time}\n{self.description}"
    
    def __repr__(self):
        return f"<Visit Object of ID {self.id}, Parameters(\"{self.date}\", \"{self.time}\", \"{self.description}\")>"

    def get_visit(self):
        return (self.time, self.date, self.description)
    
