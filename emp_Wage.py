from random import Random


def employeeWage():
    empwageperhrs = 20
    emphrs = 0
    workingdays = 0

    ispresent = 1
    random = Random()

    empCheck = random.randint(0, 2)
    if empCheck == ispresent:
        print("employee is present")

    else:
        print("employee is absent")

    if empCheck == 1:
        emphrs += 8
    elif empCheck == 2:
        emphrs += 4
    elif empCheck == 0:

        emphrs = 0
    else:
        print("error")
    workingdays += 1

    print("Total Working Hours : " + str(emphrs))
    print("Total working Days Per Month : " + str(workingdays))
    monthsalary = empwageperhrs * emphrs
    print("Total Salary of Employee per Month : " + str(monthsalary))


if __name__ == "__main__":
    employeeWage()
