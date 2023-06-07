class Shift:
    def __init__(self, doctor, day):
        self.doctor = doctor
        self.day = day
        self.points = day.points  # Les points attribués à cette garde sont déterminés par le type de jour
