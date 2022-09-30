import pyodbc
import os

os.system('cls')
os.system('pip install pyodbc')
os.system('cls')


class SQLOperations:
    def __init__(self) -> None:
        self.connectionString = ("Driver={SQL Server Native Client 11.0};"
                                 "Server=localhost\SQLEXPRESS,1433;Database=EduIT;UID=sa;PWD=Admin123;")

    def execute_reader(self, query: str) -> tuple:
        cnxn = pyodbc.connect(self.connectionString)
        cursor = cnxn.cursor()
        for item in cursor.execute(query):
            yield item
        cursor.close()
        cnxn.close()

    def execute_query(self, query: str) -> None:
        cnxn = pyodbc.connect(self.connectionString)
        cursor = cnxn.cursor()
        count = cursor.execute(query)
        print(f"Se afectaron {count.rowcount} líneas")
        cnxn.commit()
        
        cursor.close()
        cnxn.close()


sqlOps = SQLOperations()

for i in sqlOps.execute_reader("SELECT * FROM [User]"):
    print(i)

query = ("INSERT INTO [dbo].[User] "
         "([name],[lastName],[email],[userName],[password],[country],[language],[roleID]) "
         "VALUES ('Hugo', 'Pérez Penas', 'hugo@hotmail.com', 'hugo', 'Admin123', 'MX', 'Python', 1)")
sqlOps.execute_query(query)

#os.system('pip uninstall pyodbc')
