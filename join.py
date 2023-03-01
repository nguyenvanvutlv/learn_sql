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
# myCursor.execute(department)
# myCursor.execute(employee)
# myCursor.execute(add_data_1)
# myCursor.execute(add_data_2)
# data.commit()


# Cross join
# kết hợp mỗi hàng từ bảng 1 với mỗi hàng ở bảng 2

# kết hợp chéo rõ ràng
# results = myCursor.execute("SELECT * FROM employee CROSS JOIN department").fetchall()
# for result in results:
#     print(result)


# results = myCursor.execute("SELECT * FROM employee, department").fetchall()
# for result in results:
#     print(result)



# Inner join -> kết hợp các giá trị của hai bảng
# Yêu cầu mỗi hàng trong 2 bảng phải có cùng một giá trị cột
# -> không được coi là lựa chọn tốt nhất trong các tình huống
# so sánh từng hàng của A với từng hàng của B để tìm các cặp thoả mãn
# có hai cách một là explicit [rõ ràng], implicit [ngầm] <không khuyến khích>
# được dùng khi các cột giá trị của các bảng không có giá trị NULL
def inner_join(database, explicit: bool = True, implicit: bool = False, is_null: bool = False):
    assert explicit != implicit
    cursor = database.cursor()
    if explicit:
        results = cursor.execute("""
            SELECT employee.LastName, employee.DepartmentID, department.DepartmentName 
            FROM employee
            INNER JOIN department ON
            employee.DepartmentID = department.DepartmentID;
        """).fetchall()
        print("Results of Explicit")
        for result in results:
            print(result)
    else:
        results = cursor.execute("""
            SELECT employee.LastName, employee.DepartmentID, department.DepartmentName 
            FROM employee, department
            WHERE employee.DepartmentID = department.DepartmentID;
        """).fetchall()
        print("Results of Implicit")
        for result in results:
            print(result)