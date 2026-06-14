# 4. Person -> Employee -> Manager (Multi-Level Inheritance)  
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}, age {self.age}"

    @staticmethod
    def is_adult(age):
        return age >= 18


class Employee(Person):
    company = "Acme Corp"
    bonus_pct = 5

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = float(salary)

    def work_intro(self):
        return f"I work at {Employee.company} as id {self.emp_id}"

    def apply_bonus(self):
        self.salary += self.salary * Employee.bonus_pct / 100

    @classmethod
    def set_bonus(cls, new_pct):
        cls.bonus_pct = new_pct


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, team):
        super().__init__(name, age, emp_id, salary)
        self.team = team

    def add_member(self, employee):
        self.team.append(employee)

    def team_intro(self):
        return f"I lead a team of {len(self.team)} people."

    def team_total_salary(self):
        total = self.salary

        for employee in self.team:
            total += employee.salary

        return total
p = Person("Sam", 17)
e1 = Employee("Alice", 25, "E001", 100000)
e2 = Employee("Bob", 30, "E002", 80000)
m = Manager("Carol", 40, "M001", 150000, [])
m.add_member(e1)
m.add_member(e2)
print(p.greet())
print()
print(e1.greet())
print(e1.work_intro())
print()

print(e2.greet())
print(e2.work_intro())
print()
print(m.greet())
print(m.work_intro())
print(m.team_intro())
print()

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()
print(f"Alice salary -> {e1.salary}")
print(f"Bob salary   -> {e2.salary}")
print(f"Carol salary -> {m.salary}")
print()
Employee.set_bonus(10)
e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()

print("After changing bonus to 10%:")
print(f"Alice salary -> {e1.salary}")
print(f"Bob salary   -> {e2.salary}")
print(f"Carol salary -> {m.salary}")
print()
print(f"is_adult(17) -> {Person.is_adult(17)}")
print(f"is_adult(25) -> {Person.is_adult(25)}")
print(f"is_adult({p.age}) -> {Person.is_adult(p.age)}")
print(f"is_adult({m.age}) -> {Person.is_adult(m.age)}")
print()
print(f"Team total salary -> {m.team_total_salary()}")