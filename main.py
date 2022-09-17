import random

counter = 0
list1 = ['a','s','b','t']
multiple = 1
for i in range(1,len(list1)+1,1):
    multiple *= i
for i in range(multiple):
    random.shuffle(list1)
    print(''.join(list1),end=' ')
    counter += 1
    if counter == 5:
        print()
        counter = 0
