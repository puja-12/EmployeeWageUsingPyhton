from random import Random


class TotalSalary:

    def __init__(self, company, wagePerHour, maxWorkingDays, maxWorkingHours):

        self._company = company
        self._wagePerHour = wagePerHour
        self._maxWorkingDays = maxWorkingDays
        self._maxWorkingHours = maxWorkingHours

    def salary(self):
        workingHours = 0
        workingDaysPerMonth = 0

        attendanceCheck = Random()
        isPresent = attendanceCheck.randint(0, 4)
        print(isPresent)
        if isPresent == 1:
            print("Employee is present and working Full Time!")
            # WorkingHours = 8
        elif isPresent == 2:
            print("Employee is working for part Time!")
            # WorkingHours = 4
            # if isPresent is 2 then we consider it as part time and working hours are 4
        else:
            print("Employee is Absent!")
            # WorkingHours = 0

        while (workingHours < self._maxWorkingHours) and (workingDaysPerMonth < self._maxWorkingDays):

            if isPresent == 1:

                workingHours += 8
            elif isPresent == 2:

                workingHours += 4
            elif isPresent == 0:

                workingHours = 0

            workingDaysPerMonth += 1
        print("Total Working Hours : " + str(workingHours))
        print("Total working Days Per Month : " + str(workingDaysPerMonth))
        totalSalary = self._wagePerHour * workingHours
        print("Total Salary of Employee per Month ", self._company, "is", totalSalary)


if __name__ == "__main__":
    Amazon = TotalSalary("Amazon", 20, 5, 100)
    Amazon.salary()
    BridgeLabs = TotalSalary("Bridge Labs", 25, 5, 120)
    BridgeLabs.salary()
