import pyodbc
# IMPORTANT: insert credentials here!!!
class SQL:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = None
        self.cursor = None

    def connect(self):
        try:
            self.cnxn = pyodbc.connect(
                f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
            )
            self.cursor = self.cnxn.cursor()
            print("Connected successfully!")
        except pyodbc.Error as e:
            print(f"Error connecting to SQL Server: {e}")
        finally:
            return self

    def disconnect(self):
        if self.cnxn:
            self.cnxn.close()
            self.cursor = None
            print("Disconnected successfully!")
        else:
            print("There is no connection to disconnect.")

# query
sql = SQL(server="myserver", database="mydatabase", username="myusername", password="mypassword")
sql.connect()
#store connection to cnxn and cursor object
cnxn = sql.cnxn
cursor = cnxn.cursor()

# disconnecting
sql.disconnect()

#SQL query on languages

try:
    # establish connection and cursor
    sql_conn = SQL()
    cursor = sql_conn.cursor()

    # execute the query to join languages and capitals tables
    query = '''SELECT l.country_name, l.language_spoken, c.capital_cities 
               FROM languages l 
               JOIN capitals c ON l.capital_cities_id = c.ID'''
    cursor.execute(query)

    # iterate through the results and print in the desired format
    for row in cursor:
        print(f"Country: {row.country_name} - Language {row.language_spoken}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # close the cursor and connection
    cursor.close()
    sql_conn.close()

#Add a new country 
#assumes connection is valid

new_country = 'Mongolia'
new_language = 'Mongolian'
capital_cities_id = 13

# execute SQL command to insert new row
insert_query = f"INSERT INTO languages (country, language, datetime_column, capital_cities_id) VALUES ('{new_country}', '{new_language}', NULL, {capital_cities_id})"
cursor = cnxn.cursor()
cursor.execute(insert_query)

# commit changes to database
cnxn.commit()

# close the cursor
cursor.close()

#close connection
cnxn.close()

############ update columns in language

# create a cursor object
cursor = cnxn.cursor()

# update rows with duplicated language
update_query = '''UPDATE languages
                  SET datetime_column = GETDATE()
                  WHERE language IN (
                      SELECT language
                      FROM languages
                      GROUP BY language
                      HAVING COUNT(*) > 1
                  )'''
cursor.execute(update_query)

# commit changes to database
cnxn.commit()

# close the cursor and connection
cursor.close()
cnxn.close()
