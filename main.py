# Note: Only difference between dynamic and embedded is that queries are 
# hard coded in embedded and variables allow changes in dynamic.

import pyodbc

class Database:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=' + self.server + ';Database=' + self.database + ';Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
    
    def execute_query(self, sql_query, params):
        self.cursor.execute(sql_query, params)
        rows = self.cursor.fetchall()
        return rows

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# Example usage
db = Database('MSI\SQLEXPRESS', 'mydatabase')

# Example user input
username = "Alice"

# Construct a dynamic SQL query using a Python string
sql_query = "SELECT * FROM users WHERE username = ?"

# Execute the query with user input
rows = db.execute_query(sql_query, [username])

# Fetch the results and print them
for row in rows:
    print(row)
