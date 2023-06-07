class Day:
    def __init__(self, date, type_day, points):
        self.date = date
        self.type_day = type_day
        self.points = points
        self.doctors_on_duty = []  # Liste des médecins de garde ce jour
