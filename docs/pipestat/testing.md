# Testing Configuration

##  Optional Dependencies

Note: to run the pytest suite locally, you will need to install the related requirements:

```bash
cd pipestat

pip install -r requirements/requirements-test.txt

```

## Database Backend Configuration for Tests

Many of the tests require a postgres database to be set up otherwise many of the tests will skip.

We recommend using docker:
```bash
docker run --rm -it --name pipestat_test_db \
    -e POSTGRES_USER=pipestatuser \
    -e POSTGRES_PASSWORD=shgfty^8922138$^! \
    -e POSTGRES_DB=pipestat-test \
    -p 127.0.0.1:5432:5432 \
    postgres
```