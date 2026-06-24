# Uber-End-to-End-Ride-Streaming-Project-EventHub

<img width="1226" height="687" alt="image" src="https://github.com/user-attachments/assets/a1b6299f-0068-4923-a86c-8cd1ece38942" />

## Overview


This project demonstrates a complete end-to-end Data Engineering solution built on Azure and Databricks. The pipeline ingests real-time ride events, processes streaming data using PySpark Structured Streaming, applies Slowly Changing Dimension (SCD Type 2) logic, and builds analytical datasets using a Medallion Architecture.

## Architecture

Source → Azure Event Hub → Azure Data Factory → Azure Data Lake Storage → Databricks Structured Streaming → Bronze Layer → Silver Layer → Gold Layer → Analytics & KPI Views

## Tech Stack

* Azure Event Hub
* Azure Data Factory
* Azure Data Lake Storage Gen2
* Azure Databricks
* PySpark
* Spark Structured Streaming
* Delta Lake
* Unity Catalog
* GitHub
* Python

## Project Components

### Real-Time Data Generation

* Python-based ride event simulator
* Faker library used for synthetic ride generation
* Events published to Azure Event Hub

### Data Ingestion

* Azure Data Factory pipelines ingest static mapping files data into Data Lake Storage
* Metadata-driven ingestion framework

### Bronze Layer

* Raw streaming events captured from Event Hub
* Incremental ingestion using Structured Streaming using SDP

### Silver Layer

* Data cleansing and validation
* Business rule implementation
* Deduplication and standardization

### Gold Layer

* Star Schema implementation
* Fact and Dimension tables

## Slowly Changing Dimensions (SCD Type 2)

Implemented SCD Type 1&2 using spark declarative pipelines

* DimCustomers
* DimDrivers
* DimLocations
* DimPayments
* DimVehicles

## Data Model
Star Schema Data Modelling

### Fact Table

* Fact

### Dimension Tables

* DimBookings
* DimDrivers
* DimLocations
* DimVehicles
* DimPayments

## Key Features

* Real-Time Streaming Pipeline
* Metadata-Driven Processing
* Medallion Architecture
* Delta Lake Storage
* Unity Catalog Governance
* SCD Type 2 Implementation
* Star Schema Modeling

## Repository Structure

```text
Architecture/
Data/
databrick/
Screenshots/
README.md
```

## Future Enhancements

* Power BI Dashboard Integration
* CI/CD using GitHub Actions
* Data Quality Framework
* Monitoring & Alerting
* Automated Deployment Pipelines

## Author

Ayesha Shaik

Azure Data Engineer | Databricks | PySpark | dbt | Azure Data Factory

<img width="1226" height="687" alt="image" src="https://github.com/user-attachments/assets/397288ce-10f6-4abc-adb4-5055d8849317" />

