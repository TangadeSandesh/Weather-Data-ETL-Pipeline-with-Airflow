# Twitter ETL Pipeline

A data pipeline that extracts tweets from Elon Musk's Twitter profile, transforms the data into a structured format, and loads it into Amazon S3.

## Overview

This project uses Apache Airflow to schedule and run a daily ETL (Extract, Transform, Load) pipeline that:

1. Extracts the latest tweets from Elon Musk's Twitter profile using the Twitter API
2. Transforms the data by selecting relevant fields and formatting them appropriately
3. Loads the data into an Amazon S3 bucket for storage and further analysis

## Prerequisites

- Python 3.7+
- Apache Airflow
- AWS account with S3 access
- Twitter API Bearer Token

## Required Python Packages

- tweepy
- pandas
- python-dotenv
- apache-airflow
- apache-airflow-providers-amazon

## Project Structure

```
twitter-etl-project/
├── dags/
│   ├── twitter_dag.py
│   └── twitter_etl.py
├── .env
└── README.md
```

## Setup Instructions

1. Clone this repository:
   ```
   git clone <repository-url>
   cd twitter-etl-project
   ```

2. Create a `.env` file in the project root directory with your Twitter API credentials:
   ```
   BEARER_TOKEN=your_twitter_bearer_token
   ```

3. Configure AWS credentials in Airflow:
   - Create an AWS connection in Airflow named "aws_default"
   - Add your AWS access key, secret key, and region

4. Create an S3 bucket named "sandesh-twitter-bucket" (or modify the code to use your bucket name)

5. Install the required Python packages:
   ```
   pip install tweepy pandas python-dotenv apache-airflow apache-airflow-providers-amazon
   ```

## How It Works

### twitter_etl.py

This file contains the main ETL function `run_twitter_etl()` which:
- Connects to the Twitter API using the bearer token
- Retrieves Elon Musk's user ID
- Fetches the 10 most recent tweets with metadata (creation date, like count, retweet count)
- Transforms the data into a pandas DataFrame
- Saves the data as a CSV file locally
- Uploads the CSV file to the specified S3 bucket

### twitter_dag.py

This file defines the Airflow DAG that:
- Runs once per day
- Executes the ETL function defined in twitter_etl.py
- Includes retry logic for handling failures

## Usage

1. Place the DAG files in your Airflow DAGs folder
2. Enable the DAG in the Airflow UI
3. The pipeline will run automatically based on the schedule (daily)

## Monitoring

You can monitor the pipeline execution in the Airflow UI:
- Check task logs for detailed execution information
- Verify S3 bucket contents to ensure data is being uploaded correctly

## Extending the Project

Potential enhancements:
- Add data quality checks
- Implement error notifications
- Expand to track multiple Twitter accounts
- Add data visualization layer
- Implement data partitioning in S3
