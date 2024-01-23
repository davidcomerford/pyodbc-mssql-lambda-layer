# pyodbc-mssql-lambda-layer

[![Docker Image CI](https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/actions/workflows/docker-image.yml/badge.svg)](https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/actions/workflows/docker-image.yml)

AWS Lambda layer to connect to SQL Server using PyODBC, UnixODBC and Microsoft ODBC 18 driver for SQL Server.

## Features

- Builds for Python 3.11 and 3.12

- Builds for x86_64 and ARM64

- Microsoft ODBC 18 for SQL Server

- Latest UnixODBC

    I'm pulling the latest version from the Amazon Linux 2023 repository so that'll tick your security boxes.


<br>

## Download Prebuilt Release

https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/releases/latest

<br>

## Or Build Your Own

1. Download the Dockerfile

1. Build image
    ```bash
    docker buildx build --file=Dockerfile.python.3.12 --tag pyodbc-mssql .
    ```
1. Run a temporary container to get the zip file 
    ```bash
    docker run --rm --volume $(pwd):/tmp pyodbc-mssql cp /layer.zip /tmp/
    ```

### Test it

Download, unzip and run docker container

```bash
unzip layer.zip -d layer-test
cd layer-test
docker run --rm -v $(pwd):/opt -it public.ecr.aws/sam/build-python3.12 python
```

Import library

```python
import sys
sys.path.append('/opt/python')
import pyodbc
```

