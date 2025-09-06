# Dominote FastAPI backend


### Requirements:

- PostgresSQL should be installed. If you don't have installed on your system there are some scripts that could 
help you

*Linux*

- Install PostgresSql
```sh

    . ./scripts/db_scripts/install_postgres.sh
```

- Database Interations:

Create Databases and tables:

```sh
    . ./scripts/db_scripts/create_db.sh
```

Delete Database and tables
```sh
    . ./scripts/db_scripts/create_db.sh
```

Run on dev
```sh
fastapi dev main.py
```

