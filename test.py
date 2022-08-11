from company import *



class TestEmployee:

    def test_add_emp(self):
        company = Company("amazon")

        employee = Employee({'emp_name': "Rahul", 'emp_id': "1", 'emp_salary': "2000", 'emp_phone': '12345678'})
        assert len(company.emp_dict) == 0
        company.add_emp(employee)
        assert len(company.emp_dict) == 1

    def test_delete(self):
        company = Company("amazon")

        employee = Employee({'emp_name': "Pooja", 'emp_id': "2", 'emp_salary': "2000", 'emp_phone': '12345678'})
        company.add_emp(employee)
        assert len(company.emp_dict) == 1
        company.delete(employee.emp_id)
        assert len(company.emp_dict) == 0

    def test_edit(self):
        company = Company("amazon")

        employee = Employee({'emp_name': "Shweta", 'emp_id': "3", 'emp_salary': "2000", 'emp_phone': '12345678'})
        assert employee.emp_id == "3"
        company.edit(employee.emp_name, employee.emp_salary,employee.emp_id, employee.emp_phone)
        employee.emp_name = 'Rahul'
        assert employee.emp_name == "Rahul"
