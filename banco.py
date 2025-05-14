import sqlite3 as lite

#criar um banco
con = lite.connect("dado.db")
sql = con.cursor()

#criando tabela
sql.execute('''create table if not exists login(id integer primary key autoincrement,
nome varchar(40), email varchar(40),login varchar(40),senha varchar(40));''')

#adicionando