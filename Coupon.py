#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
l1=range(65,91)
l2=range(97,123)
lst=l1+l2
print 'Your Coupon:'
for i in range(1,5):
    Coupon=set()
    while len(Coupon)<8:
        Coupon.add(chr(random.choice(lst)))
    Coupon="".join(Coupon)
    print Coupon

