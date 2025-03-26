class Employee:
    def __init__(self, employee_id, first_name, last_name):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name

        self._salary = None

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary > 0:
            self._salary = salary
        else:
            err = f"Invalid salary value: {salary}"
            raise ValueError(err)


karel = Employee(1, "Karel", "Novak")
print(f"First name: {karel.first_name}")



