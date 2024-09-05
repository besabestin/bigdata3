CREATE USER shopperdbuser WITH PASSWORD 'bgdata3.0';

GRANT ALL ON SCHEMA public TO shopperdbuser;
GRANT USAGE, CREATE ON SCHEMA public to shopperdbuser;

CREATE DATABASE shopperdb;
GRANT ALL PRIVILEGES ON DATABASE shopperdb TO shopperdbuser;
ALTER DATABASE shopperdb OWNER TO shopperdbuser;

\c shopperdb shopperdbuser;

ALTER DEFAULT PRIVILEGES GRANT ALL ON TABLES TO shopperdbuser;
ALTER DEFAULT PRIVILEGES GRANT ALL ON SEQUENCES TO shopperdbuser;
ALTER DEFAULT PRIVILEGES GRANT ALL ON FUNCTIONS TO shopperdbuser;
