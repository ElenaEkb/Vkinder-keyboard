def creat_db():
    initial_connection = psycopd2.connect(
        database='diplom',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432'
    )
    initial_connection.close()


