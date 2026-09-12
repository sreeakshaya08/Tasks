class Employee:

    def __init__(self, employee_id, name, basic_salary):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        self.hra = self.basic_salary * 0.20
        self.da = self.basic_salary * 0.10
        self.bonus = self.basic_salary * 0.05

        self.total_salary = (
            self.basic_salary +
            self.hra +
            self.da +
            self.bonus
        )

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Basic Salary: ₹", self.basic_salary)
        print("HRA: ₹", self.hra)
        print("DA: ₹", self.da)
        print("Bonus: ₹", self.bonus)
        print("Total Salary: ₹", self.total_salary)
        print("------------------------")



employee1 = Employee(101, "Akshaya", 30000)
employee2 = Employee(102, "Priya", 40000)
employee1.calculate_salary()
employee2.calculate_salary()
employee1.display_details()
employee2.display_details()