FROM python:3.10

RUN pip install pandas

WORKDIR /app

COPY . .

CMD ["python", "scripts/pipeline.py"]