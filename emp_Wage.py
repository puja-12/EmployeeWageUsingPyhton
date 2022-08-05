from random import Random


class TotalSalary:
    def __init__(self, Company, wagePerHour, maxWorkingDays, maxWorkingHours):
        # instance fields found by C# to Python Converter:
        self._wagePerHour = 20
        self._workingHours = 0
        self._workingDaysPerMonth = 0
        self._maxWorkingDays = 0
        self._maxWorkingHours = 0
        self._Company = None
        self._totalSalary = 0

        self._Company = Company
        self._wagePerHour = wagePerHour
        self._maxWorkingDays = maxWorkingDays
        self._maxWorkingHours = maxWorkingHours

    def salary(self):

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

        while (self._workingHours < self._maxWorkingHours) and (self._workingDaysPerMonth < self._maxWorkingDays):

            if isPresent == 1:
                # Console.WriteLine("Employee is present and working Full Time!")
                self._workingHours += 8
            elif isPresent == 2:
                # Console.WriteLine("Employee is present and working Part Time!")
                self._workingHours += 4
            elif isPresent == 0:
                # Console.WriteLine("Employee is Absent!")
                self._workingHours = 0
                # Console.WriteLine("Something went wrong!!")
            self._workingDaysPerMonth += 1
        print("Total Working Hours : " + str(self._workingHours))
        print("Total working Days Per Month : " + str(self._workingDaysPerMonth))
        totalSalary = self._wagePerHour * self._workingHours
        print("Total Salary of Employee per Month ", self._Company, "is", totalSalary)


if __name__ == "__main__":
    Amazon = TotalSalary("Amazon", 20, 5, 100)
    Amazon.salary()
    BridgeLabs = TotalSalary("Bridge Labs", 25, 5, 120)
    BridgeLabs.salary()
