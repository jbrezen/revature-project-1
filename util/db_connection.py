import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='postgres',
            password='SuperJ98!',
            host='jbrezenpostgres.cjssqswshuti.us-east-2.rds.amazonaws.com',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(f'{e}')
        return conn


connection = create_connection()