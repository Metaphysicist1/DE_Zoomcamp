FROM python:3.10

RUN pip install pandas

WORKDIR /app

COPY scripts/pipeline.py .

CMD ["python", "pipeline.py"]