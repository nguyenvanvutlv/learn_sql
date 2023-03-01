import sqlite3


department = """
CREATE TABLE IF NOT EXISTS department(
    DepartmentID INT PRIMARY KEY NOT NULL,
    DepartmentName VARCHAR(20)
);
"""

employee = """
CREATE TABLE IF NOT EXISTS employee (
    LastName VARCHAR(20),
    DepartmentID INT REFERENCES department(DepartmentID)
);
"""

add_data_1 = """
INSERT INTO department
VALUES (31, 'Sales'),
       (33, 'Engineering'),
       (34, 'Clerical'),
       (35, 'Marketing');
"""

add_data_2  = """
INSERT INTO employee
VALUES ('Rafferty', 31),
       ('Jones', 33),
       ('Heisenberg', 33),
       ('Robinson', 34),
       ('Smith', 34),
       ('Williams', NULL);
"""



data = sqlite3.connect("data.db")

myCursor = data.cursor()

myCursor.execute(department)
myCursor.execute(employee)
myCursor.execute(add_data_1)
myCursor.execute(add_data_2)
data.commit()
# data.cursor().execute(add_data)