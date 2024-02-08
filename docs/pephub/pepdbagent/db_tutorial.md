# Database setup

### container installation: 


0) Go to [pep_db](../pep_db)  directory and then run the following lines
1) Build the docker: `docker build -t pep-db ./`
2) Run the docker: `docker run --name pep-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=docker -p 5432:5432 -d pep-db`
3) Start it: `docker start pep-db`

Now db is installed

### How to connect to the docker:

`docker exec -it 65f bash`

`psql -U postgres -d pep-db`

---
If you have your own database, you can initialize a connection using pepdbagent. 
The pepdbagent will create a new database schema if it doesn't already exist, or throw an exception if the schema is incorrect.