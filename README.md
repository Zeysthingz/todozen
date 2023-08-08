#  todozen
This is a task management application based on django,css and boostrap

###  Postgres and PgAdmin
Postgresql is a database management system. It is used to store data.
Pgadmin is a graphical interface for postgres. It is used to manage postgres databases. It is not necessary to use 
pgadmin, but it is recommended.

###  Download and install Postgresql and Pgadmin

PgAdmin: https://www.pgadmin.org/download/

How to create a server in pgadmin: https://www.pgadmin.org/docs/pgadmin4/development/server_dialog.html

postgres: https://www.postgresql.org/download/

### .env file
Create a .env file to reduce share private information like secret key database settings. This file should be  in the
root directory of the project and can include the following  variables:

```
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

