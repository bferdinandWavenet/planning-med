from dotenv import load_dotenv
import mysql.connector
import os
from datetime import date, timedelta

load_dotenv()

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST', 'localhost')

# Connect to MySQL
cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = cnx.cursor()

# définition des scores
scores = {
    0: 2,  # Lundi
    1: 2,  # Mardi
    2: 2,  # Mercredi
    3: 1,  # Jeudi
    4: 3,  # Vendredi
    5: 5,  # Samedi
    6: 4,  # Dimanche
}

# jours fériés
holidays = [date(2023, 7, 21), date(2023, 8, 15)]

start_date = date(2023, 7, 3)
end_date = date(2023, 10, 1)

current_date = start_date

while current_date <= end_date:
    # vérifie si le jour est un jour férié
    if current_date in holidays:
        points = 5
        type_day = 'holiday'
    else:
        points = scores[current_date.weekday()]
        type_day = 'normal'
        if current_date.weekday() == 4:  # Friday
            type_day = 'friday'
        elif current_date.weekday() == 6:  # Sunday
            type_day = 'sunday'

    # génère la requête SQL
    query = (f"INSERT INTO days (date, type_day, points) VALUES ('{current_date}', '{type_day}', {points})")

    # Exécute la requête
    cursor.execute(query)

    # pour les samedis, on insère un deuxième enregistrement pour le service d'urgence
    if current_date.weekday() == 5:  # Saturday
        type_day = 'saturday_emergency'
        points = 3
        query = (f"INSERT INTO days (date, type_day, points) VALUES ('{current_date}', '{type_day}', {points})")
        cursor.execute(query)

    current_date += timedelta(days=1)

# Assurez-vous que les modifications sont appliquées à la base de données
cnx.commit()

# Ferme les connexions
cursor.close()
cnx.close()
