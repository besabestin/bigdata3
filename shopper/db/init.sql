CREATE USER shopperdbuser WITH PASSWORD 'bgdata3.0';

GRANT ALL ON SCHEMA public TO shopperdbuser;
GRANT USAGE, CREATE ON SCHEMA public to shopperdbuser;

CREATE DATABASE shopperdb;
GRANT ALL PRIVILEGES ON DATABASE shopperdb TO shopperdbuser;
ALTER DATABASE shopperdb OWNER TO shopperdbuser;

\c shopperdb shopperdbuser;

ALTER DEFAULT PRIVILEGES GRANT ALL ON TABLES TO shopperdbuser;
ALTER DEFAULT PRIVILEGES GRANT ALL ON SEQUENCES TO shopperdbuser;

-- Create quantity_types table
CREATE TABLE quantity_types (
	id SERIAL PRIMARY KEY,
	type VARCHAR(50) NOT NULL
);

-- Create items table
CREATE TABLE items (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	quantity_type_id INTEGER NOT NULL,
	quantity_value DECIMAL(10, 2) NOT NULL,
	bought BOOLEAN DEFAULT FALSE,
	FOREIGN KEY (quantity_type_id) REFERENCES quantity_types(id)
);

ALTER DEFAULT PRIVILEGES GRANT ALL ON FUNCTIONS TO shopperdbuser;