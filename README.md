# How to Connect Python to SQL Server Using pyodbc

1. install odbc driver from https://learn.microsoft.com/zh-tw/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16
2. pip install sqlalchemy, pyodbc
3. python main.py


# FreeTDS vs unixodbc
- 通常，FreeTDS 與 unixODBC 是一起使用的。
[Difference between FreeTDS and unixodbc?](https://stackoverflow.com/questions/31980980/difference-between-freetds-and-unixodbc)

## unixODBC
- 通用性高 (如果有換DB的需求, 需要用 unixODBC)
- unixODBC 需要進行額外的介面轉換和管理

## FreeTDS
- 只能用在MSSQL
- FreeTDS 直接使用資料庫的原生通訊協議，因此通常會比通過 unixODBC 間接連接資料庫效率更高