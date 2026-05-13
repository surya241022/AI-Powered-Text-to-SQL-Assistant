from sqlalchemy import create_engine, inspect

# MySQL credentials
username = "root"
password = "surya2410"
host = "localhost"
database = "customer_behavior"

# Create database engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Function to get database schema
def get_schema():

    inspector = inspect(engine)

    schema = ""

    # Get all table names
    tables = inspector.get_table_names()

    # Loop through tables
    for table in tables:

        schema += f"\nTable: {table}\n"

        # Get columns for each table
        columns = inspector.get_columns(table)

        for column in columns:

            schema += f"{column['name']}\n"

    return schema