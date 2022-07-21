from random import Random


def partTime():
    IS_FULL_TIME = 2
    EMP_RATE_PER_HOUR = 20
    IS_PART_TIME = 1
    random = Random()
    empCheck = random.randint(0, 3)
    if empCheck is IS_PART_TIME:
        empHrs = 4
    elif empCheck is IS_FULL_TIME:
        empHrs = 8
    else:
        empHrs = 0
    empWage = empHrs * EMP_RATE_PER_HOUR
    print("Emp Wage :" + str(empWage))

    return empWage


if __name__ == "__main__":
    partTime()