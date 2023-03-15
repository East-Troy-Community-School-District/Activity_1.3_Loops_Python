'''
Multiplication Table
Pawelski
3/15/2023
Python II

Instructions:
How does this code execute? Also, let's dicuss what this
"{:<4}".format(product) does.
'''

for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        print("{:<4}".format(product), end="")
    print()
