'''
编程实现牛顿法求解非线性方程 请先设计接口，编程实现，并求解下列方程的解。
2*x^2+10*e^(-x)-5=0
'''

import sympy
import math

x = symbols('x')

def solution(func):
    while True:
        sympy.diff(f(x), x)

def f(x):
    f = 2 * x ** 2 + 10 * math.exp(-x) - 5
    return f
