FROM python:3.12.8

# Install required packages
RUN pip install pandas sqlalchemy psycopg2 

WORKDIR /app

COPY ingest.py .
COPY data/yellow_tripdata_2021-07.csv data/yellow_tripdata_2021-07.csv

ENTRYPOINT [ "python", "ingest.py" ]