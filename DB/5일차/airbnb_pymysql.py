import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'beebom((00',
    db = 'airbnb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    #1번문제 : 새 제품 추가
    sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"

    cursor.execute(sql,('Python Book',10000,10))
    connection.commit()

    #문제 2 고객 목록 조회


    cursor.execute("SELECT * FROM Products")
    for book in cursor.fetchall():
        print(book)

    
    #문제 3 제품 재고 업데이트

    sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    cursor.execute(sql, (1,1))
    connection.commit()

    # 고객별 총 주문 금액
    sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM orders GROUP BY customerID"
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)

    #고객 이메일 업데이트
    sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    cursor.execute(sql, ('update@update.com', 1))
    connection.commit()

    # 주문취소
    sql = "DELETE FROM Orders WHERE orderID = %s"
    cursor.execute(sql, (15))
    connection.commit()


    # 특정제품검색
    sql = "SELECT * FROM Products WHERE productName LIKE %s"
    cursor.execute(sql, ('%Book'))
    datas = cursor.fetchall()

    for data in datas :
        print(data['productName'])

    # 특정고객의 모든 주문 조회
    sql = "SELECT * FROM Orders WHERE customerID = %s"
    cursor.execute(sql, (1))
    datas = cursor.fetchall()

    for data in datas :
        print(data)

    # 가장많이 주문한 고객
    sql = "SELECT customerID, COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"

    cursor.execute(sql)

    data = cursor.fetchone()
    print(data)    


cursor.close()