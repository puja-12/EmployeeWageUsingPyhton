from employee import Employee
import json
import os

TABLE = "{:<15}{:<15}{:<15}{:<15}"


class JsonOperation:
    filename = "db.json"

    @classmethod
    def read(cls):
        if os.path.exists(cls.filename) and os.path.getsize(cls.filename) > 0:
            with open(cls.filename) as file:
                data = json.load(fp=file)
                if not data:
                    data = {}
                return data

    @classmethod
    def write(cls, data):
        with open(cls.filename, 'w') as file:
            json.dump(data, fp=file)


class Company:
    def __init__(self, com_name):
        self.com_name = com_name
        self.emp_dict = self.read_file()

    def add_emp(self, emp_object):
        self.emp_dict.update({emp_object.emp_id: emp_object})
        self.update_file()

    def update_file(self):
        # print(list(self.emp_dict.values()))
        data = {}
        for key, value in self.emp_dict.items():
            data.update({key: value.as_dict()})

        JsonOperation.write(data)

    def read_file(self):
        data = JsonOperation.read()
        if not data:
            data = {}
        new_data = {}
        for key, value in data.items():
            new_data.update({key: Employee(value)})
            # print(value)
            # print(Employee(value))

        return new_data

    def display(self):
        print(TABLE.format("emp_name", "emp_id", "emp_salary", "emp_phone"))
        for key, value in self.emp_dict.items():
            print(TABLE.format(*value.as_list()))

    def get_emp(self, emp_id):
        return self.emp_dict.get(emp_id)

    def edit(self, emp_id,emp_name,emp_salary,emp_phone):
        emp_details = self.get_emp(emp_id)
        if not emp_details:
            print("emp id is not present")
            return

        emp_details.emp_name = emp_name
        emp_details.emp_salary = emp_salary
        emp_details.emp_phone = emp_phone
        print("updated successfully")

    def delete(self, emp_id):
        data = self.get_emp(emp_id)
        if not data:
            print("given id not exists")
            return
        self.emp_dict.pop(emp_id)

        print("contact deleted successfully")


if __name__ == '__main__':
    comp = Company("amazon")

    print("1 to Add employee details, \n2 to display employee contact"
          "\n3 For edit the details \n4. For delete emp details")
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            data = {'emp_name': input(), 'emp_id': input(), 'emp_salary': input(), 'emp_phone': input()}
            employee = Employee(data)
            print("Enter the employee name :")
            employee.emp_name = input()
            print("Enter the employee id :")
            employee.emp_id = input()
            print("Enter the  salary:")
            employee.emp_salary = input()
            print("Enter the Phone Number :")
            employee.emp_phone = input()
            comp.add_emp(employee)
        elif choice == 2:
            comp.display()
        elif choice == 3:
            key = input("Enter key to check:")
            print("given name contact exists")
            print("Please enter the employee name : ")
            emp_name = input()
            print("Please enter the emp_salary : ")
            emp_salary = input()
            print("Please enter the Phone Number : ")
            emp_phone = input()
            comp.edit(key, emp_name, emp_salary, emp_phone)
        elif choice == 4:
            emp_id = input("Enter emp id to check:")
            comp.delete(emp_id)
        elif choice == 5:
            print("enter correct option")



