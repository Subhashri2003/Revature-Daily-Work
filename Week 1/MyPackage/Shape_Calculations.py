""" Area,Circumference of sq,rect,circle"""
from math import pi
"""
Area of square
:param side: side of square
:return:Area
"""

def area_of_square(side):
    return side**2

def area_of_circle(radius):
    return pi*radius*radius

def area_of_rect(length,breadth):
    return length*breadth

