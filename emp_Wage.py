from random import Random


def Main():
    ispresent = 1
    random = Random()

    empCheck = random.randint(0, 2)
    if empCheck is ispresent:
        print("employee is present")

    else:
        print("employee is absent")
        return empCheck


if __name__ == "__main__":
    Main()