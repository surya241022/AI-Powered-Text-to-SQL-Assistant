from sqlalchemy import create_engine
import pandas as pd

# MySQL credentials
username = "root"
password = "surya2410"
host = "localhost"
database = "customer_behavior"

# Create database engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Function to execute SQL query
def execute_query(sql_query):

    try:
        df = pd.read_sql(sql_query, engine)

        return df

    except Exception as e:
        return f"Error: {e}"