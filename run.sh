if [ ! -f yellow_tripdata_2021-07.csv.gz ]; then
    wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-07.csv.gz
else
    echo "File already exists, skipping download"
fi

gunzip -f yellow_tripdata_2021-07.csv.gz