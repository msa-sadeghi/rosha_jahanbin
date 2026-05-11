# class BankAcount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance
#         self.__transactions = []

#     @property
#     def balance(self):
#         return self.__balance
#     @property
#     def transactions(self):
#         return self.__transactions

#     def do_some_transaction(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"-{amount}")
#             return True
#         return False


# b1 = BankAcount("sara", 1000)
# b2 = BankAcount("reza", 10000)

# print(f"{b1.owner}, {b1.balance}")
# print(f"{b2.owner}, {b2.balance}")

# if b1.do_some_transaction(500):
#     print(f"transaction successfuly done")
#     print(b1.transactions)


# class Employee:
#     def __init__(self, name, emp_id, base_salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.base_salary = base_salary

#     def calculate_salary(self):
#         return self.base_salary


# class Developer(Employee):
#     def __init__(self, name, emp_id, base_salary, projects_completed=0):
#         super().__init__(name, emp_id, base_salary)
#         self.projects_completed = projects_completed

#     def calculate_salary(self):
#         bonus = self.projects_completed * 500
#         return self.base_salary + bonus


# class Manger(Employee):
#     def __init__(self, name, emp_id, base_salary, team_size):
#         super().__init__(name, emp_id, base_salary)
#         self.team_size = team_size

#     def calculate_salary(self):
#         bonus = self.team_size * 300
#         return self.base_salary + bonus


# employees = [
#     Developer('hos', 'D001',15_000_000, projects_completed=3),
#     Manger('sara', 'M001', 20_000_000, team_size=5),
#     Developer('maryam', "D002", 15_000_000,  projects_completed=5)
# ]

# print(f"{employees[0].name} has {employees[0].projects_completed} projects completed and his salary is {employees[0].calculate_salary()}")

# sum_of_all_salary = 0
# for emp in employees:
#     sum_of_all_salary += emp.calculate_salary()

# print("total salary is:", sum_of_all_salary)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#     def __repr__(self):
#         return f"Vector ({self.x}, {self.y})"
#     def __mul__(self, other):
#         return Vector(self.x * other.x, self.y * other.y)

# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# v3 = v1 + v2
# print(v3.x, v3.y)
# print(v3)
# print(v1 * v2)

# n1 = int(input("enter a number: "))
# n2 = int(input("enter a number: "))
# n3 = int(input("enter a number: "))

# maxi = n1
# if n2 > maxi:
#     maxi = n2
# if n3 > maxi:
#     maxi = n3
# print("max is ", maxi)


# x = input("enter a number: ")
# result = 0
# for digit in  x :
#     result += int(digit)

# print(result)

# x = int(input("enter a number: "))
# result = 0
# while x != 0:
#      result += x % 10
#      x //= 10
# print(result)


# n = int(input("enter "))
# r = 0
# for i in range(1, n):
#      r += i
# print(r)
     
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()