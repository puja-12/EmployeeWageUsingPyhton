from random import Random


def Dailywage():
    IS_FULL_TIME = 1
    EMP_RATE_PER_HOUR = 20
    random = Random()
    # computation
    empCheck = random.randint(0, 2)
    if empCheck == IS_FULL_TIME:
        empHrs = 8
    else:
        empHrs = 0
    empWage = empHrs * EMP_RATE_PER_HOUR
    print("Emp Wage :" + str(empWage))
    return empWage


if __name__ == "__main__":
    Dailywage()