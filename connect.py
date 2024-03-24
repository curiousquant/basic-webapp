import psycopg2
from config import load_config
from urllib.parse import urlparse

def connect():
    
    pg_connection_dict = {
        'dbname': 'postgresdb_czir',
        'user': 'admin',
        'password': 'PmK1wFxvr4zd003IctgbUACt9bC4U6RE',
        'port': 5432,
        'host': 'dpg-cn5ovqmct0pc738hm5kg-a.ohio-postgres.render.com'
    }
    
    try:
        con = psycopg2.connect(**pg_connection_dict)
        print("Connected successfully!")
        return con
    except Exception as e:
        print(f"Error: {e}")

def selectItems(connection):
    try:
        cursor = connection.cursor()
        # Example: Retrieve all rows from the 'employees' table
        cursor.execute("SELECT * FROM headline")
        results = cursor.fetchall()
        
        return results
    except Exception as e:
        print(f"Error executing query: {e}")

    finally:
        cursor.close()
        connection.close()
if __name__ == '__main__':
    #db_config = load_config()
    con = connect()
    selectItems(con)