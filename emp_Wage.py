import os
import json


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


class Company:
    # emp = Employee(self.as_dict())

    def __init__(self, company_name):
        self.emp_dict = {}
        self.com_name = company_name
        self.filename = 'employee.json'

    def add_contacts(self):

        global employee_detail
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                employee_detail = open(self.filename, 'r')
                data = json.load(employee_detail)
                employee_detail.close()
            else:
                employee_detail = open(self.filename, 'a')
                data = {}

            contact = self.get_details_from_user()
            data[contact['com_name']] = contact
            employee_detail = open(self.filename, 'a')
            json.dump(data, employee_detail)
            employee_detail.close()

            print('Contact Added Successfully!')
        except Exception as e:
            print('There was an error! Contact was not added.')
            print(e)
        finally:
            employee_detail.close()

            # Getting the details from the user to adding the employess

    def get_details_from_user(self):
        try:
            self.emp_dict['com_name'] = str(input('Enter Contact\'s company Name: '))
            self.emp_dict['emp_name'] = str(input('Enter Contact\'s Full Name: '))
            self.emp_dict['emp_id'] = str(input('Enter Contact\'s emp_id: '))
            self.emp_dict['emp_salary'] = str(input('Enter Contact\'s emp_salary: '))
            self.emp_dict['emp_phone'] = int(input('Enter Contact\'s Phone Number: '))
            return self.emp_dict
        except KeyboardInterrupt as error:
            raise error

    def display_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            employee_detail = open(self.filename, 'r')
            data = json.load(employee_detail)
            employee_detail.close()
            if data:
                for records in data.values():
                    print(records)
            employee_detail.close()
        else:
            print('No Record in database.')


if __name__ == "__main__":
    company = Company("amazon")
    print("1 to Add contact, \n2 to display contact")

    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            company.add_contacts()
        elif choice == 2:
            company.display_contacts()
