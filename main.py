import pandas as pd

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://prometheus:12345@0.0.0.0:3306/data_vector"

df = pd.read_sql_table('coordenadas', SQLALCHEMY_DATABASE_URL)
print(df.shape)
