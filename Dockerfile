FROM apache/airflow:2.11.0-python3.12

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt
