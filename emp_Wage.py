from random import Random


def totalWage():
    IS_PART_TIME = 1
    IS_FULL_TIME = 2
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 2
    MAX_HRS_IN_MONTH = 10
    totalempHrs = 0
    totalWorkingDays = 0
    while totalempHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
        totalWorkingDays += 1
        random = Random()
        empCheck = random.randint(0, 3)
        if empCheck is IS_PART_TIME:
            empHrs = 4
        elif empCheck is IS_FULL_TIME:
            empHrs = 8
        else:
            empHrs = 0

        totalempHrs += empHrs
        print("Day#:" + str(totalWorkingDays) + "empHrs : " + str(empHrs))
    totalempWage = totalempHrs * EMP_RATE_PER_HOUR
    print("totalempWage :" + str(totalempWage))
    return totalempWage


if __name__ == "__main__":

    totalWage()
