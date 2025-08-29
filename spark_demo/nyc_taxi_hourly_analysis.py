# ================================
# NYC Taxi Sample Demo - Databricks
# ================================
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# Iniciar Spark
spark = SparkSession.builder.getOrCreate()

# Paths a tus parquet
avg_fare_path = "/Volumes/workspace/default/vol1/output/avg_fare_by_hour.parquet"
trips_path = "/Volumes/workspace/default/vol1/output/trips_by_hour.parquet"

# Leer los Parquet
avg_fare_df = spark.read.parquet(avg_fare_path)
trips_df = spark.read.parquet(trips_path)

# Pasar a Pandas para graficar
avg_fare_pd = avg_fare_df.toPandas()
trips_pd = trips_df.toPandas()

# Ordenar por hora si no lo está
avg_fare_pd = avg_fare_pd.sort_values(by="hour")
trips_pd = trips_pd.sort_values(by="hour")

# Gráfico 1: tarifa promedio por hora
plt.figure(figsize=(10,5))
plt.plot(avg_fare_pd["hour"], avg_fare_pd["avg_fare"], marker="o")
plt.title("Average Fare by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Fare ($)")
plt.grid(True)
plt.show()

# Gráfico 2: cantidad de viajes por hora
plt.figure(figsize=(10,5))
plt.bar(trips_pd["hour"], trips_pd["num_trips"])
plt.title("Number of Trips by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Trips")
plt.grid(axis="y")
plt.show()
