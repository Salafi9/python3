#! /usr/bin/env python3
#-*-coding:utf8;-*-
__author__ = 'Ahmad Abdulnasir <ahmadabdulnasir9@gmail.com>'
__copyright__ = 'Copyright (c) 2018, salafi'
__version__ = "0.1t"

import sys
from math import sqrt

def varInsp():
    try:
        a = float(input("\tPlease enter the coefficients a: "))
        b = float(input("\tPlease enter the coefficients b: "))
        c = float(input("\tPlease enter the constant c: "))
        if a*2 == 0:
            print("Not defined quadratiic equation with a = 0")
            sys.exit(1)
        else:
            pass
        #return a, b , c
        quadratic(a,b,c)
    except ValueError as koo:
        print("Please Check Your Input ", koo)
        varInsp()

def quadratic(a,b,c):
    dis = b*b-4*a*c
    if dis > 0:
        root1 = round((-b + sqrt(dis)) / (2*a),3)
        root2 = round((-b - sqrt(dis)) / (2*a),)
        print("\nThe solutions are: {} and {} ".format(root1, root2))
    elif dis == 0:
        root1 = round((-b + sqrt(dis)) / (2*a),3)
        root2 = round((-b - sqrt(dis)) / (2*a),3)
        print("\nThe solutions are: {} and {} ".format(root1, root2))
    elif dis < 0:
        print("\nThe solutions for this equation are Complex.")
        root1 = round((-b + sqrt(dis*-1)) / (2*a),3)
        root2 = round((-b - sqrt(dis*-1)) / (2*a),3)
        print("\nThe solutions are: {}i and {}i".format(root1 , root2))

def solve():
    print("This program finds the  solutions to a quadratic equation. of the form \n\t ax^2 + bx + c = 0 ")
#    var = varInsp()
#    quadratic(var[0],var[1],var[2])
    varInsp()
if __name__ == "__main__":
    solve()
