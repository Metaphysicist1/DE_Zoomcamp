from sqlalchemy import create_engine
import pandas as pd
from time import time
import os
import argparse


# engine = create_engine('postgresql://root:root@0.0.0.0:5431/ny_taxi')

# print(pd.io.sql.get_schema(data,name='ny_taxi_table', con=engine))



# df_iter = pd.read_csv('../data/yellow_tripdata_2021-07.csv', iterator=True, chunksize=100000)




def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table_name
    url = params.url

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    
    
    df_iter = pd.read_csv(f'{os.getcwd()}/data/yellow_tripdata_2021-07.csv', iterator=True, chunksize=100000)

    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datatime = pd.to_datetime(df.tpep_dropoff_datetime)


    # df.head(n=0).to_sql('ny_taxi_table', engine, if_exists='replace',index=False)

    df.to_sql(name=table, con=engine, if_exists='append', index=False)

    n = 0
    while True:
        try:
        
            time_start = time()
            df = next(df_iter)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datatime = pd.to_datetime(df.tpep_dropoff_datetime)
            
            df.to_sql('ny_taxi_table', con=engine, if_exists='append', index=False)

            time_end = time()

            print(f"Inserted chunk {n} : ,{time_end - time_start} ")
            n += 1

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
    



