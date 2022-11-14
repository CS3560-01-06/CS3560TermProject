class VisitLog():
    '''
    A VisitLog is used to track the incoming visits that a Patient has for the hospital in the future.
    It consists of a simple array of Visits, which can be modified and indexed using the given methods.
    '''
    def __init__(self, log=None, max=None):
        self.log = log if log != None else []
        self.max = max if max != None else 1000
    
    def __len__(self):
        return len(self.log)

    def append(self, visit):
        if self.log.__len__ < max:
           self.log.append(visit)
           return True
        return False
    
    def append(self, date, time, description) -> bool:
        if self.log.__len__ < max:
            self.log.append(Visit(date, time, description))
            return True
        return False
        
    def remove(self, index: int):
        if self.log.__len__ <= index:
            return False
        self.log.pop(index)
        return True
    
    def get_visit(self, index):
        if 0 <= index <= len(self.log):
            return str(self.log[index])
        else:
            raise IndexError(f"Index {index} out of bounds.")
    
    def return_visits(self):
        return self.log
    
    def search_visits(self, **kwargs):
        results = set([])
        results += [(ind, visit) for ind, visit in enumerate(self.log) if visit.id == kwargs.get("ID")]
        results += [(ind, visit) for ind, visit in enumerate(self.log) if visit.date == kwargs.get("Date")]
        results += [(ind, visit) for ind, visit in enumerate(self.log) if visit.time == kwargs.get("Time")]
        results += [(ind, visit) for ind, visit in enumerate(self.log) if visit.desc == kwargs.get("Desc")]    
        return results


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
        return isinstance(__o, self.__class__) and (self.date == __o.date and self.time == __o.time and self.desc == __o.desc) or (self.id == __o.id)

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    
    def __str__(self):
        return f"Date:\t{self.date}\nTime:\t{self.time}\n{self.description}"
    
    def __repr__(self):
        return f"<Visit Object of ID {self.id}, Parameters(\"{self.date}\", \"{self.time}\", \"{self.description}\")>"

    def get_visit(self):
        return (self.time, self.date, self.description)
    
