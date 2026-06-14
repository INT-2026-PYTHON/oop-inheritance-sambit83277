# 2. Employee Class with Instance, Class & Static Methods 
class Employee:
    company = "Acme Corp"   # Class attribute
    raise_pct = 5           # Class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)

    # Instance method
    def apply_raise(self):
        self.salary += self.salary * (Employee.raise_pct / 100)
        
    @classmethod
    def set_raise_percentage(cls, new_pct):
        cls.raise_pct = new_pct

    @classmethod
    def from_string(cls, csv_line):
        name, salary = csv_line.split(",")
        return cls(name, float(salary))

    @staticmethod
    def is_valid_salary(amount):
        return isinstance(amount, (int, float)) and amount > 0
e1 = Employee("Alice", 100000)
e2 = Employee("Bob", 80000)
e3 = Employee.from_string("Carol,75000")
for emp in (e1, e2, e3):
    emp.apply_raise()
Employee.set_raise_percentage(10)
for emp in (e1, e2, e3):
    emp.apply_raise()
for emp in (e1, e2, e3):
    print(f"{emp.name} -> {emp.salary}")
print(f"is_valid_salary(50000)  -> {Employee.is_valid_salary(50000)}")
print(f"is_valid_salary(-100)   -> {Employee.is_valid_salary(-100)}")
print(f'is_valid_salary("abc")  -> {Employee.is_valid_salary("abc")}')