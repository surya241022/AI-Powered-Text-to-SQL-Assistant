import streamlit as st

from llm.sql_generator import generate_sql
from database.query_executor import execute_query
from utils.query_validator import validate_query

# Streamlit page config
st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI-Powered SQL Assistant")

st.markdown(
    "Ask questions in natural language and safely query the database."
)

# User input
question = st.text_input(
    "Enter your question:"
)

# Button
if st.button("Generate Answer"):

    if question:

        # Generate SQL query
        try:
            sql_query = generate_sql(question)
        except Exception as e:
            st.error(f"Execution Error: {e}")
            st.stop()

        # Check if question is relevant
        if sql_query == "NOT_RELEVANT":

            st.error(
                "Question is not related to available database tables."
            )

        else:

            # Display generated SQL
            st.subheader("Generated SQL Query")

            st.code(sql_query, language="sql")

            # Validate query safety
            is_valid = validate_query(sql_query)

            if is_valid:

                # Execute SQL query
                results = execute_query(sql_query)

                # Display results
                st.subheader("Query Results")

                st.dataframe(results)

            else:

                st.error(
                    "Unsafe query detected. Query execution blocked."
                )

    else:

        st.warning("Please enter a question.")