class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, sort_param):
    if sort_param == 1:  # Sort by Age
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_param == 2:  # Sort by Name
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_param == 3:  # Sort by Salary
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Employee Sorting Options:")
    print("1. Sort by Age")
    print("2. Sort by Name")
    print("3. Sort by Salary")

    try:
        sort_param = int(input("Enter your choice (1/2/3): "))
        sorted_employees = sort_employees(employees, sort_param)

        print("\nSorted Employee Data:")
        for emp in sorted_employees:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    except ValueError as e:
        print("Invalid input. Please choose a valid sorting parameter (1/2/3).")

if __name__ == "__main__":
    main()
