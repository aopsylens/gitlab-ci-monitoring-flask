CREATE TABLE something(
	id serial PRIMARY KEY,
	name VARCHAR (50) UNIQUE NOT NULL);

INSERT INTO something (id, name) VALUES (1, 'devops');