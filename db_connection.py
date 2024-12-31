import pyodbc

def get_db_connection():
    connection = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=dist-6-505.uopnet.plymouth.ac.uk;" 
        "Database=COMP2001_SThompson;"             
        "UID=SThompson;"                                 
        "PWD=AeuF110*;"                        
        "TrustServerCertificate=yes;"
    )
    return connection
