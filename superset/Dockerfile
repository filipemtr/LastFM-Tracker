FROM apache/superset:3.1.1

USER root

RUN pip install --upgrade pip

RUN pip install --no-cache-dir \
    "PyAthena[SQLAlchemy]==2.25.2"

USER superset
