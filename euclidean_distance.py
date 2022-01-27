import math
count = 0
while count == 0:
    try:
        x = input('Enter the x co-ordinate : ')
        y = input('Enter the y co-ordinate : ')
        euclidean_dist = math.sqrt(pow(int(x),2) + pow(int(y),2))
        print('Euclidean Dist from origin : ', euclidean_dist)
        break

    except ValueError:
        print('Enter correct value')