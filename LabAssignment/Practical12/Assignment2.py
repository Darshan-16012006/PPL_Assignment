import sqlite3

conn = sqlite3.connect("practical12.db")
cursor = conn.cursor()

# Create Item Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Item (
    item_id TEXT PRIMARY KEY,
    item_name TEXT,
    category TEXT,
    price INTEGER,
    stock INTEGER,
    supplier TEXT
)
""")

# Insert Items
items = [
    ('C101', 'Denim Jeans', 'Bottomwear', 1500, 30, 'Levis'),
    ('C102', 'Cotton Shirt', 'Topwear', 1200, 50, 'Raymond'),
    ('C103', 'Silk Saree', 'Ethnicwear', 5000, 20, 'Fabindia'),
    ('C104', 'Woolen Sweater', 'Winterwear', 2000, 15, 'Spark'),
    ('C105', 'Sports T-Shirt', 'Active Wear', 800, 60, 'Nike')
]

cursor.executemany("INSERT OR IGNORE INTO Item VALUES (?, ?, ?, ?, ?, ?)", items)

# Create Supplier Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Supplier (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT,
    contact TEXT,
    location TEXT
)
""")

# Insert Suppliers
suppliers = [
    ('S201', "Levi's", '9876543210', 'Mumbai'),
    ('S202', 'Raymond', '9123456789', 'Delhi'),
    ('S203', 'Fabindia', '9988776655', 'Bangalore'),
    ('S204', 'Monte Carlo', '9345678123', 'Chandigarh'),
    ('S205', 'Nike', '9234567890', 'Pune')
]

cursor.executemany("INSERT OR IGNORE INTO Supplier VALUES (?, ?, ?, ?)", suppliers)

# Operation 1: Display all items
print("Items in Inventory:\n")
cursor.execute("SELECT * FROM Item")
for row in cursor.fetchall():
    print(row)

# Display Supplier Table
print("\nSupplier Table:\n")
cursor.execute("SELECT * FROM Supplier")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()