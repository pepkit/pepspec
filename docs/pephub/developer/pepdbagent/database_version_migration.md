# 🔧 Database Version Migration and Upgrade Instructions

To change the database version smoothly and seamlessly, we use Alembic.
This tool allows us to manage database schema changes in a consistent, version-controlled manner.
As a result, users who have built their own PEPhub instances can easily upgrade to the latest version without losing 
any data or needing to manually interact with the database.

## 👷 Database schema change - for database developers

If you are changing database schema in `db_utils.py` file and schema in the database changed, you should 
percied with the following steps:

### 0. **Set up the database URL in `alembic.ini`:**

```text
sqlalchemy.url = postgresql+psycopg://user:password@localhost/dbname
```

By default, it is set to testing database. Credentials are in README.md in test folder of the repository.

### 1. **Create a new migration script**: 

When you modify your SQLAlchemy models, follow these steps to keep the database schema in sync:

a. Modify Models: Update your SQLAlchemy models in your code.
b. Generate Migration:
```bash
alembic revision --autogenerate -m "Describe your change"
```

### 2. **Edit the migration script**: 
Open the newly created migration script and edit the `upgrade()` and `downgrade()` functions to define the changes you want to make to the database schema.
- The `upgrade()` function should contain the code to apply the changes.
- The `downgrade()` function should contain the code to revert the changes.

### 3. **Apply the Migration**

Run the migration to apply it to your database. Create small Python script with connection to the database 
with `pepdbagent`, and parameter `run_migrations=True`:

```python
from pepdbagent import PEPDatabaseAgent

db_agent = PEPDatabaseAgent(
   host="localhost",
   port=5432,
   database="pep-db",
   user=None,
   password=None,
   run_migrations=True,
)
```

This will run all migrations of the database, including the one you just created.


### **Version Control**

Each migration script has a unique identifier and tracks schema changes. Always commit these scripts to version control.
   

## 🧙‍♂️ Database schema change - for PEPhub users

If you are changing database schema in `db_utils.py` file and schema in the database changed, you should
run the following script before connecting to the database:

```python
from pepdbagent import PEPDatabaseAgent

db_agent = PEPDatabaseAgent(
   host="localhost",
   port=5432,
   database="pep-db",
   user=None,
   password=None,
   run_migrations=True,
)
```

This will run all migrations of the database, including the one you just created.
