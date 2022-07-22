from random import Random


def emplWage():
    IS_PART_TIME = 1
    IS_FULL_TIME = 2
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    totalEmpWage = 0
    for day in range(0, NUM_OF_WORKING_DAYS):
        random = Random()
        empCheck = random.randint(0, 3)
        if empCheck is IS_PART_TIME:
            empHrs = 4
        elif empCheck is IS_FULL_TIME:
            empHrs = 8
        else:
            empHrs = 0
        empWage = empHrs * EMP_RATE_PER_HOUR
        totalEmpWage += empWage
        print("Emp Wage :" + str(empWage))
    print("Total Emp Wage :" + str(totalEmpWage))
    return empWage


if __name__ == "__main__":

    emplWage()