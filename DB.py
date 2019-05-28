import pypyodbc

server = 's-kv-center-x61;'
database = ''
connection = pypyodbc.connect('driver={ODBC Driver 13 for SQL Server};'
                              'Trusted_Connection=No;'
                              'server=s-kv-center-x61;'
                              'uid=OFFICEKIEV\\a-b.shvets;'
                              'pwd=Ganjubas6')

cursor = connection.cursor()

query = ("""
    SELECT TOP 50
    FROM [base].[Vouchers]"""
)

result = cursor.fetchall()
for x in result:
    print(result)

connection.close()