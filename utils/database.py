import psycopg2 as db
from main import config


class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            password=config.DB_PASS,
            user=config.DB_USER,
            host=config.DB_HOST
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        user_table = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(55),
        phone_number VARCHAR(13),
        location_name VARCHAR(55))
        """

        photos = """
        CREATE TABLE IF NOT EXISTS photos (
        id SERIAL PRIMARY KEY,
        user_id INT references users(id),
        status BOOLEAN DEFAULT false)
        """

        likes = """
        CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        user_id INT references users(id),
        photo_id INT references photos(id),
        is_like BOOLEAN DEFAULT false)
        """

        self.cursor.execute(user_table)
        self.cursor.execute(photos)
        self.cursor.execute(likes)

        self.conn.commit()
