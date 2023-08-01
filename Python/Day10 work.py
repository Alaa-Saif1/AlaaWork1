# Exception:

"""try:
    inputFile = open("q.txt", "r")
    try:
        mlti_of_n_y = []
        for line in inputFile:
            data = line.split(" ")
            s = int(data[0])
            f = int(data[1])
            w = int(data[2])
            mlti_of_n_y = (f * w)
            if mlti_of_n_y <= s:
                print("Yes")
            else:
                print("No")
                    
    finally:
        inputFile.close()
        
except IOError:
    print("Erorr: File not found!")"""
                        
# Basic

"""class Person:
    no_of_persons = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.no_of_persons += 1
        
    def descrip(self):
        return f"This Person Name Is {self.name} And {self.age} Years Old"
    
    def set_age(self, new_age):
        self.age = new_age
        
p1 = Person("Alaa", 24)
p2 = Person("Hamza", 22)
print(p1.descrip())

# Number of object created from class Person
print(Person.no_of_persons)

# To change the value of age
p2.set_age(35)
print(p2.descrip())"""

# Q1:

"""class Employee:
    
    def __init__(self, emp_name, emp_id, emp_salary,emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        
    def calculate_emp_salary(self, salary, hours_Worked):
        if hours_Worked > 50:
            OverTime = hours_Worked - 50
            OverTime_Amount = (OverTime * (salary / 50))
            return OverTime_Amount
        
        
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
        
        
    def print_emp_details(self):
        return f"This Employee Name Is {self.emp_name} And His Department is {self.emp_department} "

        

emp1 = Employee("ADAMS","E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES","E7499", 54000, "RESEARCH")
emp3 = Employee("MARTIN","E7900", 50000, "SALES")
emp4 = Employee("SMITH","E7698", 55000, "OPERATIONS")

emp1.emp_assign_department("RESEARCH")
print(emp1.print_emp_details())
print(emp2.calculate_emp_salary(54000, 70))"""

# supper class & child class

"""class Person:
    def __init__(self, name, age, address, hours):
        self.name = name
        self.age = age
        self.address = address
        self.hours = hours
        
    def class_type(self):
        return "This is Parent Class"
    
class Student(Person):
    def __init__(self,name, age, address, hours, grade):
        super().__init__(name, age, address, hours)
        self.grade = grade
        
    def class_type(self):
        return "This is Student Class"
    
        
s1 = Student("Salim", 23, "Muscat", 180, [3.1, 2.5, 2])
p1 = Person("Hamed", 36, "Muscat", 180)
print(p1.class_type())
print(s1.class_type())
print(type(s1))"""

# cls method

"""from datetime import date

class Person:
    def __init__(self, name, age, address, hours):
        self.name = name
        self.age = age
        self.address = address
        self.hours = hours
        
    def class_type(self):
        return "This is Parent Class"
    
class Student(Person):
    def __init__(self,name, age, address, hours, grade):
        super().__init__(name, age, address, hours)
        self.grade = grade
        
    def class_type(self):
        return "This is Student Class"
    
    @classmethod
    def new_student(cls, name, birth_year, address, hours, grade ):
        return cls(name, date.today().year - birth_year, address, hours, grade)
    
        
s1 = Student("Salim", 23, "Muscat", 180, [3.1, 2.5, 2])
s1.new_student("Salim", 23, "Muscat", 180, [3.1, 2.5, 2])
s2 = Student.new_student("Ali",1992, "Muscat", 180, [3.1, 2.58, 2.91])
p1 = Person("Hamed", 36, "Muscat", 180)


print(p1.class_type())
print(s1.class_type())
print(type(s1))
print(s2.age)"""

# Q2:

"""class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))

    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))

restaurant = Restaurant()

# Add items
restaurant.add_item_to_menu("Cheeseburger", 9.99)
restaurant.add_item_to_menu("Caesar Salad", 8)
restaurant.add_item_to_menu("Grilled Salmon", 19.99)
restaurant.add_item_to_menu("French Fries", 3.99)
restaurant.add_item_to_menu("Fish & Chips:", 15)
# Book table
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)
# Order items
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()
print("\nTable reserved in the Restaurant:")
restaurant.print_table_reservations()
print("\nPrint customer orders:")
restaurant.print_customer_orders()"""
    
# Q3:

"""class BankAccount:
    def __init__(self, balance, account_number, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def deposit(self, amnt):
        self.balance += amnt
        print(f"{amnt} OMR Has Been Deposited")
 
    def withsdrow(self, amnt):
        if amnt > self.balance:
            print("Not Enough Balance")
        else:
            self.balance -= amnt
            print(f"{amnt} OMR Has Been Withsdrow")
            
    def check_balance(self):
        print(f"Your Current Balance Is OMR{self.balance}")
        
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance:{self.balance} OMR\n")
        
ac1 = BankAccount(345, "01-02-2011", 50000, "Alaa Saif")
ac2 = BankAccount(1218, "11-05-2021", 15000, "Janah Musllam")
ac3 = BankAccount(4532, "12-08-2019", 30000, "Khalid Hamood")
ac4 = BankAccount(532, "18-06-2016", 300, "Sara Said")

print("Customer Details: ")
ac1.print_customer_details()
ac2.print_customer_details()
ac3.print_customer_details()
ac4.print_customer_details()


ac2.deposit(1000)
ac2.check_balance()
ac1.withsdrow(5000)
ac3.withsdrow(3400)
ac3.check_balance()"""



        
    
    
    
    
    
    
        
    
        
   
