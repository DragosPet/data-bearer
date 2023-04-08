# data-bearer

Small CLI for interacting with different database services.

Supported database engines : 
- Postgres (Connection type : POSTGRESQL)
- Sqlite (Connection type : SQLITE)

### Changelog

- v 0.1.1 - Added support for MySQL connector and redirecting logs to files
- v 0.1.0 - inital functionality added

# Build and installation

Project is maintained through `poetry`. To build it, it's enough to run : 

```bash
poetry build 
```

Then install the local package through Wheel :

```bash
export VERSION=$(poetry version -s)
pip install dist/data_bearer-$VERSION-py3-none-any.whl
```

# Usage

Package assumes that in the structure of the working directory, there is a SQL directory avaialble in which the desired queries are available for execution.

Also, a `run_config.yaml` file that stores the required DB properties is needed in the working directory, for running the queries.

To populate the configuration yaml, you can either input manually all connection properties required by each supported database, or use the `bearer-init-config` command which will walk you through it iteratively.

```bash
[poetry run] bearer-init-config

---------------------------------------------------
--------------------DATA BEARER--------------------
---------------------------------------------------

Starting configuration of client!
Input working directory (where to store the db config) :
.
Input Connection TYPE ([POSTGRES/SQLITE]) :
POSTGRES
Replace Existing Config (if any) ? :
Y
Input Database Host (if necessary) :

Input Database Port (if necessary) :

Input Database User (if necessary) :

Input Database Password (if necessary) :

Input Target Database (if sqlite, path to db) :

Input desired Logging level ([INFO/WARN/ERROR]) :

Redirect logs to files ? (y/n) :

Config already exists.
Replace flag is marked as Y. Replacing config.
Exporting config : dict_keys(['DB_HOST', 'CONNECTION_TYPE', 'DB_PORT', 'DB_USERNAME', 'DB_PASSWORD', 'DB_DATABASE','LOG_LEVEL','USE_FILES','LOGS_PATH'])
Creating local state storage
All set !

---------------------------------------------------
--------------------DATA BEARER--------------------
---------------------------------------------------
```

After configuration is established in the working directory, to run any sql query from the `sql/` path, command `bearer-run-sql` should be used. This supports 2 execution modes, interactive (by specifying some run options during the execution), or shell which will require specifying all command options.

```bash
[poetry run] bearer-run-sql --help
usage: bearer-run-sql [-h] -w WORKDIR -i {y,n} [-ep EXPORT_PATH] [-sn SQL_FILE_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -w WORKDIR, --workdir WORKDIR
                        Workdir path for storing and reading the state config and sql files.
  -i {y,n}, --interactive {y,n}
                        Interactive Execution, allowing sql file discovery and execution
  -ep EXPORT_PATH, --export_path EXPORT_PATH
                        Export path for the provided data.
  -sn SQL_FILE_NAME, --sql_file_name SQL_FILE_NAME
                        SQL File that would be executed.
```

# Testing

Unit tests should be executed through `pytest`. Linting and formatting should be applied before pushing to repo.

# Contributing

If you wish to contribute to the project, don't hesitate to open an issue/comment on available issues. Every change should be done through pull requests and code review. 



