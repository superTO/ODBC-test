from sqlalchemy import create_engine
from urllib.parse import quote_plus

# ip addres
server = "192.168.0.1:1433"
# account
user = ""
password = ""
db_name = "db_name"
# ODBC driver
dsn = "ODBC Driver 17 for SQL Server"

engine = create_engine(f"mssql+pyodbc://{user}:%s@{server}/{db_name}?TrustServerCertificate=yes&driver={dsn}" % quote_plus(password))

connection = engine.connect()

print("connected")

connection.close()

# query test

# insert test

# update test

# delete test
