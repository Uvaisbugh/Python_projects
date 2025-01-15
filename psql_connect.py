import psycopg2
from psycopg2 import sql

# Function to connect to the PostgreSQL database
def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="pos",
            user="postgres",
            password="123456"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to fetch all products from the products table
def data():
    conn = connect()
    if conn is None:
        return None
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    print("The number of parts: ", cur.rowcount)
    cur.close()
    conn.close()
    return rows

# Function to insert a new product into the products table
def insert_product(product):
    conn = connect()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", product)
    conn.commit()
    print("Product added successfully")
    cur.close()
    conn.close()

# Function to update an existing product in the products table
def update_product(product):
    conn = connect()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("UPDATE products SET name = %s, price = %s, stock = %s WHERE id = %s", product)
    conn.commit()
    print("Product updated successfully")
    cur.close()
    conn.close()

# Function to delete a product from the products table
def delete_product(id):
    conn = connect()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = %s", (id,))
    conn.commit()
    print("Product deleted successfully")
    cur.close()
    conn.close()

# Function to search for a product by name
def search_product(name):
    conn = connect()
    if conn is None:
        return None
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE name = %s", (name,))
    rows = cur.fetchall()
    print("The number of parts: ", cur.rowcount)
    cur.close()
    conn.close()
    return rows

# Example Usage
if __name__ == "__main__":
    # Insert a new product
    insert_product(('Laptop', 1000, 50))

    # Update a product
    update_product(('Laptop Pro', 1200, 40, 1))

    # Search for a product by name
    product = search_product('Laptop Pro')
    print(product)

    # Delete a product
    delete_product(1)
    
    # Fetch all products
    all_products = data()
    print(all_products)
