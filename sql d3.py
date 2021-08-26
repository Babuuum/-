# я так и не понял как создать отдельный файл(для заполнения) или что я заполняю и где это находится, так что все делалось вслепую(извиняюсь за крайне сырое дз)
import sqlalchemy

engine = sqlalchemy.create_engine("postgresql://postgres:******@localhost:5432/hometask")

connection = engine.connect()

connection.execute('''INSERT INTO performers
VALUES(1, 'Three Days Grace'),
(2, 'Nirvana'),
(3, 'Misfits'),
(4, 'Venom Prison'),
(5, 'Elvis Presley'),
(6, 'Chuck Berry'),
(7, 'Motörhead'),
(8, 'Breaking Benjamin');
''')

connection.execute('''INSERT INTO gernes
VALUES(1, 'grunge'),
(2, 'post grunge'),
(3, 'punk rock'),
(4, 'death metal'),
(5, 'rock-n-roll');
''')

connection.execute('''INSERT INTO albums
VALUES(1, 'Human', 2015, 'NONE'),
(2, 'Nevermind', 1991, 'GRAMMY'),
(3, 'Famous Monsters', 1999, 'NONE'),
(4, 'Primeval', 2020 'NONE'),
(5, 'How Great Thou Art', 1967 'SNICKERS'),
(6, 'Chuck Berry Is on Top', 1959 'DALI DENEG)))))'),
(7, 'Ace of Spades', 1980) 'YSTAL ISKAT" NAGRADI',
(8, 'Saturate', 2002 '((((');
''')

connection.execute('''INSERT INTO tracks
VALUES(1, 'track1', 201, 1),
(2, 'track2', 202, 1),
(3, 'track3', 203, 2),
(4, 'track4', 11231, 2),
(5,	'track5', 1, 3),
(6,	'track6', 204, 3),
(7,	'track7', 205,	4),
(8	'track8', 180,	4),
(9	'track9', 160,	5),
(10, 'track10', 180,	5),
(11, 'track11', 300,	6),
(12, 'track12', 310,	6),
(13, 'track13', 280,	7),
(14, 'track14', 30,	7),
(15, 'track15', 250,	8);
''')

connection.execute('''INSERT INTO collections
VALUES(1, 'PODDBORKA DL9 GULEI', 2005),
(2,	'MY3IKA DL9 KA4ALKI',	1999),
(3,	'4YVSTVENNIE TREKI',	2028),
(4,	'GACHI PODDBORKA 2019',	1999),
(5,	'(=MORGERSTEIN - KRYTIE TREKI=)',	1),
(6,	'JEST9K',	1970),
(7,	'MY3IKA DL9 TA4KI/KA4ALKI',	2011),
(8,	'!!!!!!HITI 2010!!!!!!',	2010);
''')

connection.execute('''INSERT INTO performers_albums
VALUES(1, 1, 1);
''')

connection.execute('''INSERT INTO performers_genres
VALUES(1, 2 ,1);
''')

connection.execute('''INSERT INTO tracks_collections
VALUES(1, 1, 2);
''')





