class Employee:

    def __init__(self, data: dict):
        self.emp_name = data.get("emp_name")
        self.emp_id = data.get("emp_id")
        self.emp_salary = data.get("emp_salary")
        self.emp_phone = data.get("emp_phone")

    def details(self):
        return f"{self.emp_name},{self.emp_id},{self.emp_salary},{self.emp_phone}"

    def as_dict(self):
        return {'emp_name': self.emp_name, 'emp_id': self.emp_id,
                'emp_salary': self.emp_salary, 'emp_phone': self.emp_phone}

    def as_list(self):
        return [self.emp_name, self.emp_id,
                self.emp_salary, self.emp_phone]
