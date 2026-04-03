import sqlite3

conn = sqlite3.connect("practical11.db")
cursor = conn.cursor()

# Create Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    empno TEXT PRIMARY KEY,
    emp_name TEXT,
    dept_name TEXT,
    salary INTEGER,
    doj TEXT,
    branch TEXT
)
""")

# Insert Data
employees = [
    ('E101', 'Vivek', 'R&D', 145000, '2019-06-11', 'Nagpur'),
    ('E102', 'Vishal', 'Marketing', 90000, '2012-03-15', 'Pune'),
    ('E103', 'Priyal', 'Product Development', 120000, '2018-07-20', 'Bangalore'),
    ('E105', 'Shrushti', 'Product Development', 80000, '2019-09-19', 'Nagpur'),
    ('E106', 'Pranay', 'Product Development', 100000, '2018-10-22', 'Mumbai')
]

cursor.executemany("INSERT OR IGNORE INTO Employee VALUES (?, ?, ?, ?, ?, ?)", employees)

# Create Designation Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Designation (
    empno TEXT,
    emp_name TEXT,
    designation TEXT
)
""")

designations = [
    ('E101', 'Vivek', 'Project Manager'),
    ('E102', 'Vishal', 'Sales Manager'),
    ('E103', 'Priyal', 'Design Architect'),
    ('E105', 'Shrushti', 'Software Developer'),
    ('E106', 'Pranay', 'Project Lead')
]

cursor.executemany("INSERT OR IGNORE INTO Designation VALUES (?, ?, ?)", designations)

# Display Employees
print("Employee Table:\n")
cursor.execute("SELECT * FROM Employee")
for row in cursor.fetchall():
    print(row)

# Display Designations
print("\nDesignation Table:\n")
cursor.execute("SELECT * FROM Designation")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()