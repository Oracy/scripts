import psycopg2
import time

try:
    connection = psycopg2.connect(user="docker",
                                    password="docker",
                                    host="localhost",
                                    port="5432",
                                    database="postgres")
    cursor = connection.cursor()

    postgres_create_query = """ CREATE TABLE distributors ( did     integer, name    varchar(40) ); """
    cursor.execute(postgres_create_query)
    connection.commit()
    
    while True:
        postgres_insert_query = """ INSERT INTO public.distributors (did, "name") VALUES (%s,%s)"""
        record_to_insert = (0, '')
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")
        time.sleep( 0.1 )


except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")