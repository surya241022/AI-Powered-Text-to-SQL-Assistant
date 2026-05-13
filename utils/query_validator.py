# Function to validate SQL query

def validate_query(sql_query):

    # Convert query to uppercase
    query = sql_query.upper()

    # Dangerous SQL keywords
    blocked_keywords = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE"
    ]

    # Check for blocked keywords
    for keyword in blocked_keywords:

        if keyword in query:
            return False

    return True