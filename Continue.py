'''
Continue
Pawelski
3/15/2023
Python II

Instructions:
Modify the program so that it uses the mod operator instead
of the continue keyword.

Modify the program again so that it doesn't use the mod operator
or the continue keyword.
'''

for i in range(1, 11):
    if i % 2 == 0:
        continue
    else:
        print(i)
