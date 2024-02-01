# Pipestat configuration file specification

All the relevant pieces of information required to initialize the `PipestatManager` object can be provided to the object constructor or as a command line argument in the form of a YAML-formatted **pipestat configuration file**.

```yaml
record_identifier: <unique record identifier for either sample or project-level reporting>
schema_path: <path to the schema>
results_file_path: <path to results file> # either "results_file_path"
database: # or DB login credentials
  name: <database name>
  user: <user name>
  password: <user password>
  host: <database address>
  port: <database port>
  dialect: <database type>
  driver: <python database driver>
```

If both `results_file_path` and DB login credentials are provided, the YAML results file is given priority.

Any of the settings specified in the configuration file, apart from the database login credentials, can be overwritten with the respectively named arguments in the `PipestatManager` object constructor. Therefore, the configuration file is *required* only if the intended pipestat back-end is a database or if using pipestat in tandem with [Looper](https://looper.databio.org/en/dev/pipestat/).

## Example

For the [PostgreSQL](https://www.postgresql.org/) instance has been started in a container, with the following command:

```console
docker run -d
    --name pipestat-postgres \
    -p 5432:5432 \
    -e POSTGRES_PASSWORD=b4fd34f^Fshdwede \
    -e POSTGRES_USER=john \
    -e POSTGRES_DB=pipestat-test \
    -v postgres-data:/var/lib/postgresql/data postgres
```

The configuration file should look like this:

```yaml
schema_path: /path/to/schema.yaml
database:
  name: pipestat-test
  user: john
  password: b4fd34f^Fshdwede
  host: 127.0.0.1
  port: 5432
  dialect: postgresql
  driver: psycopg
```
