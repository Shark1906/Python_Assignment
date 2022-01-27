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
        for i in range(0, N):
            coupons.append(Coupon_Number.get_random())
            for j in range(N, -1):
                if coupons[i] == coupons[j]:
                    coupons[i] = Coupon_Number.get_random()
        print(coupons)

N = input('Enter the number of coupons you want : ')
Coupon_Number.generate_coupons(int(N))
