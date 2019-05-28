import mysql.connector

mySql_server = '10.10.16.202'
Database = 'db_newsilpo_dev1'

connection = mysql.connector.connect(host=mySql_server,
                                        database=Database,
                                        port=3306,
                                        user='a-b.shvets',
                                        password='Ganjubas6'
                                    )

mySql_query = ("""
        SELECT *
        FROM hr_vacancy
        """)

cursor = connection.cursor()
cursor.execute(mySql_query)

result = cursor.fetchall()


print(result)
connection.close()