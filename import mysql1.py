import mysql.connector
from mysql.connector import Error

def main():
    try:
        # 1. connect to the database
        con=mysql.connector.connect(host='localhost',database='klndemo',user='root',password='root')
        if con.is_connected():
            print('connected to database')
        else:
            print('not connected to database')
            
        cursor =con.cursor()   
        # 2) Insert Operation
        name=input("Enter the Name to insert :")
        password=input("Enter Password to insert :")
        
        insert_sql="INSERT INTO login (name,password) VALUES (%s,%s)"
        cursor.execute(insert_sql,(name,password))
        con.commit()
        print('inserted data')
        
        # 4) Update 
        password1 = input("Enter new password: ")
        name1 = input("Enter the name to update password for: ")

        update_sql = "UPDATE login SET password = %s WHERE name = %s"
        cursor.execute(update_sql, (password1, name1))
        con.commit()
        print('updated data')
        
        # Display
        print("Current Records :")
        view_sql="SELECT * FROM login"
        cursor.execute(view_sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        # 5) Delete
        name2 = input("Enter name to delete: ")
        delete_sql = "DELETE FROM login WHERE name = %s"
        cursor.execute(delete_sql, (name2,))
        con.commit()
        print('deleted data')
        
        print("Current Records :")
        view_sql="SELECT * FROM login"
        cursor.execute(view_sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
        
    except Error as e:
        print('error while connecting to mysql',e)
    finally:
        if con.is_connected():
            con.close()
            print('database connection closed')
            
if _name_ =="_main_":
    main()