#
# ED_P2_2012_entrega.py
#
# author: olopezsa13
#

import random
import types

class Node:
    """
    The most basic element in a bi-directional linked structure.
    """
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        """ When printing a node, it prints the content of the data. """
        return self.data.__str__()
                
class Stack:
    """
    The classic (arguably boring) implementation of a LIFO heterogeneous
    collection.
    """
    def __init__(self):
        """ When constructed, the stack is empty. """
        self.head = None

    def __str__(self):
        """ Returns a string representation of the stack's content. """
        if self.isEmpty():
            return "Empty stack."

        node, i, text = self.head, 1, ""
        while node != None:
            text += "(%s) %s\n" % (i, node)
            node = node.next
            i += 1
        return text

    def isEmpty(self):
        """ This method indicates whether the stack is empty, or not. """
        return self.head == None
       
    def push(self, data):
        """ Add the data to the first position of the collection. """
        temp = Node(data, self.head)
        self.head = temp

    def pop(self):
        """
        Remove the element at the first position.

        WARNING: Do not pop from an empty stack or an IndexError
        exception will be raised.
        """
        if self.isEmpty():
            raise IndexError("Tried to pop from an empty stack.")

        temp = self.head.data
        self.head = self.head.next
        return temp

class Queue:
    """
    An inefficient implementation of a FIFO heterogeneous collection.
    """
    def __init__(self):
        """ When constructed, the queue is empty. """
        self.head = None

    def __str__(self):
        """ Returns a string representation of the queue's content. """
        if self.isEmpty():
            return "Empty queue."

        node, i, text = self.head, 1, ""
        while node != None:
            text += "(%s) %s\n" % (i, node)
            node = node.next
            i += 1
        return text

    def isEmpty(self):
        """ Tells whether the queue is empty or not. """
        return self.head == None

    def enqueue(self, data):
        """ Queues a new element to the queue. """
        temp = Node(data, self.head)
        self.head = temp

    def dequeue(self):
        """ Removes the oldest element from the queue. """
        if self.isEmpty():
            # Raise exception if someone tries to dequeue from an empty queue.
            raise IndexError("Tried to dequeue from an empty queue.")

        if self.head.next == None:
            # Treat one-element queue as a unique case
            temp = self.head.data
            self.head = None
            return temp
        else:
            # Queues with more than one element
            now = self.head
            prev = None
            while now.next != None:
                prev = now
                now = now.next
            temp = now.data
            prev.next = None
            return temp

class EfficientQueue:
    """
    A basic (yet efficient, I think) implementation of a FIFO heterogeneous collection.
    """
    def __init__(self):
        """ When constructed, the queue is empty. """
        self.head = None
        self.tail = None

    def __str__(self):
        """ Returns a string representation of the queue's content. """
        if self.isEmpty():
            return "Empty queue."

        node, i, text = self.head, 1, ""
        while node != None:
            text += "(%s) %s\n" % (i, node)
            node = node.next
            i += 1
        return text

    def isEmpty(self):
        """ Returns whether the queue is empty or not. """
        return self.head == None and self.tail == None

    def enqueue(self, data):
        """ Adds a new element at the beginning of the queue. """
        if self.isEmpty():
            # Treat the empty queue as a special case
            self.tail = Node(data)
            self.head = self.tail
        else:
            temp = Node(data, self.head)
            self.head.prev = temp
            self.head = temp

    def dequeue(self):
        """ 
        Removes the oldest element of the queue.

        WARNING: Do not dequeue from an empty queue or an IndexError
        exception will be raised.
        """
        if self.isEmpty():
            raise IndexError("Tried to dequeue from an empty queue.")

        temp = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return temp

class Movie:
    """
    Movie model. It stores all the information about a movie.
    It also gives several methods to import and export data.
    """
    def __init__(self,
            title = "",
            director=[],
            cast = [],
            producer = [],
            writer = [],
            country = [],
            language = [],
            year = "",
            genres = [],
            votes = "",
            rating = "",
            runtime = [],
            plot = [],
            coverUrl = ""):
        self.title = title
        self.director = director
        self.cast = cast
        self.producer = producer
        self.writer = writer
        self.country = country
        self.language = language
        self.year = year
        self.genres = genres
        self.votes = votes
        self.rating = rating
        self.runtime = runtime
        self.plot = plot
        self.coverUrl = coverUrl
    
    def __str__(self):
        """ Returns a reduced set of movie information """
        self.getTitle()

    def getTitle(self):
        return self.title
    
    def parseArray(self, data):
        """ 
        Given a multi-sized array that contains the movie information,
        this method loads the data from it inside the object.
        """
        self.getTitle() = data[0]
        self.director = data[1]
        self.cast = data[2]
        self.producer = data[3]
        self.writer = data[4]
        self.country = data[5]
        self.language = data[6]
        self.year = data[7]
        self.genres = data[8]
        self.votes = data[9]
        self.rating = data[10]
        self.runtime = data[11]
        self.plot = data[12]
        self.coverUrl = data[13]

    def importFromString(self, movieString):
        """
        This method tries to parse the given string to get the movie data
        from it.
        """
        data = []
        fields = movieString.split("|")
        for field in fields:
            if field.find("&&") != -1:
                composedField = field.rstrip().split("&&")
                data.append(composedField)
            else:
                data.append(field.rstrip())

        self.parseArray(data)

def loadMovieList(filename):
    """
    Given a string containing the name of the file, this method
    parses the file information, looking up for movies data.
    """
    print "Loading movies from '%s'" % ( filename )
    movies = []

    try:
        f = open(filename, 'r')
        filmEntries = f.readlines()
        f.close()

        movieData = []
        for entry in filmEntries:
            fields = entry.split("|")
            for field in fields:
                if ( field.find("&&") != -1 ):
                    composedField = field.rstrip().split("&&")
                    movieData.append(composedField)
                else:
                    movieData.append(field.rstrip())
            movie = Movie()
            movie.parseArray(movieData)
            movies.append(movie)
            movieData = []
    except IOError:
        print "Error while trying to read file:", filename

    return movies

movieList = loadMovieList('peliculas100.dat')
## Reduce MovieList to 20 elements
movieList = movieList[0:20]
"""
newStack = Stack()
print newStack

newStack.push(movieList[0])
print newStack

newStack.push(movieList[1])
print newStack

newStack.push(movieList[2])
print newStack

m1 = newStack.pop()
print newStack

m2 = newStack.pop()
print newStack

m3 = newStack.pop()
print newStack

# Trying to pop out of an empty stack.
m4 = None
try:
    m4 = newStack.pop()
    print newStack
except IndexError:
    print "Nice try, little sparrow.\n"

print m1.getTitle()
print m2.getTitle()
print m3.getTitle()
print m4
##print m4.getTitle()  GUESS WHAT HAPPENS...
"""
## THIS IS TO TEST YOUR CODE - QUEUE
queue = Queue()
print queue

queue.enqueue(movieList[0])
print queue

queue.enqueue(movieList[1])
print queue

queue.enqueue(movieList[2])
print queue

m1 = queue.dequeue()
print queue

m2 = queue.dequeue()
print queue

m3 = queue.dequeue()
print queue

try:
    m4 = queue.dequeue()
    print dequeue
except IndexError:
    print "Now, lad, tell me something I don't know about queues...\n"

print m1.getTitle()
print m2.getTitle()
print m3.getTitle()
##print m4.getTitle()  GUESS WHAT HAPPENS...
