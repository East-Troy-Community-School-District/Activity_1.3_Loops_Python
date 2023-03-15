'''
Break
Pawelski
3/15/2023
Python II

Instructions:
Modify the program so that it doesn't use the break keyword.
'''

while True:
    repeat = input("Do you have work today? (Y/N) >> ")
    if repeat == "Y":
        print("Another day another dollar...")
    else:
        print("Vacation time!")
        break