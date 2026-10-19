import pyodbc

SERVER = "Avinash"
DATABASE = "Employeedb"
DRIVER = "ODBC Driver 18 for SQL Server"

def get_connection():
    return pyodbc.connect(
        f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};"
        "Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes;"
    )