from functions import *
def main():
    n = int(input("Enter your grade: "))
    if n in range(0,101):
        grade(n)
    else:
        print('Invalid input')
        main()
main()