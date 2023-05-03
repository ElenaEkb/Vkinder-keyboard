import psycopg2


conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='Ghfdlf1407$',
    database='diplom'
    )


def create_table_seen_person(conn):
    """создает Таблицу"""
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS seen_person(
                id_vk varchar(50) NOT NULL,
                id_ws varchar(50) NOT NULL,
                PRIMARY KEY(id_vk, id_ws));"""
        )
        conn.commit()


def insert_data_seen_person(conn, id_vk, id_ws):
    """вставка данных в таблицуe"""
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            INSERT INTO seen_person (id_vk, id_ws)
            VALUES ({id_vk}, {id_ws})
           """
        )
        conn.commit()


def check(conn, id_vk, id_ws):
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT id_vk FROM seen_person 
            WHERE id_vk = %(id_vk)s AND id_ws = %(id_ws)s;
            """, {'id_vk': str(id_vk), 'id_ws': str(id_ws)}
        )
        out = cursor.fetchall()
        return False if out else True

    return False if out else True


if __name__ == '__main__':
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Ghfdlf1407$',
        database='diplom'
    )

