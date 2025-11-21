'''You’re building a small program for a school. The user must enter the student’s name and marks in three subjects. The program should calculate the total, average, and display a grade. If marks are not between 0 and 100, show an error message. Concepts: Input/Output, data validation, arithmetic, if–elif–else.'''
name=str(input("Enter the name of the student.."))
try:
    s1=float(input("enter the marks of first subject."))
    s2=float(input("enter the marks of second subject."))
    s3=float(input("enter the marks of third subject."))
    if (0 <= s1 <= 100 and 0 <= s2 <= 100 and 0 <= s3 <= 100):
        pass
    else:
        print("Error! enter the marks between 0 to 100.")
        exit()
except ValueError:
    print("invalid input! please enter a number.")
    exit()
total=s1+s2+s3
avarage=total/3
print(f"the total marks are {total}")
print(f"the avarage marks are {avarage}")
def grade(x):
    if x>90:
        return "The grade is A."
    elif x>80:
        return "The grade is B."
    elif x>65:
        return "The grade is C."
    elif x>35:
        return "The grade is D."
    else:
        return "The grade is F."  
print(f"The grade is {grade(avarage)}")