import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
import os
load_dotenv()

def Conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if conexao.is_connected():
            print("Conectado ao banco de dados!")
            return conexao
    
    except Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None 