import mysql.connector
from mysql.connector import MySQLConnection
from config import DB_CONFIG


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(**DB_CONFIG) # Tworzymy połączenie z bazą danych.


def execute(query: str, params, fetch: str = None):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True) # Zwraca dane w formie słownika a nie tuple
        cursor.execute(query, params)
        if fetch == "all":
            return cursor.fetchall()
        elif fetch == "one":
            return cursor.fetchone()
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()