from sqlalchemy import create_engine
import pandas as pd

# MySQL credentials
username = "root"
password = "surya2410"
host = "localhost"
database = "customer_behavior"

# Create connection engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# SQL query
query = "SELECT * FROM customer"

# Execute query and store results
df = pd.read_sql(query, engine)

# Display output
print(df)