import sqlite3


class Client:
    def __init__(self, *args):
        #я хотів щоб number проставлявся інкрементально, саме в БД. Але екземпляр класу я можу створити в коді
        #не придумав нічого кращого, соррі
        if len(args) == 6:
            self.number = args[0]
            self.name = args[1]
            self.surname = args[2]
            self.phone = args[3]
            self.deal_type = args[4]
            self.status = args[5]
        else:
            self.number = None
            self.name = args[0]
            self.surname = args[1]
            self.phone = args[2]
            self.deal_type = args[3]
            self.status = args[4]


    def __repr__(self):
        return f"Client(number={self.number},name={self.name}, surname={self.surname}, phone={self.phone}, deal_type={self.deal_type}, status={self.status})"


class AbstractRepository:

    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path, isolation_level=None)
        self._cursor = self._connection.cursor()

    def __del__(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()


class ClientRepository(AbstractRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        self._cursor.execute(
            """CREATE TABLE IF NOT EXISTS clients
            (number integer NOT NULL CONSTRAINT table_name_pk  PRIMARY KEY AUTOINCREMENT,
            name text,
            surname text,
            phone text,
            deal_type integer,
            status integer);""")

    def add_client(self, c: Client):
        self._cursor.execute(f"""INSERT INTO clients (name, surname, phone, deal_type, status)
                                    VALUES ('{c.name}', '{c.surname}', '{c.phone}', '{c.deal_type}', '{c.status}')""")
        return self

    def row2object(self, row):
        return Client(*row)

    def rows2objects(self, rows):
        return [self.row2object(row) for row in rows]

    def get_all_clients(self):
        data = self._cursor.execute('SELECT * from clients order by number asc;')
        return self.rows2objects(data)

    def search_client_by_text(self, by, condition):
        if by in ['name', 'surname', 'phone']:
            data = self._cursor.execute(f"""SELECT * from clients where {by} like '%{condition}%'
                                            order by number asc;""")
            return self.rows2objects(data)
        else:
            return None

    def search_client_by_number(self, number):
        data = self._cursor.execute(f"""SELECT * from clients where number = {number}
                                        order by number asc;""")
        return self.rows2objects(data)

    def delete_by_number(self, number):
        self._cursor.execute(f"""DELETE FROM clients WHERE number = {number}""")
        return self

    def update_status_by_number(self, number, status):
        self._cursor.execute(f"""UPDATE clients SET status = {status} WHERE number = {number}""")


repo = ClientRepository('dbs/test.db')
user1 = Client('Harry', 'Potter', '93412', 1, 2)
user2 = Client('John', 'Rambo', '1221', 2, 1)

# Add client
repo.add_client(user1)
repo.add_client(user2)

# Search client:
print(repo.get_all_clients())
print(repo.search_client_by_text('name', 'Jo'))

# Update status
repo.update_status_by_number(2,3)

# Delete user
repo.delete_by_number(2)




