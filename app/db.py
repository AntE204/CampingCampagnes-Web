from .config import Config
import mysql.connector
import bcrypt
from mysql.connector import Error
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract

type Base = PooledMySQLConnection | MySQLConnectionAbstract

class DB:
    @staticmethod
    def get_db(config: Config)->Base:
        host = config.get("DB_HOST")
        user = config.get("DB_USER")
        password = config.get("DB_PASSWORD")
        database = config.get("DB_NAME")

        return mysql.connector.connect(
            host,
            user,
            password,
            database
        )

    def check_email_used(email: str) -> bool:
        connection : Base = DB.get_db()
        cursor = connection.cursor(dictionary=True)
        checkEmail = "SELECT * FROM utilisateur WHERE email = %s"
        cursor.execute(checkEmail, email)
        res = cursor.fetchone()

        cursor.close()
        connection.close()
        return res

    def password_hash(mdpClair: str)-> str:
        return bcrypt.hashpw(mdpClair, bcrypt.gensalt())

    def password_verify(mdpClair:str, mdpHash:str)->bool:
        return bcrypt.checkpw(mdpClair, mdpHash)

    def inscription(nom: str, prenom: str, mail:str, password: str, ville: str, rue: str, code_postal: str, tel: str)->tuple[str, str]:
        if(DB.check_email_used(mail)):
            return ("L'email renseigné est déja utilisé", "danger")

        connection : Base = DB.get_db()
        cursor = connection.cursor()

        passwordHash= DB.password_hash(password)
        inser = "INSERT INTO utilisateur (nom, prenom, mail, motDePasse, ville, rue, codePostal, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            params=(nom, prenom, passwordHash, ville, rue, code_postal, tel)
            cursor.execute(inser, params)
            connection.commit()
            message = ("Votre compte a été crée, veuillez vous y connecter", "success")
        except Error as e:
            connection.rollback()
            message = (f"Erreur lors de la création de l'utilisateur : {e}", "danger")
        finally:
            cursor.close()
            connection.close()
        
        return message