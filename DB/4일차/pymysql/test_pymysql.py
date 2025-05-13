import pymysql

# (1) db connection
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password='beebom((00',
    db = 'classicmodels',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor

)

# (2) CRUD

## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()



    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])


## 2. INSERT INTO
def add_customer():
    name = 'inseop'
    feamily_name = 'kim'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES{1000}, {name} ,{family_name})"
    cursor.execute(sql)
    connection.commit()
    
add_customer()


   