def grade(n):
    if n >= 40 and n< 60 :
        print(f"Your grade is {n} so that is 'Good'")
    elif n >= 60 and n< 75 :
        print(f"Your grade is {n} so that is 'Very good'")
    elif n >= 75 and n<= 100 :
        print(f"Your grade is {n} so that is 'Excellent'")
    elif n < 40:
        print(f"Your grade is {n} so that is 'Fail'")