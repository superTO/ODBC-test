import pyodbc

# wrong ip address
# server = "192.168.0.1:1433"
# correct ip address
server = "192.168.0.1,1433" # PORT using , not :
user = ""
password = ""
db_name = "db_name"
dsn = "{ODBC Driver 17 for SQL Server}"

connectionString = f'DRIVER={dsn};SERVER={server};DATABASE={db_name};UID={user};PWD={password};TrustServerCertificate=yes;'

try:
    print("Connecting to database...")
    conn = pyodbc.connect(connectionString, timeout=5)
    print("connected")
    conn.close()
except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Error: {ex}")
    print(f"SQLSTATE: {sqlstate}")
except Exception as e:
    print(f"Unexpected error: {e}")