from random import Random


class TotalSalary:

    def __init__(self):

        self._wagePerHour = 20
        self._workingHours = 0
        self._workingDaysPerMonth = 0
        self._maxWorkingDays = 0
        self._maxWorkingHours = 0
        self._Company = None

    def salary(self, Company, wagePerHour, maxWorkingDays, maxWorkingHours):

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

        while (self._workingHours < maxWorkingHours) and (self._workingDaysPerMonth < maxWorkingDays):

            if isPresent == 1:

                self._workingHours += 8
            elif isPresent == 2:

                self._workingHours += 4
            elif isPresent == 0:

                self._workingHours = 0

        self._workingDaysPerMonth += 1
        print("Total Working Hours : " + str(self._workingHours))
        print("Total working Days Per Month : " + str(self._workingDaysPerMonth))
        totalSalary = wagePerHour * self._workingHours
        print("Total Salary of Employee per Month ", Company, totalSalary)


if __name__ == "__main__":
    total = TotalSalary()

    print("Welcome to Employ Wage Computation Program!")
    total.salary("Amazon", 20, 20, 100)
    total.salary("Bridgelabz", 18, 21, 80)
    total.salary("TCS", 19, 24, 90)
