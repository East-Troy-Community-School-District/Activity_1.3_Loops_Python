'''
Sum Numbers
Pawelski
3/15/2023
Python II

Instructions:
How could we use the while loop in this program in other
programs?

Modify the program so that you can also enter "y" or "yes"
to get the loop to repeat.
'''

repeat = "Y"
total = 0
while repeat == "Y":
    number = int(input("Enter a number >> "))
    total += number
    repeat = input("Would you like to enter another number? (Y/N) >> ")
print("The sum of the numbers is:", total)
