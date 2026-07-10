import sqlite3


def show_menu():
    print()
    print("1 - Show all products")
    print("2 - Show products by category")
    print("3 - Show category stats")
    print("4 - Show expensive products")
    print("5 - Show products by min price")
    print("6 - Show cheapest product")
    print("7 - Show most expensive product")
    print("8 - Show products count")
    print("9 - Show average price")
    print("10 - Show total price")
    print("11 - Show products by max price")
    print("12 - Show products by price range")
    print("13 - Search products by title")
    print("14 - Search products by title part")
    print("15 - Search products by category part")
    print("16 - Search products")
    print("17 - Show products sorted by price")
    print("18 - Show products sorted by price desc")
    print("19 - Show products sorted by category and price")
    print("20 - Add product")
    print("21 - Delete product")
    print("22 - Update product price")
    print("0 - Exit")


def print_product(product):
    product_id = product[0]
    title = product[1]
    price = product[2]
    category = product[3]

    print(f"{product_id}. {title} | {price} | {category}")


def show_category_stats(cursor):
    cursor.execute("""
    SELECT category, SUM(price) AS total_price, AVG(price) AS average_price
    FROM products
    GROUP BY category;
    """)

    products = cursor.fetchall()

    for product in products:
        category = product[0]
        total_price = product[1]
        average_price = product[2]

        print(f"{category} | total: {total_price} | average: {average_price}")


def show_all_products(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    ORDER BY title;
    """)

    products = cursor.fetchall()

    for product in products:
        print_product(product)


def get_int_input(prompt):
    try:
        number = int(input(prompt))
        return number
    except ValueError:
        print("Please enter a valid number")
        return None


def get_non_empty_text(prompt, error_message):
    text = input(prompt).strip()

    if not text:
        print(error_message)
        return None
    
    return text


def update_product_price(connection, cursor):
    product_id = get_int_input("Enter product id: ")

    if product_id is None:
        return
    
    new_price = get_int_input("Enter new price: ")

    if new_price is None:
        return
    
    if new_price <= 0:
        print("Price must be greater than zero")
        return
    
    cursor.execute("""
    UPDATE products
    SET price = ?
    WHERE id = ?;
    """, (new_price, product_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("Product not found")
        return
    
    print("Product price updated successfully")


def show_products_by_category(cursor, category):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE category = ?;
    """, (category,))

    products = cursor.fetchall()

    if not products:
        print("No products in this category")
        return

    for product in products:
        print_product(product)


def show_expensive_products(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE price > 1000
    ORDER BY price DESC;
    """)

    products = cursor.fetchall()

    if not products:
        print("No expensive products found")
        return

    for product in products:
        print_product(product)


def show_products_by_min_price(cursor, min_price):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE price > ?
    ORDER BY price DESC;
    """, (min_price,))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return

    for product in products:
        print_product(product)


def show_products_by_max_price(cursor, max_price):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE price < ?
    ORDER BY price;
    """, (max_price,))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return

    for product in products:
        print_product(product)


def show_products_by_price_range(cursor, min_price, max_price):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE price >= ? AND price <= ?
    ORDER BY price;
    """, (min_price, max_price))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return

    for product in products:
        print_product(product)


def show_cheapest_product(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    ORDER BY price
    LIMIT 1;
    """)

    product = cursor.fetchone()

    if product is None:
        print("No product found")
        return
    
    print_product(product)

    

def show_most_expensive_product(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    ORDER BY price DESC
    LIMIT 1;
    """)

    product = cursor.fetchone()

    if product is None:
        print("No products found")
        return
    
    print_product(product)


def show_average_price(cursor):
    cursor.execute("""
    SELECT AVG(price) AS average_price
    FROM products;
    """)

    result = cursor.fetchone()

    average_price = result[0]

    if average_price is None:
        print("No products found")
        return

    print(f"Average price: {average_price}")


def show_total_price(cursor):
    cursor.execute("""
    SELECT SUM(price) AS total_price
    FROM products;
    """)

    result = cursor.fetchone()

    total_price = result[0]

    if total_price is None:
        print("No products found")
        return

    print(f"Total price: {total_price}")


def show_products_count(cursor):
    cursor.execute("""
    SELECT COUNT(*) AS products_count
    FROM products;
    """)

    result = cursor.fetchone()

    if result is None:
        print("No products")
        return
    
    count = result[0]

    print(f"Products count: {count}")

def search_product_by_title(cursor, title):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE title = ?;
    """, (title,))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return
    
    for product in products:
        print_product(product)


def search_products_by_title_part(cursor, title_part):
    
    pattern = f"%{title_part}%"

    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE title LIKE ?
    ORDER BY title;
    """, (pattern,))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return

    for product in products:
        print_product(product)


def search_products_by_category_part(cursor, category_part):
    
    pattern = f"%{category_part}%"

    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE category LIKE ?
    ORDER BY title;
    """, (pattern,))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return

    for product in products:
        print_product(product)


def search_products(cursor, search_text):
    pattern = f"%{search_text}%"

    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    WHERE title LIKE ? OR category LIKE ?
    ORDER BY title;
    """, (pattern, pattern))

    products = cursor.fetchall()

    if not products:
        print("No products found")
        return

    for product in products:
        print_product(product)


def show_products_sorted_by_price(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    ORDER BY price;
    """)

    products = cursor.fetchall()

    for product in products:
        print_product(product)


def show_products_sorted_by_price_desc(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    ORDER BY price DESC;
    """)

    products = cursor.fetchall()

    for product in products:
        print_product(product)


def show_products_sorted_by_category_and_price(cursor):
    cursor.execute("""
    SELECT id, title, price, category
    FROM products
    ORDER BY category, price;
    """)

    products = cursor.fetchall()

    for product in products:
        print_product(product)

def add_product(connection, cursor):
    title = get_non_empty_text("Enter title: ", "Title cannot be empty")

    if title is None:
        return
    
    price = get_int_input("Enter price: ")

    if price is None:
        return

    if price <= 0:
        print("Price must be greater than zero")
        return

    category = get_non_empty_text("Enter category: ", "Category cannot be empty")

    if category is None:
        return
    
    category = category.capitalize()

    cursor.execute("""
    INSERT INTO products (title, price, category)
    VALUES (?, ?, ?);
    """, (title, price, category))

    connection.commit()

    print("Product added successfully")


def delete_product(connection, cursor):
    product_id = get_int_input("Enter product id: ")

    if product_id is None:
        return

    cursor.execute("""
    DELETE FROM products
    WHERE id = ?;
    """, (product_id,))

    connection.commit()

    if cursor.rowcount == 0:
        print("Product not found")
        return

    print("Product deleted successfully")                    


def setup_database(connection, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price INTEGER,
        category TEXT
    )
    """)

    cursor.execute("""
    SELECT COUNT(*)
    FROM products;
    """)

    result = cursor.fetchone()
    products_count = result[0]

    if products_count == 0:
        cursor.execute("""
        INSERT INTO products (title, price, category)
        VALUES
        ('Milk', 80, 'Food'),
        ('Keyboard', 3000, 'Tech'),
        ('Bread', 50, 'Food'),
        ('Mouse', 1500, 'Tech')
        """)

        connection.commit()




def run_app(connection, cursor):
    while True:
        show_menu()

        choice = input("Choose option: ").strip()

        if choice == "1":
            show_all_products(cursor)
    
        elif choice == "2":
            category = input("Enter category: ").strip().capitalize()
            show_products_by_category(cursor, category)

        elif choice == "3":
            show_category_stats(cursor)

        elif choice == "4":
            show_expensive_products(cursor)

        elif choice == "5":
            min_price = input("Enter min price: ").strip()

            try:
                min_price = int(min_price)
            except ValueError:
                print("Price must be a number")
                continue

            show_products_by_min_price(cursor, min_price)

        elif choice == "6":
            show_cheapest_product(cursor)

        elif choice == "7":
            show_most_expensive_product(cursor)

        elif choice == "8":
            show_products_count(cursor)

        elif choice == "9":
            show_average_price(cursor)

        elif choice == "10":
            show_total_price(cursor)

        elif choice == "11":
            max_price = input("Enter max price: ").strip()

            try:
                max_price = int(max_price)
            except ValueError:
                print("Price must be a number")
                continue

            show_products_by_max_price(cursor, max_price)

        elif choice == "12":
            min_price = input("Enter min price: ").strip()
            max_price = input("Enter max price: ").strip()

            try:
                min_price = int(min_price)
                max_price = int(max_price)
            except ValueError:
                print("Price must be a number")
                continue

            if min_price > max_price:
                print("Min price cannot be greater than max price")
                continue

            show_products_by_price_range(cursor, min_price, max_price)    
        
        elif choice == "13":
            title = input("Enter title: ").strip().capitalize()
            search_product_by_title(cursor, title)

        elif choice == "14":
            title_part = input("Enter title part: ").strip()

            if not title_part:
                print("Title part cannot be empty")
                continue
            
            search_products_by_title_part(cursor, title_part)

        elif choice == "15":
            category_part = input("Enter category part: ").strip()

            if not category_part:
                print("Category part cannot be empty")
                continue
            
            search_products_by_category_part(cursor, category_part)

        elif choice == "16":
            search_text = input("Enter search text: ").strip()

            if not search_text:
                print("Search text cannot be empty")
                continue
            
            search_products(cursor, search_text)

        elif choice == "17":
            show_products_sorted_by_price(cursor)

        elif choice == "18":
            show_products_sorted_by_price_desc(cursor)

        elif choice == "19":
            show_products_sorted_by_category_and_price(cursor)

        elif choice == "20":
            add_product(connection, cursor)

        elif choice == "21":
            delete_product(connection, cursor)

        elif choice == "22":
            update_product_price(connection, cursor)                          

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Wrong choice")
    

def main():

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    setup_database(connection, cursor)

    run_app(connection, cursor) 

    connection.close()


if __name__ == "__main__":
    main()    

    

