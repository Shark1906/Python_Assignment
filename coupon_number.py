import math
from random import random

class Coupon_Number:
    @staticmethod
    def get_random():
        return math.floor(random()*100)
    
    @classmethod
    def generate_coupons(self, N):
        self.N = N
        coupons = []
        count = 0
        while count != N:
            coupon = Coupon_Number.get_random()
            if not coupons.__contains__(coupon):
                coupons.append(coupon)
                count+=1
        print(coupons)

N = input('Enter the number of coupons you want : ')
Coupon_Number.generate_coupons(int(N))
