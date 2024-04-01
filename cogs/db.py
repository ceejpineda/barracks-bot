import mysql.connector

def create_connection():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="c3_dev"
    )
    return cnx