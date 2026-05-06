def load(df):
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/spark") \
        .option("dbtable", "public.clean_sales") \
        .option("user", "owais") \
        .option("password", "owais7383") \
        .option("driver", "org.postgresql.Driver") \
        .mode("write") \
        .save()