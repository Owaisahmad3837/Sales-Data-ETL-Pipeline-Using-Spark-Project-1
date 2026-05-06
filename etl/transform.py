from pyspark.sql.functions import col, to_date

def transform(df):

    df = df.fillna({"product": "Missing"})

    df = df.withColumn("amount", col("amount").cast("double"))
    median=df.approxQuantile("amount",[0.5],0.01)[0]
    df=df.fillna({"amount":median})
    
    df = df.withColumn("quantity", col("quantity").cast("double"))

    df = df.fillna({"quantity": 1})

    df = df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

    df = df.dropna(subset=["order_id", "product"])

    df = df.dropDuplicates()

    return df