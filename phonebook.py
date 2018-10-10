from os import system


def formatNum(number):
    formattedNum = "(%s)-%s-%s" % (number[0:3], number[3:6], number[6:])
    return formattedNum


def newContact(phonebook):
    system("clear")
    # enter name
    name = raw_input("What is their good name?\n")
    if name in phonebook.keys():
        c = raw_input("This name is already in the phonebook, do you wish to replace the number? Yes or No\n")
        if (c[0].lower() != "y") and (len(c) > 0):
            newContact(phonebook)  # fix recurtion glitch

    # enter number
    number = raw_input("Whoms't are their cellular digits?\n")
    while number in phonebook.values():
        number = raw_input("This number is already in use, please enter another number.\n")
        while (len(number) != 10) or (not number.isdigit()):
            number = raw_input("please enter a legitamate number\n")
    while (len(number) != 10) or (not number.isdigit()):
        number = raw_input("please enter a legitamate number\n")
    phonebook[name] = number
    system("clear")
    return phonebook


def searchPhonebookName(phonebook):
    system("clear")
    search = raw_input("What is the name of the feller who's number you want?\n")
    if search not in phonebook.keys():
        print("Apologies, the is no contact named '%s'" % (search))
        again = raw_input("Do you want to try again? Yes or No\n")
        if (again[0].lower() == "y") and (len(again) > 0):
            searchPhonebookName(phonebook)
    else:
        formattedNum = formatNum(phonebook[search])
        print("%s's number is: %s" % (search, formattedNum))
        raw_input("hit 'enter' when done")
    system("clear")


def searchPhonebookNumber(phonebook):
    system("clear")
    search = raw_input("What is the number of the feller who's name you want?\n")
    if search not in phonebook.values():
        print("Apologies, the is no contact who's number is '%s'" % (formatNum(search)))
        again = raw_input("Do you want to try again? Yes or No\n")
        if (again[0].lower() == "y") and (len(again) > 0):
            searchPhonebookNumber(phonebook)
    else:
        name = str([name for name, number in phonebook.items() if number == search])
        print("%s's name is: %s" % (formatNum(search), name[2:-2]))
        raw_input("hit 'enter' when done")
    system("clear")


def showPhonebook(phonebook):
    system("clear")
    if len(phonebook) < 1:
        print("The phonebook is empty.")
    for i in sorted(phonebook):
        print("%s : %s" % (i, formatNum(phonebook[i])))
    raw_input("hit 'enter' when done")
    system("clear")


def deleteContact(phonebook):
    system("clear")
    delCon = raw_input("What is the name or number of the contact you want to remove?\n")
    if delCon in phonebook.keys():
        del phonebook[delCon]
    elif delCon in phonebook.values():
        for key in phonebook.keys():
            if phonebook[key] == delCon:
                del phonebook[key]
    else:
        print("There was no contact with the name or number '%s'" % (delCon))
        again = raw_input("Do you want to try again? Yes or No\n")
        if (again[0].lower() == "y") and (len(again) > 0):
            deleteContact(phonebook)
    print("The contact was removed")
    raw_input("hit 'enter' when done")
    system("clear")


def choose(phonebook):
    options = ["1", "2", "3", "4", "5", "6"]
    q = """
To add a new contact,        please press 1
To delete a contact,         please press 2
To find a contact by name,   please press 3
To find a contact by number, please press 4
To see the phonebook,        please press 5
To exit the program,         please press 6\n\n"""

    print("Hello")
    opt = raw_input(q)

    if opt in options:
        if opt == options[0]:
            phonebook = newContact(phonebook)
        if opt == options[1]:
            deleteContact(phonebook)
        if opt == options[2]:
            searchPhonebookName(phonebook)
        if opt == options[3]:
            searchPhonebookNumber(phonebook)
        if opt == options[4]:
            showPhonebook(phonebook)
        if opt == options[5]:
            quit()

        choose(phonebook)
    else:
        print("Please enter a valid option")
        system("clear")
        choose(phonebook)


def main():
    phonebook = {}
    choose(phonebook)


main()
