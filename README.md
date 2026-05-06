# 🚀 First Spark Project — Sales Data ETL Pipeline

A beginner-friendly Data Engineering project built using Apache Spark and PySpark.
This project demonstrates how to build a simple ETL (Extract, Transform, Load) pipeline for cleaning and processing sales data.

---

# 📌 Project Overview

This is my **first Spark project** where I learned:

* How Spark reads CSV files
* Data cleaning and transformation
* Handling missing values and duplicates
* Basic ETL pipeline structure
* Aggregating sales data using Spark DataFrames

The goal of this project is to understand the fundamentals of Data Engineering workflows using Spark.

---

# 🧠 What I Learned

✅ SparkSession creation
✅ Reading CSV files with PySpark
✅ Data cleaning techniques
✅ Working with Spark DataFrames
✅ GroupBy and aggregation
✅ ETL pipeline thinking
✅ Writing clean modular code

---

# ⚙️ Technologies Used

* Python
* Apache Spark (PySpark)
* PostgreSQL (optional)
* CSV Files

---

# 📂 Project Structure

```text
Sales-Data-ETL-Pipeline/
│
├── app.py
│
├── Files/
│   └── sales_messy.csv
│
├── Output/
│   └── cleaned_sales/
│
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
└── README.md
```

---

# 🔄 ETL Workflow

## 1️⃣ Extract

Read raw sales CSV data using Spark.

```python
df = spark.read.csv(
    "Files/sales_messy.csv",
    header=True,
    inferSchema=True
)
```

---

## 2️⃣ Transform

Data cleaning and processing:

* Handle missing values
* Remove duplicates
* Convert columns to correct data types
* Format date columns

Example:

```python
df = df.dropDuplicates()
```

---

## 3️⃣ Load

Store cleaned data:

* CSV Output
* PostgreSQL Table (optional)

Example:

```python
df.write.mode("overwrite").csv("Output/")
```

---

# 📊 Example Features

✔ Remove null values
✔ Fix invalid numeric data
✔ Convert date columns
✔ Calculate total sales per product
✔ Save cleaned dataset

---

# 🔥 Sample Aggregation

```python
from pyspark.sql.functions import sum

df_grouped = df.groupBy("product") \
               .agg(sum("amount").alias("total_sales"))

df_grouped.show()
```

---

# ▶️ How to Run

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Linux/Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 2️⃣ Install Dependencies

```bash
pip install pyspark pandas
```

---

## 3️⃣ Run the Project

```bash
python app.py
```

---

# 📈 Example Output

```text
+-----------+-----------+
| product   | total_sales |
+-----------+-----------+
| Laptop    | 3200      |
| Phone     | 1600      |
+-----------+-----------+
```

---

# 🎯 Why I Built This Project

I built this project to practice:

* Data Engineering fundamentals
* Spark DataFrame operations
* ETL pipeline development
* Real-world data cleaning workflow

This project helped me understand how industry ETL systems process messy data into clean and usable datasets.

---

# 👨‍💻 Author

Owais Ahmad
