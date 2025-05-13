import mysql.connector 
from faker import Faker
import random #파이썬 기본 모듈

db_connection = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password="beebom((00",
    database = 'testdatabase'
)

#mysql 연결
cursor = db_connection.cursor()
faker = Faker()

#users 데이터 생성

for _ in range(100):
    username=faker.user_name()
    email = faker.email()

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
    cursor.execute(sql,(username,email))



    

# user_id 불러오기
cursor.execute("select user_id from users")
valid_user_id = [row[0] for row in cursor.fetchall()]

#100개의 주문 더미 데이터 생성
for _ in range(100):
    username=faker.user_name()

 

    user_id = random.choice(valid_user_id)

    product_name = faker.word()
    quantity = random.randint(1,10)


try:
    sql = "insert into orders(user_id, product_name, quantity) VALUES(%s,%s,%s)"
    values = (user_id, product_name, quantity)
    cursor.execute(sql, values)

except :
    print("오류발생")
    pass

db_connection.commit()
cursor.close()
db_connection.close()