# HS_samples
A little bit of everything, using hearthstone game data.

This repo is brand new and is being developed and improved little by little.

### Plans:
- Create routine for downloading data files from Hearthscry
- Manage merging of the files with duplicate data, transition between moving files between extract, processing and backup directories
- Parse files into record-by-record JSON records and publish them into messaging tools (Kafka/Pubsub/Kinesis)
- Create consumers for Kafka/Pubsub/Kinesis and move the data into all sorts of databases (MongoDB/Hive/Redshift/BigQuery)
- Create batch jobs for ETL processes on the raw data from the forementioned databases (SQL/Spark/Map Reduce)
- Create scheduled events for batch jobs on the databases mentioned above (Airflow/Oozie/Luigi)
- Create consumer for moving data into NoSql databases (HBase/Cassandra/DynamoDB/BigTable), creating several types of different random-access events
- Create unified solution for querying multiple sources using Presto
- Use Docker and Kubernetes for containerization of all the technologies mentioned above.
- Cleanup of all unnecessary files and notes. Commentary in all of the code. Creation of generic functions and scripts for doing similar tasks. Creation of configuration files to facilitate customization. Etc.

### Future plans:
- Statistical Analysis
- Machine learning
- Deep learning
