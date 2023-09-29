import psycopg2

class Database:
    def __init__(self, host, database, user, password) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

if __name__ == '__main__':
    db = Database(host="localhost", database="pea_tomtom", user="postgres", password="postgres")
    cursor = db.conn.cursor()
    cursor.execute("select * from stocks limit 1")
    print(cursor.fetchall())
    cursor.close()