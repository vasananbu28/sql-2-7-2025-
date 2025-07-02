import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="786@",       
    database="banking"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS banking (
    account_num INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    age INT,
    amount INT(50)
)
""")
insert_query = """
INSERT IGNORE INTO banking (account_num, username, age, amount)
VALUES (%s, %s, %s,%s)
"""

banking_data = [
    ("23456789","Reshma", 21, "50000"),
    ("34567894","Arjun", 22, "60000"),
    ("45678909","Priya", 20, "700000"),
    ("67567890","Karthik", 23, "80000"),
    ("45345678","Sneha", 21, "7000000"),
    ("56789077","Vishwa",24,"67900000")
]
cursor.executemany(insert_query, banking_data)
print(f"{cursor.rowcount} rows inserted successfully.")
cursor.execute("SELECT * FROM banking")
rows = cursor.fetchall()
print("\naccount_num | username     | age | amount")
print("-" * 32)
for row in rows:
    print(f"{row[0]:<2} | {row[1]:<9} | {row[2]:<3} | {row[3]}")
    
update_query="""
update banking
set username = %s , age =  %s
where account_num= %s
"""
update_data=("penciya" , 25, 56789077)
cursor.execute(update_query,update_data)

print(f"{cursor._rowcount} is upadted successfully")



delete_query="""
delete from banking
where username=%s"""

delete_data=("sneha",)
cursor.execute(delete_query,delete_data)
print(f"{cursor.rowcount} is deleted")

cursor.execute("SELECT * FROM banking")
updatedrows = cursor.fetchall()
for row in updatedrows:
    print(f"{row[0]:<2} | {row[1]:<9} | {row[2]:<3} | {row[3]}")
    


    
conn.commit()
cursor.close()
conn.close()