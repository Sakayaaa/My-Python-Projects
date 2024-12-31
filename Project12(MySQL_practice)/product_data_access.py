import mysql.connector


def save_product(product,quantity,price):
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="mft"
    )
    cursor = database.cursor()

    cursor.execute("insert into mft.product (product,quantity,price) values (%s, %s, %s)", [product, quantity, price])
    database.commit()

    database.close()