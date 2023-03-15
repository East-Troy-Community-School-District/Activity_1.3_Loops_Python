'''
Prime Number
Pawelski
3/15/2023
Python II

Instructions:
When does the else clause execute? When does it not execute?
'''


number = int(input("Enter a number >> "))
for i in range(2, number):
    if number % i == 0:
        print(number, "is divible by", i)
        break
else:
    print(number, "is a prime number")
