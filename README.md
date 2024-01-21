# pyodbc-mssql-lambda-layer

[![Docker Image CI](https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/actions/workflows/docker-image.yml/badge.svg)](https://github.com/davidcomerford/pyodbc-mssql-lambda-layer/actions/workflows/docker-image.yml)

AWS Lambda layer to connect to SQL Server using PyODBC, UnixODBC and Microsoft ODBC 18 driver for SQL Server.

## Features 

- Python 3.12

- Microsoft ODBC 18 for SQL Server

- Latest UnixODBC

    I'm pulling the latest version from the Amazon Linux 2023 repository so that'll tick your security boxes.

# Download


# Build your own

1. Download the Dockerfile

1. Build image
    ```bash
    docker build --no-cache -t mssql-lambda .
    ```
1. Run a temporary container to get the zip file 
    ```bash
    docker run --rm --volume $(pwd):/tmp mssql-lambda cp /layer.zip /tmp/
    ```

## Test it
unzip layer.zip -d layer-test
cd layer-test
docker run --rm -v $(pwd):/opt -it amazonlinux /bin/bash

