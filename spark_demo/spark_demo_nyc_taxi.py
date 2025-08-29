# ================================
# NYC Taxi Sample Demo - Databricks
# ================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, hour

# Create or take existing SparkSession
spark = SparkSession.builder.getOrCreate()

# Route to the uploaded CSV
file_path = "/Workspace/Repos/carlosmaccarrone/Python-Labs/spark_demo/nyc_taxi_sample_10k.csv"

# Read CSV with header and infer types
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show first rows
df.show(5)
df.printSchema()

# --------------------------------
# Prepare data
# --------------------------------
# Add pickup time column
df = df.withColumn("hour", hour(col("tpep_pickup_datetime")))

# --------------------------------
# Analysis
# --------------------------------
# 1 Average hourly rate
avg_fare_by_hour = df.groupBy("hour").agg(avg("total_amount").alias("avg_fare"))
print("\nAverage hourly rate:")
avg_fare_by_hour.show(10)

# 2 Number of trips per hour
trips_by_hour = df.groupBy("hour").agg(count("*").alias("num_trips"))
print("\nNumber of trips per hour:")
trips_by_hour.show(10)

# 3 Top 5 longest trips
print("\nTop 5 longest trips:")
df.orderBy(col("trip_distance").desc()).show(5)

# --------------------------------
# Save results (optional)
# --------------------------------
avg_fare_by_hour.write.mode("overwrite").parquet("/FileStore/tables/output/avg_fare_by_hour.parquet")
trips_by_hour.write.mode("overwrite").parquet("/FileStore/tables/output/trips_by_hour.parquet")

print("\n✅ Demo completed. Results saved in /FileStore/tables/output/")
