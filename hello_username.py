'''
@Author: Aman Raj
@Date: 2022-01-24 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2022-01-24 18:00:30
@Title : Replace username with hello message
'''
from random import random
import re

user_name = input('Enter your name : ')
temp = "Hello {}, How are you?".format(user_name)
is_match = re.match('^[A-Z]{1}[a-z]{2,}$', user_name)
if is_match :
    print(temp)
else :
    print('Invalid name')