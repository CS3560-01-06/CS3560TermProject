
#Staff class inherits person
#Staff ID
#Active Staff
#Job Type
#Specialty



import VisitData
import Person

class Staff:
    def __init__(self, name = "Dr. John Doe", patient = "ABC", job_type = "Doctor", specialty = "Cardiology"):
        self.name = name
        self.patients = patient
        self.job_type = job_type
        if(specialty):
            self.specialty = specialty
        self.id
    
    def get_patients(self) -> str:
        return self.patients
    def get_log(self):
        return patient.log
    
    def get_specialty(self):
        return self.specialty

    def get_id(self):
        return self.id
    def job_type(self):
        return self.job_type