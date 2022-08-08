from random import Random


class Employee:

    def __init__(self, data: dict):
        self.com_name = data.get("company_name")
        self.emp_name = data.get("emp_name")
        self.emp_id = data.get("emp_id")
        self.emp_salary = data.get("emp_salary")
        self.emp_phone = data.get("emp_phone")
        print(data)

    # def details(self):
    #     return f"{self.company_name},{self.wagePerHour},{self.maxWorkingDays},{self.maxWorkingHours}"


class Company:
    def __init__(self):
        self.emp_dict = {}

    def add_contacts(self, contact_object):
        self.emp_dict.update({contact_object.company_name: contact_object})


#     def all_values(self):
#         """
#             function to read all contacts from dictionary
#             """
#         # Iterate over all values of the dictionary
#         for key, value in self.emp_dict.items():
#             print(key, value.details())


if __name__ == "__main__":
    # company = Company()
    # print("Enter the company name :")
    # com_name = input()
    # print("Enter the emp_name :")
    # emp_name = input()
    # print("Enter the emp_id :")
    # emp_id = input()
    # print("Enter the emp_salary :")
    # emp_salary = input()
    # print("Enter the emp_phone :")
    # emp_phone = input()
    # emp = Employee ()
    # company.add_contacts()
    emp = Employee("company_name"="amazon")


