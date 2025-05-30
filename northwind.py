import sqlite3

# Connect to the northwind_small database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query 1: What are the ten most expensive items
expensive_items = curs.execute('''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
''').fetchall()

# Query 2: What is the average age of an employee at the time of their hiring?
avg_hire_age = curs.execute("""
SELECT AVG(HireDate - BirthDate) AS avg_age
FROM Employee
""").fetchall()

# Query 3: What are the ten most expensive items?
ten_most_expensive = curs.execute("""
SELECT Produt.ProductName, Product.UnitPrice,Supplier.CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
""").fetchall()


# Query 4: What is the largest category (by number of unique products in it)?
largest_category = curs.execute("""
SELECT Category.CategoryName, COUNT(DISTINCT Product.Id) AS num_products
FROM Category
JOIN Product ON Category.Id = Product.CategoryId
GROUP BY Category.Id
ORDER BY num_products DESC
LIMIT 1
""").fetchall()

if __name__ == '__main__':
    print("Expensive Items:", expensive_items)
    print("Avg Hire Age:", avg_hire_age)
    print("Ten Most Expensive:", ten_most_expensive)
    print("Largest Category:", largest_category)
