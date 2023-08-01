#Write a Python code snippet to establish a connection with a Microsoft
#SQL Server database.Include the necessary steps and import statements.

"""import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ALAA\MSSQLS;'
                      'Database=TMS;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM borrower')

for i in cursor:
    print(i)"""

#Explain the process of creating a new database in Microsoft SQL Server
#using Python. Provide a code example that demonstrates the creation
#of a database with specific parameters.

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ALAA\MSSQLS;'
                      'Database=TMS;'
                      'Trusted_Connection=yes;')
conn.autocommit= True
cursor = conn.cursor()
cursor.execute('CREATE DATABASE a1')
cursor.close()
conn.close()


#Write a Python function that takes input parameters and inserts data into a specific table in the SQL
#Server database. Include error handling and parameterized queries in your code.

"""import pyodbc

def insert_data_into_table(server, database, table, data):
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
        cursor = conn.cursor()

        query = f"INSERT INTO {table} (product_id, product_name, price) VALUES (?, ?, ?)"

        for row in data:
            cursor.execute(query, row) 
        conn.commit()
        conn.close()

        print("Data inserted successfully!")
    except pyodbc.Error as e:
        print("Error occurred while inserting data into the table:", e)


server_name = "DESKTOP-ALAA\MSSQLS"
db_name = "Test_Database"
table_name = "products"
data_to_insert = [
    ('3', 'Computer', '800'),  
    ('4', 'Printer', '150')  
]

insert_data_into_table(server_name, db_name, table_name, data_to_insert)"""


#Create a SQL query using Python to retrieve all records from a specific table in the database.Write the
#Python code to execute the query and print the fetched data.

"""import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ALAA\MSSQLS;'
                      'Database=Test_Database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM products')

for i in cursor:
    print(i)"""

#Implement a Python function that calculates the average value of a specific column in a table using
#data retrieved from the SQL Server database. Include error handling and appropriate data type
#conversion in your code.

"""import pyodbc

def calculate_average(server, database, table, column):
    try:
        
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
        cursor = conn.cursor()

        query = f"SELECT {column} FROM {table}"
        cursor.execute(query)

        rows = cursor.fetchall()
        if rows:
            total = 0
            count = 0

            for row in rows:
                value = row[0]  
                if value is not None:
                    total += float(value)
                    count += 1

            if count > 0:
                average = total / count
                print("Average:", average)
            else:
                print("No data found in the column.")
        else:
            print("No rows found in the table.")

        conn.close()

    except pyodbc.Error as e:
        print("Error occurred while calculating the average:", e)


server_name = "DESKTOP-ALAA\MSSQLS"
db_name = "Test_Database"
table_name = "products"
column_name = "price"

calculate_average(server_name, db_name, table_name, column_name)"""

#Write a Python script that connects to the SQL Server database, selects a subset of records based on
#specific criteria, and performs statistical calculations such as calculating the mean and standard
#deviation of a numeric column. Print the calculated statistics as output.

"""import pyodbc
import statistics

def calculate_statistics(server, database, table, column, condition):
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
        cursor = conn.cursor()

        query = f"SELECT {column} FROM {table} WHERE {condition}"

        cursor.execute(query)

        rows = cursor.fetchall()

        if rows:
            values = []

            for row in rows:
                value = row[0] 
                if value is not None:
                    values.append(float(value))

            if values:
                mean = statistics.mean(values)
                stddev = statistics.stdev(values)

                print("Mean:", mean)
                print("Standard Deviation:", stddev)
            else:
                print("No numeric values found in the column")
        else:
            print("No rows found matching the criteria")

        conn.close()

    except pyodbc.Error as e:
        print("Error occurred while executing the query:", e)


server_name = "DESKTOP-ALAA\MSSQLS"
db_name = "Test_Database"
table_name = "products"
column_name = "price"
condition = "price <= 800"  

calculate_statistics(server_name, db_name, table_name, column_name, condition)"""


