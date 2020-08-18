def main():
    showMenu()
    print('Please choose an option...')
    
def showMenu():
    print('Password Manager')
    print('====================')
    print('1) Add new combination')
    print('2) Remove combination')
    print('3) Check existing combinations')

def chooseChoice(choice):
    if choice == 1:
        print('1')
    elif choice == 2:
        print('2')
    elif choice == 3:
        print('3')
    else: 
        print('none here')


if __name__ == '__main__':
    main()