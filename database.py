import psycopg2
class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname='maintenance_tracker', user='postgres', password='justine', host='localhost', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except:
            print("Failed to connect to the database")

    def create_table_users(self):
        create_database_table = " CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name  VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL UNIQUE, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(100) NOT NULL, create_date TIMESTAMP DEFAULT  CURRENT_TIMESTAMP, is_admin BOOLEAN)"
        self.cursor.execute(create_database_table)

    def create_table_requests(self):
        create_requests_table = "CREATE TABLE IF NOT EXISTS requests(id SERIAL PRIMARY KEY, client_name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, category VARCHAR(100) NOT NULL, request_title VARCHAR(100) NOT NULL, description VARCHAR(250) NOT NULL, department VARCHAR(100) NOT NULL, status VARCHAR(100) DEFAULT 'pending...', create_date TIMESTAMP DEFAULT  CURRENT_TIMESTAMP)"
        self.cursor.execute(create_requests_table)

    def delete_table(self):
        delete = "DROP TABLE users"
        self.cursor.execute(delete)

    def close(self):
        self.cursor.close()


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table_users()
    database_connection.create_table_requests()
    # database_connection.delete_table()
