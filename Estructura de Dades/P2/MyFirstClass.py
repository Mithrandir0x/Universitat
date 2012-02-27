# -*- coding: iso-8859-15 -*-

class MyFirstClass:  # <--- Class definition.
                     # <--- The character ':' defines the beginnning
                     #      of the class definition.

    def __init__(self): # <--- Class Constructor

        self.v = 10 # <--- Defines a variable and set it to 10
                    #      'self' is the reference to the object itself
                    #      so that 'v' is part of the object instance.
        
        
    def setV(self,value): # <--- Defines a method that sets the value of 'v' to
                          #      the value of 'value'.
        
        self.v = value
        
    def printV(self): # <--- Defines a method that prints the value of 'v'
        
        print(self.v) # <--- 'print' automatically converts a number to the
                      #      sequence of characters that corresponds to the
                      #      given  number.
        
    def getV(self): # <--- Defines a method that return the value of 'v'

        return self.v #      'return' is a keyword!!!



# Class definition is OVER

# Script starts HERE

obj = MyFirstClass() # <--- Create an object instace 'obj' of the class
                     #      'MyFirstClass'. 'obj' is NOT a keyword

print(obj.v)         # <--- 'v' is public (private variables do not exist
                     #      in Python) so that I can read (and print) its value
                     #      just referring to it using the point '.'
                     #      this print '10' in the Python Shell

obj.setV(100)        # <--- Set the value of 'v' to 100, calling the set method 'setV'.

obj.printV()         # <--- Calls the method 'printV' with no parameters.
                     #      Guess what it does!
                     
obj.v = 1000         # <--- Set the value of the public variable 'v' to 1000

print(obj.getV())    # <--- Prints the value given by the mthod 'getV',
                     #      that is the value of 'v'


