# ligação à base de dados
import sqlite3
connetion = sqlite3.connect("contacts.db")
cursor = connetion.cursor()

cursor.execute("""create table if not exists 'Contactos'(
                   id integer primary key,
                   name text not null,
                   email text null
                )
               """)