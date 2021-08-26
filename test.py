import sqlalchemy

engine = sqlalchemy.create_engine("postgresql://postgres:Ragimaliev2013@localhost:5432/hometask")

connection = engine.connect()

connection.execute('''INSERT INTO performers(name)
VALUES("Three Days Grace",
"Nirvana",
"Misfits",
"Venom Prison",
"Elvis Presley",
"Chuck Berry",
"Motörhead",
"Breaking Benjamin");''')
