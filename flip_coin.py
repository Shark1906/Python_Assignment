from random import random

print('Enter the number of flipcoin')
n = input()
if(int(n) > 0):

    head = 0
    tail = 0
    for i in range(0, int(n)):
        if(random() > 0.5):
            head += 1
        else:
            tail += 1
    temp = "Head {} : Tail {}".format((head/int(n))*100, (tail/int(n))*100)
    print(temp)
else:
    print('Enter number greater than zero')