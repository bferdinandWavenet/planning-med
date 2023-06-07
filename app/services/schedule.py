from app.models.doctor import Doctor
from app.models.day import Day
from app.models.shift import Shift

# Vous devez charger vos médecins et vos jours de votre base de données, c'est juste un exemple simplifié
doctors = [Doctor(1, "Dr. A"), Doctor(2, "Dr. B"), Doctor(3, "Dr. C")]
days = [Day("2023-07-03", "weekday", 2), Day("2023-07-04", "weekday", 2)]  # etc.
shifts = []

def can_assign_shift(doctor, day):
    # Ici, vous devez implémenter la logique pour vérifier si un médecin peut être assigné à un shift.
    # Par exemple, vérifiez que le médecin n'a pas déjà une garde dans les 3 jours précédents.
    pass

def assign_shift(doctor, day):
    # Ici, vous créez un nouveau Shift et l'ajoutez à la liste des shifts.
    # Vous devez également mettre à jour le total de points du médecin.
    shift = Shift(doctor, day)
    shifts.append(shift)
    doctor.total_points += day.points

def find_doctor_with_lowest_score(doctors):
    # Retourne le médecin avec le score total le plus bas
    return min(doctors, key=lambda doctor: doctor.total_points)

def find_doctor_with_least_shifts(doctors):
    # Retourne le médecin avec le moins de gardes
    return min(doctors, key=lambda doctor: len([shift for shift in shifts if shift.doctor == doctor]))

# L'algorithme d'attribution des gardes
for doctor in doctors:
    for desired_day in doctor.desired_days:
        if can_assign_shift(doctor, desired_day):
            assign_shift(doctor, desired_day)

remaining_days = [day for day in days if not any(shift.day == day for shift in shifts)]
while remaining_days:
    doctor_with_lowest_score = find_doctor_with_lowest_score(doctors)
    next_day = remaining_days.pop(0)
    if can_assign_shift(doctor_with_lowest_score, next_day):
        assign_shift(doctor_with_lowest_score, next_day)

remaining_days = [day for day in days if not any(shift.day == day for shift in shifts)]
while remaining_days:
    doctor_with_least_shifts = find_doctor_with_least_shifts(doctors)
    next_day = remaining_days.pop(0)
    if can_assign_shift(doctor_with_least_shifts, next_day):
        assign_shift(doctor_with_least_shifts, next_day)
