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

CREATE TABLE predictionDB.AUD AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('AUD', 'Dolar Australijski', 'A');

CREATE TABLE predictionDB.CHF AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('CHF', 'Frank Szwajcarski', 'A');

CREATE TABLE predictionDB.GBP AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('GBP', 'Funt Szterling', 'A');

CREATE TABLE predictionDB.JPY AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('JPY', 'Jen (Japonia)', 'A');

CREATE TABLE predictionDB.CZK AS TABLE predictionDB.GOLD;
INSERT INTO predictionDB.types(id, full_name, table_id) VALUES ('CZK', 'Korona Czeska', 'A');



-- przydatne komendy
\dt predictionDB.* --wylistowanie wszystkich tabel w schemacie predictionDB
SELECT * FROM predictionDB.types;
SELECT * FROM predictionDB.GOLD;
DROP SCHEMA predictionDB CASCADE;