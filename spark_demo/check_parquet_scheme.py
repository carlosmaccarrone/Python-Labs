# ================================
# NYC Taxi Sample Demo - Databricks
# ================================
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.getOrCreate()

# Route to the Parquet
parquet_paths = [
    "/Volumes/workspace/default/vol1/output/avg_fare_by_hour.parquet",
    "/Volumes/workspace/default/vol1/output/trips_by_hour.parquet"
]

for path in parquet_paths:
    print(f"\n=== {path} ===")
    df = spark.read.parquet(path)

    # Show detailed diagram
    df.printSchema()

    # Show first rows to spy on column names
    print("Columnas:", df.columns)
    df.show(5, truncate=False)
