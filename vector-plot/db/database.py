import pandas as pd

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://prometheus:12345@0.0.0.0:3306/data_vector"

def get_coordenadas():
    return pd.read_sql_table('coordenadas', SQLALCHEMY_DATABASE_URL)
def get_magnitude():
    return pd.read_sql_table('magnitude', SQLALCHEMY_DATABASE_URL)