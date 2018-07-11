# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:17:45 2018

@author: baumann
"""


def fib(n):    # write Fibonacci series up to n
   a, b = 0, 1
   while a < n:
       print(a, end=' ')
       a, b = b, a+b
   print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
       result.append(a)
       a, b = b, a+b
    #result.append(23)
    return result