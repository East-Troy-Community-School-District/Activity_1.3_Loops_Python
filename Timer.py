'''
Timer
Pawelski
3/15/2023
Python II

Instructions:
What does time.sleep(1) do? What does the 1 represent?
What does print("\a") do?

Modify the program so that it starts the count at 1 and
ends at 10.

Modify the program so that it starts the count at 10 and
ends at 1.
'''

import time

for i in range(10):
    print(i)
    time.sleep(1)
print("\a")