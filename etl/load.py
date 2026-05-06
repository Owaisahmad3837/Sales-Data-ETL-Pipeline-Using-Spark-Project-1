import os
def load(df):
    os.makedirs("Output",exist_ok=True)
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/spark") \
        .option("dbtable", "public.clean_sales") \
        .option("user", "owais") \
        .option("password", "owais7383") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()
    
    df.write.mode("overwrite").option("header",True).csv("Output/clean_sales.csv")