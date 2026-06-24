# Databricks notebook source
import pandas as pd

df = pd.read_json('https://datalakeuberprojectaysh.blob.core.windows.net/raw/ingestion/map_cities.json?sp=r&AZZOk%3D')

df_spark = spark.createDataFrame(df)
display(df_spark)

# COMMAND ----------

# DBTITLE 1,Cell 1
import pandas as pd

files = [
{"file": "map_cities"},
{"file":"map_cancellation_reasons"},
{"file":"map_payment_methods"},
{"file":"map_ride_statuses"},
{"file":"map_vehicle_makes"},
{"file":"map_vehicle_types"}
]
 
for file in files:

    url = f'https://datalakeuberprojectaysh.blob.core.windows.net/raw/ingestion/{file["file"]}.json?sp=xAZZOk%3D'

    df_ = pd.read_json(url)
    df_spark = spark.createDataFrame(df_)
    
    #writing data to bronze layer
    df_spark.write.format("delta")\
            .mode("overwrite")\
            .option('overwriteSchema','true')\
            .saveAsTable(f"uber.bronze.{file['file']}")

# COMMAND ----------

import pandas as pd
url = 'https://datalakeuberprojectaysh.blob.core.windows.net/raw/ingestion/bulk_rides.json?sp=r&st=2026-06-22T13:59:01Z&se=2026-06-28T10:14:01Z&spr=https&sv=2026-02-06&sr=c&sig=gAg6Yn%2FAmUy54wfXAT1QuqlIwJYiqpT%2BgAreWxAZZOk%3D'

df = pd.read_json(url)
df_spark = spark.createDataFrame(df)
if not spark.catalog.tableExists("uber.bronze.bulk_rides"):
    df_spark.write.format("delta")\
                .mode("overwrite")\
                .saveAsTable("uber.bronze.bulk_rides")
print("This will not run more than once since its only for initial load of data because its history")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from uber.bronze.map_cities

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from uber.bronze.rides_raw

# COMMAND ----------

