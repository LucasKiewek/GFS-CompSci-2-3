from os import system


class Employee:
    eCount = 0
    defaultSalary = 50000
    mattZippins = 0
    other = 0

    def __init__(self, name, salary, job):

        self.name = name
        if salary.isdigit():
            self.salary = int(salary)
        else:
            self.salary = Employee.defaultSalary
        Employee.eCount += 1

        self.job = job
        if self.job == "Matt Zippin":
            Employee.mattZippins += 1
        else:
            Employee.other += 1

    def displayCount():
        print(Employee.eCount)

    def displayEmployee(self):
        print("Name: %s Salary: %i Job: %s" % (self.name, self.salary, self.job))


def main():

    employees = []
    x = True
    while x:
        options = ["1", "2", "3", "4"]
        q = """
    To make an Employee,                                   please press 1
    To print the Employees' name, salary, and job,         please press 2
    To print the number of Employees,                      please press 3
    To exit the program,                                   please press 4\n\n
    """

        print("Hello")
        opt = raw_input(q)

        if opt in options:
            if opt == options[0]:
                name = raw_input("What is the employee's name?\n")
                salary = raw_input("What is the employee's salary?\n")
                job = raw_input("What is the employee's job?\n")
                employees.append(Employee(name, salary, job))
            if opt == options[1]:
                for i in employees:
                    i.displayEmployee()
            if opt == options[2]:
                print "Number of Employees:", Employee.eCount
            if opt == options[3]:
                quit()

        else:
            print("Please enter a valid option")
            system("clear")


main()
