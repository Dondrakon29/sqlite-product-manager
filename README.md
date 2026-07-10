# SQLite Product Manager

Console application for managing products using Python and SQLite.

The project allows you to store products in a local SQLite database, search and filter them, show statistics, add new products, and delete products by id.

## Features

- Show all products
- Show products by category
- Show expensive products
- Show products by minimum price
- Show products by maximum price
- Show products by price range
- Show the cheapest product
- Show the most expensive product
- Show products count
- Show average price
- Show total price
- Show category statistics
- Search product by exact title
- Search products by title part
- Search products by category part
- Search products by title or category
- Sort products by title
- Sort products by price
- Sort products by price descending
- Sort products by category and price
- Add new product
- Delete product by id
- Save data between program runs
- Reusable helper functions for validating integer and text input
- Update product price by ID

## Technologies

- Python
- SQLite
- sqlite3 module

## What I practiced

- Working with SQLite database
- Creating tables with `CREATE TABLE`
- Using `SELECT` queries
- Filtering data with `WHERE`
- Sorting data with `ORDER BY`
- Using `ORDER BY DESC`
- Sorting by multiple columns
- Limiting results with `LIMIT`
- Counting rows with `COUNT`
- Calculating totals with `SUM`
- Calculating average values with `AVG`
- Grouping data with `GROUP BY`
- Searching text with `LIKE`
- Using `AND` and `OR`
- Adding data with `INSERT`
- Deleting data with `DELETE`
- Using `AUTOINCREMENT` for product id
- Using SQL parameters with `?`
- Using `fetchall()`
- Using `fetchone()`
- Using `commit()`
- Checking deleted rows with `rowcount`
- Validating user input
- Handling incorrect number input with `try/except`
- Building a console menu
- Splitting code into functions
- Writing reusable helper functions
- Validating user input
- Refactoring repeated code
- UPDATE
- CRUD operations

## How to run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Open the project folder:

```bash
cd <project-folder>
```

3. Run the program:

```bash
python sql_intro.py
```

## Example menu

```text
1 - Show all products
2 - Show products by category
3 - Show category stats
4 - Show expensive products
5 - Show products by min price
6 - Show cheapest product
7 - Show most expensive product
8 - Show products count
9 - Show average price
10 - Show total price
11 - Show products by max price
12 - Show products by price range
13 - Search products by title
14 - Search products by title part
15 - Search products by category part
16 - Search products
17 - Show products sorted by price
18 - Show products sorted by price desc
19 - Show products sorted by category and price
20 - Add product
21 - Delete product
22 - Update product price
0 - Exit
```

## Example product output

```text
1. Milk | 80 | Food
2. Keyboard | 3000 | Tech
3. Bread | 50 | Food
4. Mouse | 1500 | Tech
```

## Database

The project uses a local SQLite database:

```text
shop.db
```

The database is created automatically when the program starts.

If the products table is empty, the program adds default products:

```text
Milk
Keyboard
Bread
Mouse
```

New products are saved and remain available after restarting the program.

## Project status

Completed as a learning project.

This project helped me practice the connection between Python, SQLite, SQL queries, and console application structure.