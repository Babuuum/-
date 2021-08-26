import sqlalchemy

engine = sqlalchemy.create_engine("postgresql://postgres:******@localhost:5432/hometask")

connection = engine.connect()

connection.execute("""SELECT name, relese_date FROM albums 
WHERE relese_date = 2018;
""")

connection.execute("""SELECT name, duration FROM tracks 
ORDER BY duration DESC
LIMIT 1;
""")

connection.execute("""SELECT name FROM tracks 
WHERE duration >= 210;
""")

connection.execute("""SELECT name FROM collections 
WHERE duration BETWEEN 2018 AND 2020;
""")

connection.execute("""SELECT name FROM performers 
WHERE name LIKE NOT '%% %%';
""")

connection.execute("""SELECT name FROM tracks 
WHERE name LIKE '%%my%%' OR name LIKE '%%мой%%';
""")