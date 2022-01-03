from time import sleep
from bottle import route, run, template
import mariadb
import sys
import os


HOST = os.getenv("MYSQL_HOST", "mysql")
USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSWORD')
DATABASE = os.getenv('MYSQL_DATABASE')

print('Connecting to MariaDB...')
print(f'Connecting to {DATABASE}')
print(f'User: {USER}')
print(f'Password: {PASSWORD}')

try:
    conn = mariadb.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=3306,
        database=DATABASE

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)")

# Create 5 fake products
for i in range(5):
    print(f'Inserting product {i}')
    cur.execute(
        "INSERT INTO products (name, price) VALUES (?,?)", ('PRODUCT ' + str(i), i * 10))


@route('/')
def listAll():
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    res = ''
    for row in rows:
        res += f'<li>ID {row[0]} Name {row[1]} Price {row[2]}</li>'
    return res


@route('/<id>')
def get(id: int):
    print("test")
    cur.execute(f"SELECT * FROM products WHERE id='{id}'")
    row = cur.fetchone()
    if row is None:
        return f"{id} not found"
    print(f'Found product {row is None}')
    print(row)

    return f"""
    Product name: <b>{row[0]}</b><br>
    Product id: <b>{row[1]}</b><br>
    Product price: <b>{row[2]}</b><br>
    """
    print(f"id: {id}, name: {name}, price: {price}")


@ route('/insert/<name>/<price>')
def insert(name: str, price: int):
    cur.execute("INSERT INTO products (name, price) VALUES (?,?)", (name, price))
    conn.commit()
    return template("""
    Product name: <b>{{name}}</b><br>
    Product price: <b>{{price}}</b><br>
    """, name=name, price=price)


if __name__ == "__main__":

    run(host='0.0.0.0', port=80,
        server='paste', debug=True, reloader=True)
