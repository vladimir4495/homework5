
# Task 1
list = [1, 10, 65, 44, 33, 88]
list.sort()
print('Largest number is: ', list[-1])

#Task 2
"""
import random

point = 0
while True:
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print('point: ' +  str(point))
    answer = input(str(x) + '+' + str(y) + '=? (do the addition :')
    if answer == 'q':
        break
    elif int(answer) != x+y:
        print('No points for you!')
    else:
        print('Good job.')
    point += 1
"""

#Task 3

nl=[]
for x in range(1, 100):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


