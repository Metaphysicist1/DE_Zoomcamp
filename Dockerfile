FROM python:3.10

RUN pip install pandas


WORKDIR /app

COPY scripts/eda.ipynb .

CMD ["python", "eda.ipynb"]