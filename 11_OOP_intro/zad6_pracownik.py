class Employee:
  def __init__(self, name, lastname, position, salary, exp):
    self.name = name
    self.lastname = lastname
    self.position = position
    self.salary = salary
    self.exp = exp

  def show(self):
    print(f"{self.name} {self.lastname} | {self.position }")
    print(f"{self.salary} PLN - exp: {self.exp} years")

  def salary_bump(self):
    self.salary = self.salary * 1.11
    print('New salary: ', self.salary)

p1 = Employee('Jan', 'Kowalski', 'QA', 4500, 1.5)
p1.show()
print("------ bump ------")
p1.salary_bump()
p1.show()