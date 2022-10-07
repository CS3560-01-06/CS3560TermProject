import VisitData

'''
A Patient is someone who is enrolled in the systems of the hospital.
They have a name, age, and a Visit Log, defined in another file.
'''

class Patient:
    def __init__(self, name="John Doe", age=0):
        self.name = name
        self.age = age
        self.log = VisitData.VisitLog()
        self.id
    
    def __hash__(self) -> int:
        return hash((self.name, self.age))
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.name == __o.name and self.age == __o.age
    
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    
    def __str__(self) -> str:
        return f"{self.name}, Age {self.age}. Number of visits: {len(self.log)}."
    
    def __repr__(self):
        return f"<Patient Object of ID {self.id}, Parameters(\"{self.name}\", \"{self.age}\")>"

    def get_log(self):
        return self.log
    
    def record_visit(self, ):
        self.log.append()