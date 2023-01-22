import sqlalchemy
import psycopg2

def create_db():
    initial_connection = psycopd2.connect(
        database='diplom',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432'
    )
    initial_connection.close()

def create_tables():
    connection.execute('''
    CREATE TABLE IF NOT EXISTS friend_users (
	id integer PRIMARY KEY,
	first_name varchar(40) NOT NULL UNIQUE,
	last_name varchar(40) NOT NULL UNIQUE,
	photo1 integer NOT NULL,
	photo2 integer NOT NULL,
	photo3 integer NOT NULL,
    );
    ''')

def insert_users(user, photo_data):
    if not connection.execute(f" SELECT id FROM friend_users WHERE id={user['id']}").fetchone():
        connection.execute(f"INSERT INTO friend_users (id, first_name, last_name, photo1, photo2, photo3)"
                           f"VALUES ({user['id']},\'{user['first_name']}\',"
                           f"\'{user['last_name']}\', {photo_data['photo_ids'][0]},"
                           f"{photo_data['photo_ids'][1]}, {photo_data['photo_ids'][2]});")

