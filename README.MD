# 🎵 Last.fm Lakehouse Analytics Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![PySpark](https://img.shields.io/badge/PySpark-Distributed%20Processing-orange?style=for-the-badge\&logo=apachespark)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-red?style=for-the-badge\&logo=apacheairflow)
![Databricks](https://img.shields.io/badge/Databricks-Data%20Platform-red?style=for-the-badge\&logo=databricks)
![AWS](https://img.shields.io/badge/AWS-Cloud-black?style=for-the-badge\&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge\&logo=docker)
![Superset](https://img.shields.io/badge/Apache%20Superset-BI%20Dashboard-green?style=for-the-badge)

### End-to-End Modern Data Engineering Pipeline using Lakehouse Architecture

</div>

---

# 📌 Overview

This project is a complete end-to-end Data Engineering platform built around a modern **Lakehouse Architecture** using the **Medallion Design Pattern (Bronze / Silver / Gold)**.

The pipeline consumes real-time music analytics data from the Last.fm API, orchestrates data ingestion and transformations through Apache Airflow, processes distributed workloads with PySpark on Databricks, stores data in AWS S3, exposes analytical datasets through AWS Athena, and visualizes insights using Apache Superset.

The entire infrastructure is fully containerized with Docker and designed following modern data engineering best practices.

---

# 🏗️ Architecture

```text
                           ┌────────────────────┐
                           │    Last.fm API     │
                           └─────────┬──────────┘
                                     │
                                     ▼
                      ┌─────────────────────────┐
                      │   Apache Airflow DAG    │
                      │  (Orchestration Layer)  │
                      └─────────┬───────────────┘
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
        ┌────────────────┐           ┌──────────────────┐
        │ Bronze Layer   │           │ Error Handling & │
        │ Raw JSON Data  │           │ Retry Policies   │
        │ AWS S3         │           └──────────────────┘
        └──────┬─────────┘
               │
               ▼
     ┌──────────────────────┐
     │ Databricks + PySpark │
     │ Distributed ETL/ELT  │
     └─────────┬────────────┘
               │
               ▼
       ┌─────────────────┐
       │ Silver Layer    │
       │ Cleaned Data    │
       │ Standardization │
       └──────┬──────────┘
              │
              ▼
       ┌─────────────────┐
       │ Gold Layer      │
       │ Star Schema     │
       │ Fact Tables     │
       │ Dimensions      │
       └──────┬──────────┘
              │
              ▼
       ┌─────────────────┐
       │ AWS Athena      │
       │ Query Engine    │
       └──────┬──────────┘
              │
              ▼
       ┌─────────────────┐
       │ Apache Superset │
       │ BI Dashboards   │
       └─────────────────┘
```

---

# ⚡ Core Technologies

| Category               | Technology              |
| ---------------------- | ----------------------- |
| Orchestration          | Apache Airflow          |
| Distributed Processing | PySpark                 |
| Cloud Storage          | AWS S3                  |
| Query Engine           | AWS Athena              |
| Data Platform          | Databricks              |
| Containerization       | Docker & Docker Compose |
| BI / Analytics         | Apache Superset         |
| Data Modeling          | Star Schema             |
| Architecture           | Lakehouse + Medallion   |
| Language               | Python                  |
| Data Format            | Parquet                 |

---

# 🧠 Engineering Concepts Applied

## ✅ Medallion Architecture

### Bronze Layer

* Raw API ingestion
* Immutable storage
* Historical persistence
* Original payload preservation

### Silver Layer

* Data cleansing
* Schema standardization
* Null handling
* Type casting
* Deduplication
* Transformation logic

### Gold Layer

* Analytical modeling
* Star Schema implementation
* Fact and dimension separation
* BI optimized datasets
* High-performance analytical queries

---

# 📊 Star Schema Design

## Fact Tables

### fact_global_tracks

Stores global music metrics.

### fact_country_tracks

Stores country-based listening metrics.

### fact_global_artists

Stores artist performance analytics.

---

## Dimension Tables

### dim_tracks

Track metadata and identifiers.

### dim_artists

Artist metadata.

### dim_country

Country normalization layer.

### dim_genres

Genre categorization.

---

# 🔄 Data Pipeline Workflow

## 1. API Consumption

The pipeline extracts data from the Last.fm public API.

Collected datasets include:

* Top global tracks
* Top global artists
* Top genres
* Country-based track rankings
* Country-based artist rankings

---

## 2. Orchestration with Airflow

Apache Airflow is responsible for:

* Scheduling DAG executions
* Managing dependencies
* Triggering Databricks jobs
* Monitoring execution states
* Handling retries and failures
* Centralized pipeline orchestration

### Features Implemented

* Retry policies
* Failure resilience
* Task dependency management
* Parameterized workflows
* Modular DAG structure

---

## 3. Distributed Processing with PySpark

PySpark transformations are executed inside Databricks.

Processing includes:

* Cleaning corrupted records
* Schema normalization
* Joins between datasets
* Analytical transformations
* Star schema generation
* Aggregations and enrichments

---

# ☁️ AWS Infrastructure

## Amazon S3

Acts as the centralized Data Lake.

### Storage Layers

```text
s3://lastfm-tracker/bronze/
s3://lastfm-tracker/silver/
s3://lastfm-tracker/gold_layer/
```


# 📈 Business Intelligence Layer

## Apache Superset

The BI layer connects directly to Athena.

### Dashboard Features

* Auto-refresh analytics
* Interactive visualizations
* Country filters
* Artist ranking dashboards
* Music trend analysis
* KPI tracking
* Time-based metrics

# 📂 Project Structure

```text
lastfm-tracker/
│
├── dags/
│
├── logs/
│
├── public/
│
├── src/
│
├── superset/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Pipeline Highlights

## ✔ End-to-End Automation

Fully automated extraction, transformation, modeling, and visualization pipeline.

## ✔ Scalable Lakehouse Architecture

Designed using modern scalable data engineering principles.

## ✔ Distributed Processing

PySpark enables scalable large-volume transformations.

## ✔ Analytics-Ready Data Modeling

Star schema optimized for BI workloads.

## ✔ Real-Time Dashboard Updates

Dashboards automatically reflect newly ingested data.

## ✔ Production-Oriented Design

Includes orchestration, retries, error handling, and modularization.

# 📸 Dashboard Preview

```text
Examples:

• Top Artists by Country
• Most Streamed Global Tracks
• Genre Popularity Analysis
• Country Listening Trends
• Artist Ranking Evolution
• Interactive Filters & Drilldowns
```


# 👨‍💻 Author

Developed as a complete modern Data Engineering portfolio project focused on scalable analytics architecture, orchestration, distributed computing, and business intelligence.

---

<div align="center">

### 🚀 Modern Data Engineering • Lakehouse • Distributed Analytics

</div>
