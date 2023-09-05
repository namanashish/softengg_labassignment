class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, operator, age):
        results = []
        for employee in self.employees:
            if operator == '<' and employee.age < age:
                results.append(employee)
            elif operator == '>' and employee.age > age:
                results.append(employee)
            elif operator == '<=' and employee.age <= age:
                results.append(employee)
            elif operator == '>=' and employee.age >= age:
                results.append(employee)
        return results

    def search_by_salary(self, operator, salary):
        results = []
        for employee in self.employees:
            if operator == '<' and employee.salary < salary:
                results.append(employee)
            elif operator == '>' and employee.salary > salary:
                results.append(employee)
            elif operator == '<=' and employee.salary <= salary:
                results.append(employee)
            elif operator == '>=' and employee.salary >= salary:
                results.append(employee)
        return results

    def search_by_emp_id(self, emp_id):
        results = []
        for employee in self.employees:
            if employee.emp_id == emp_id:
                results.append(employee)
        return results

if __name__ == "__main__":
    database = EmployeeDatabase()

    # Adding employees to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    # User input for search
    search_option = int(input("Select a search option:\n1. Search by Age\n2. Search by Salary\n3. Search by Employee ID\n"))

    if search_option == 1:
        operator = input("Enter operator (<, >, <=, >=): ")
        age = int(input("Enter age: "))
        results = database.search_by_age(operator, age)
    elif search_option == 2:
        operator = input("Enter operator (<, >, <=, >=): ")
        salary = float(input("Enter salary: "))
        results = database.search_by_salary(operator, salary)
    elif search_option == 3:
        emp_id = input("Enter Employee ID: ")
        results = database.search_by_emp_id(emp_id)
    else:
        print("Invalid option")

    if results:
        print("\nSearch Results:")
        for result in results:
            print(f"{result.emp_id},{result.name},{result.age},{result.salary}")
    else:
        print("No results found.")
