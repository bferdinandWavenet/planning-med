import os
from dotenv import load_dotenv
import mysql.connector

# Charge les variables d'environnement du fichier .env
load_dotenv()

# Récupère les variables d'environnement
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')

# Établit une connexion à la base de données
cnx = mysql.connector.connect(user=db_user, password=db_pass,
                              host=db_host,
                              database=db_name)


# Créez un curseur
cursor = cnx.cursor()

# Exécutez une requête
query = ("SELECT * FROM mytable")
cursor.execute(query)

# Parcourez et imprimez les résultats
for row in cursor:
    print(row)

# N'oubliez pas de fermer la connexion lorsque vous avez terminé
cursor.close()
cnx.close()
