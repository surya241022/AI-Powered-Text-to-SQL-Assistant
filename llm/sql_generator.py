from groq import Groq
from dotenv import load_dotenv
from database.schema_reader import get_schema

import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Function to generate SQL query
# Function to generate SQL query
# Function to generate SQL query
def generate_sql(user_question):

    # Dynamically get schema
    schema = get_schema()

    prompt = f"""
    You are an expert MySQL SQL query generator.

    Database Schema:
    {schema}

    Your task:
    Convert user question into executable MySQL SQL query.

    STRICT RULES:
    - Return ONLY SQL query
    - No explanation
    - No markdown
    - No comments
    - Use ONLY tables and columns present in schema
    - If question cannot be answered using schema, return ONLY:
      NOT_RELEVANT

    User Question:
    {user_question}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Extract response
    sql_query = response.choices[0].message.content

    # Clean response
    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()

    return sql_query