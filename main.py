# While loop for decision 1: make sure the user is sure about their choice


import database


def main():
    showMenu()
    chooseChoice(input('Please choose an option... \n'))


def showMenu():
    print('Password Manager')
    print('====================')
    print('1) Add new combination')
    print('2) Remove combination')
    print('3) Change existing combinations')
    print('4) Check existing combinations')


def chooseChoice(choice):
    choice = int(choice)

    if choice == 1:
        handleRegister()

    elif choice == 2:
        print('choice 2')

    elif choice == 3:
        print('choice 3')

    elif choice == 4:
        database.showRecords()

    else:
        chooseChoice(input('Not a valid choice, please try again... \n'))


def handleRegister():
    while True:
        domain = input('New domain name... \n')
        password = input('New password... \n')
        print('Domain: ' + domain + '\nPassword: ' + password)

        choice = int(
            input('Are you sure about these combinations? \n1: YES Else: NO\n'))
        if choice == 1:
            break

    database.addRecord(domain, password)


if __name__ == '__main__':
    main()
