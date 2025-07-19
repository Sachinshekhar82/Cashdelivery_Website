# backend/init_db.py
import sqlite3

DATABASE = 'cashdash.db'
SCHEMA = 'schema.sql'

print("Initializing the database...")

try:
    # Connect to the database (this will create the file if it doesn't exist)
    conn = sqlite3.connect(DATABASE)

    # Open and read the schema file
    with open(SCHEMA, 'r') as f:
        schema_script = f.read()
    
    # Execute the entire schema script
    conn.executescript(schema_script)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Database initialized successfully.")
    print("The file 'cashdash.db' has been created.")

except FileNotFoundError:
    print(f"ERROR: The schema file '{SCHEMA}' was not found in this directory.")
except Exception as e:
    print(f"An error occurred: {e}")