
class Peter:
    def __init__(self, mood, name, kid_name):
        self.instantiated_mood = mood
        self.gender = "male"
        self.age = 31
        self.wife = "Sally"
        self.surname = "Petersen"
        self.full_name = self.name_plus_surname(name, self.surname)

        self.kid_name = kid_name

def name_plus_surname(self, name, surname):
    full_name = f"{name} {surname}"
    return full_name

def build_kid_full_name():
    full_kid_name = f"{self.kid_name} {self.surname}"

instantiated_peter = Peter("happy", )

