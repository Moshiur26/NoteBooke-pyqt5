import sqlite3

class Db():


    conn = sqlite3.connect('exmpl.db')
    c = conn.cursor()

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS NoteBook (id integer primary key autoincrement, title text, note text)''')

    def insert_data(self,ttl,nte):
        title = ttl
        note = nte

        self.c.execute("INSERT INTO NoteBook(title,note) VALUES (?,?)", (title, note))
        self.conn.commit()
        # c.close()
        # conn.close()

    def read_from_db(self):
        self.c.execute('SELECT * FROM NoteBook')
        data = self.c.fetchall()

        print("data :",data[0][2])
        #for row in data:
         #   print(row)

        return data