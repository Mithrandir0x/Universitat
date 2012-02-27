# -*- coding: iso-8859-15 -*-

#
# MySecondClass.py
#
# author: olopezsa13
#

"""
This class wraps a vector and contains several methods to manipulate
it and display it.
"""
class MySecondClass:
    def __init__(self):
        self.v = []

    def add(self, element):
        self.v.append(element)

    def getV(self):
        return self.v

    def printV(self):
        print self.v

# VISUAL ASSERTION!!
#
# Because human eye cannot ever fail...

mySecondClass = MySecondClass()

mySecondClass.add(2)

print mySecondClass.getV()
mySecondClass.printV()

mySecondClass.add(3)

print mySecondClass.getV()
mySecondClass.printV()

mySecondClass.add('Hello World')

print mySecondClass.getV()
mySecondClass.printV()
