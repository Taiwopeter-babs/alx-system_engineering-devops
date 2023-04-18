-- creates a table with entries
CREATE DATABASE IF NOT EXISTS tyrell_corp;

CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (
	id INT NOT NULL AUTO_INCREMENT UNIQUE DEFAULT 1,
	name VARCHAR(256) NOT NULL
	);
INSERT INTO tyrell_corp.nexus6(name)
VALUES 
	("Taiwo peter"),
	("Kehinde paul");

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
