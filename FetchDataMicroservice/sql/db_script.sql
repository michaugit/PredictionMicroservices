CREATE SCHEMA predictionDB;

CREATE TABLE predictionDB.types(
	id VARCHAR (30) UNIQUE NOT NULL,
	full_name VARCHAR (30) UNIQUE NOT NULL,
    table_id VARCHAR (1) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE predictionDB.GOLD(
    date DATE UNIQUE NOT NULL,
    value NUMERIC NOT NULL,
	PRIMARY KEY (date)
	);
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('GOLD', 'Zloto', 'G');


CREATE TABLE predictionDB.USD AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('USD', 'Dolar Amerykanski', 'A');


CREATE TABLE predictionDB.EUR AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('EUR', 'Euro', 'A');





-- przydatne komendy
\dt predictionDB.* --wylistowanie wszystkich tabel w schemacie predictionDB
SELECT * FROM predictionDB.types;
SELECT * FROM predictionDB.GOLD;
DROP SCHEMA predictionDB CASCADE;