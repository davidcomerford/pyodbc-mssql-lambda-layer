# pyodbc-mssql-lambda-layer

[![Docker Image CI](https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/actions/workflows/docker-image.yml/badge.svg)](https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/actions/workflows/docker-image.yml)

AWS Lambda layer to connect to SQL Server using PyODBC, UnixODBC and Microsoft ODBC 18 driver for SQL Server.

## Features

- Builds for Python 3.11, 3.12 and 3.13

- Also builds for x86_64 and ARM64

- Microsoft ODBC 18 for SQL Server

- Latest UnixODBC

    I'm pulling the latest version from the Amazon Linux 2023 repository so that'll tick your security boxes.

</br>

## Download Prebuilt Release

https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/releases/latest

</br>

## Or Build Your Own

1. Download the Dockerfile

1. Build image
    ```bash
    docker buildx build --file=Dockerfile.python.3.13 --tag pyodbc-mssql .
    ```
1. Run a temporary container to get the zip file 
    ```bash
    docker run --rm --volume $(pwd):/tmp pyodbc-mssql cp /layer.zip /tmp/
    ```

### Test it locally

Download, unzip and run python from inside a new container.

```bash
unzip layer.zip -d layer-test
cd layer-test
docker run --rm -v $(pwd):/opt -it public.ecr.aws/sam/build-python3.13 python
```

When you add a layer to a function, Lambda extracts the layer contents into the /opt directory in your function’s execution environment. All Lambda runtimes include paths to specific directories within the /opt directory. This gives your function access to your layer content.

We'll simulate this behaviour locally with sys.path.append().

```python
import sys
sys.path.append('/opt/python')
import pyodbc
```

With the pyodbc module loaded, lets connect to a database and run a simple query.

```python
SERVER = 'db.microsoft.com'
USERNAME = 'sa'
PASSWORD = 'M3g@hrtz'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'
conn = pyodbc.connect(connectionString)

SQL_QUERY="""
SELECT @@VERSION
GO
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(r)
```

