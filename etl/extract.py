from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Sales_ETL").getOrCreate()

def extract():
    file_path = "Files/sales_messy.csv"
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df