""" 
    Рекомендации по выполнению домашнего задания
"""

def get_raw_data_from_tm_and_save_to_s3(url: str, dt: str, filename: str) -> None:
   """ Reads data from API and saves it to S3 """

   data = requests.get(url)
   if data.status_code == 200:
        # <ToDo>
   else:
       logging.error(f"Couldn't load data from URL {url}")

def get_data_from_s3(key: str) -> dict:
   """Read data from S3"""
   logging.info(f"Start loading {key}")

   # <ToDo>

   logging.info(f"File {key} loaded")   
   return data

def save_data_to_parquet_s3(dataf: pd.DataFrame, dt: str, filename: str) -> None:
   
   table = pyarrow.Table.from_pandas(df=dataf)
   buf = BytesIO()

   # <ToDo>

   obj.put(Body=buf.getvalue())

def filter_objects_by_prefix_in_s3_bucket(key_prefix: str, bucket_name: str) -> set:

  # <ToDo>
   return set(objects)


# Загрузку в parquet тоже рекомендуется выполнить в виде функций.
