import os
import json


class Company:

    def __init__(self, company_name):
        self.emp_dict = {}
        self.com_name = company_name
        self.filename = 'employee.json'

    def add_emp_details(self):
        """Adding details provided by the user in our employee file"""

        global employee_detail
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                employee_detail = open(self.filename, 'r')
                data = json.load(employee_detail)
                employee_detail.close()
            else:
                employee_detail = open(self.filename, 'w')
                data = {}

            employee_detail = self.get_details_from_user()
            data[employee_detail['emp_id']] = employee_detail
            employee_detail = open(self.filename, 'w')
            json.dump(data, employee_detail, indent=4)
            employee_detail.close()

            print('Contact Added Successfully!')
        except Exception as e:
            print('There was an error! Contact was not added.')
            print(e)
        finally:
            employee_detail.close()

    def get_details_from_user(self):
        """Getting the details from the user to adding the employess"""

        try:

            self.emp_dict['emp_name'] = str(input('Enter  employee full name: '))
            self.emp_dict['emp_id'] = int(input('Enter  employee id: '))
            self.emp_dict['emp_salary'] = str(input('Enter employee salary: '))
            self.emp_dict['emp_phone'] = int(input('Enter employee Phone Number: '))
            return self.emp_dict
        except Exception as error:
            raise error

    def display_all_emp_details(self):
        """To display ALL the employee details in our employee file"""

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
            company.add_emp_details()
        elif choice == 2:
            company.display_all_emp_details()
        else:
            print("choose correct option")
