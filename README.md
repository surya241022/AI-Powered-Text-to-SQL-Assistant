# 🤖 AI-Powered Text-to-SQL Assistant

A modern, intelligent Streamlit application that allows users to query a MySQL database using natural language. The system dynamically reads the database schema, constructs appropriate prompts for a Large Language Model (Groq / Llama 3.1 8B), generates safe SQL queries, validates them to prevent destructive operations, and displays results in an interactive interface.

---

## 🌟 Key Features

*   **Natural Language to SQL**: Ask questions in plain English (e.g., *"Show all customers who spent more than $100"*), and get execution-ready MySQL queries.
*   **Dynamic Schema Integration**: Automatically reads the MySQL database schema (tables and columns) and injects it into the LLM context to ensure high SQL accuracy.
*   **Query Safety & Validation**: Built-in query validator blocks dangerous SQL keywords like `DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `TRUNCATE`, and `CREATE` to ensure read-only safety.
*   **Modern Web UI**: A beautiful, interactive dashboard built using Streamlit that displays the generated SQL side-by-side with execution results.
*   **Groq API Integration**: Powered by the ultra-fast `llama-3.1-8b-instant` model on Groq.

---

## 🏗️ Architecture & Project Structure

The project is structured modularly to separate database logic, LLM generation, utilities, and UI layout:

```text
├── database/
│   ├── database_connection.py   # Establishes SQLAlchemy connection engine
│   ├── query_executor.py        # Safely executes read-only SQL queries via pandas
│   └── schema_reader.py         # Inspects database dynamically to fetch schema details
├── llm/
│   └── sql_generator.py         # Interfaces with Groq API to convert text to SQL
├── utils/
│   └── query_validator.py       # Validates generated queries against write/drop operations
├── app.py                       # Main Streamlit web application
├── requirements.txt             # Minimal setup requirements
└── README.md                    # Project documentation (this file)
```

---

## 🛠️ Prerequisites & Installation

### 1. Database Setup
Ensure you have **MySQL** running on your local machine.
1. Create a database named `customer_behavior`.
2. Ensure you have a `customer` table (or similar tables matching your query targets).
3. If necessary, configure your credentials in `database/database_connection.py`, `database/query_executor.py`, and `database/schema_reader.py` (Default: User `root`, Pass `surya2410`, Host `localhost`).

### 2. Clone and Setup Environment
Clone the repository:
```bash
git clone https://github.com/surya241022/AI-Powered-Text-to-SQL-Assistant.git
cd AI-Powered-Text-to-SQL-Assistant
```

Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Install Dependencies
Install the required packages:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

Launch the Streamlit interface:
```bash
streamlit run app.py
```

Open the local URL displayed in the terminal (typically `http://localhost:8501`) in your browser to interact with the assistant.

---

## 🔒 Security Measures

To protect the underlying database:
1. **Read-Only Restriction**: The executor is intended only for querying data.
2. **Keyword Blocking**: Any query containing destructive commands (e.g. `DROP`, `DELETE`, `UPDATE`) is immediately flagged and execution is aborted.
3. **LLM System Prompt Constraints**: The LLM is explicitly instructed to only construct queries using columns/tables present in the active schema, rejecting irrelevant requests with a `NOT_RELEVANT` signal.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
