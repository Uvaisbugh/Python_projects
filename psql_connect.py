import psycopg2

def connect():
    # connect 
    conn = psycopg2.connect(
        host="localhost",
        database="pos",
        user="postgres",
        password="123456"
    )
    return conn

def data():
    #
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    print("The number of parts: ", cur.rowcount)
    return rows

def insert_product(product):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", product)  
    conn.commit()
    print("Product added successfully")
    cur.close()
    conn.close()
    
def update_product(product):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE products SET name = %s, price = %s, stock = %s WHERE id = %s", product)
    print("Product updated successfully")
    conn.commit()
    cur.close()
    conn.close()
    
def delete_product(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = %s", (id,))
    print("Product deleted successfully")
    conn.commit()
    cur.close()
    conn.close()
    
def search_product(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE name = %s", (name,))
    print("The number of parts: ", cur.row)
    rows = cur.fetchall()
    return rows

