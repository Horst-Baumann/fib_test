# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:18:38 2018

@author: baumann
"""

import fibo

def test_fibo_10():
    result_10 = fibo.fib2(10)
    expected_result = [0,1,1,2,3,5,8]
    assert result_10 == expected_result


def test_fibo_0():
    result_0 = fibo.fib2(0)
    expected_result = []
    assert result_0 == expected_result


def test_fibo_5():
    result = fibo.fib2(5)
    expected_result = [0,1,1,2,3]
    assert result  == expected_result
    
def test_fib_type():
    result = fibo.fib2(0)

    assert type(result) == list
    
test_fibo_10()
test_fibo_0()
"""
result3000 = fibo.fib2(3000)
print(result3000)

result0 = fibo.fib2(0)
print(result0)
"""