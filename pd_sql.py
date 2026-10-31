from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
url=os.getenv("URL")

engine = create_engine(url,max_overflow=10, pool_size=10, pool_timeout=10)
# e2 = create_engine(url,connect_args)
df = pd.read_sql("select * from sample",engine,chunksize=1)
final_df = pd.concat(df, ignore_index=True)

for chunk in df:
    print(chunk)


#    id       name
# 0   2  Yash Teki
#    id     name
# 0   3  someone