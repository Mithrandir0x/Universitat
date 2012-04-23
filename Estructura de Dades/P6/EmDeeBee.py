#
# EmDeeBee.py
#
# author: olopezsa13
#

from Tkinter import *

import Image
import ImageTk
import os
import random
import shutil
import time
import types
import urllib

class Node:
    """
    The most basic element in a bi-directional linked structure.
    """
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """ When printing a node, it prints the content of the data. """
        return self.data.__str__()

class Queue:
    """
    A basic implementation of a FIFO heterogeneous collection.
    """
    def __init__(self):
        """ When constructed, the queue is empty. """
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """ Returns a string representation of the queue's content. """
        if self.isEmpty():
            return "Empty queue."

        node, i, text = self.head, 1, ""
        while node != None:
            text += "(%s) %s\n" % (i, node)
            node = node.right
            i += 1
        return text

    def __iter__(self):
        """ Returns an iterator to be used to (let me guess...) iterate the queue. """
        return self._next()

    def _next(self):
        """ 'Private' This method is a python's generator used to iterate the queue. """
        node = self.head
        while node != None:
            yield node.data
            node = node.right

    def __len__(self):
        """ Returns the size of the queue. """
        return self.size

    def isEmpty(self):
        """ Returns whether the queue is empty or not. """
        return self.head == None and self.tail == None

    def add(self, data):
        """ Adds a new element at the beginning of the queue. """
        if self.isEmpty():
            # If the queue is empty, simply create a new node at the
            # end, and refer the head to this one
            self.tail = Node(data)
            self.head = self.textvariable
        else:
            temp = Node(data, self.head)
            self.head.left = temp
            self.head = temp
        self.size += 1

    def remove(self):
        """
        Removes the oldest element of the queue.

        WARNING: Do not dequeue from an empty queue or an IndexError
        exception will be raised.
        """
        if self.isEmpty():
            raise IndexError("Tried to dequeue from an empty queue.")

        temp = self.tail.data
        if self.head == self.tail:
            # When there's only one element in the queue, both head
            # and tail refer to no element
            self.head = None
            self.tail = None
        else:
            # Remove the tail
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

        return temp

    def peek(self):
        """ Return the most important element without removing it. """
        return self.tail.data

class LinkedListPriorityQueue(Queue):
    """
    Implementation of a priority queue using a linked list.

    Treat the 'head' as the element with the least priority, and 'tail' with utmost priority.

    Enqueueing elements may take O(N) complexity.
    Dequeueing elements takes O(1) complexity.

    The priority of the elements is evaluated by their own comparator implementation.
    """
    # A little explanation about why a double-linked queue implementation is used. Although
    # it is totally possible to do it with a single link queue implementation is possible,
    # it seemed for me more natural and convenient.
    def add(self, data):
        """
        @Overrides
        Adds the new element depending on its priority, and returns the node reference
        of this new element
        """
        if self.isEmpty():
            # Consider the empty queue as a special case
            self.tail = Node(data)
            self.head = self.tail
            self.size += 1
            return self.head
        else:
            node = self._add(self.head, data)
            self.size += 1
            return node

    def _add(self, node, data):
        """
        'Private' recursive method called by 'self.add'.

        It iterates over every element in the queue until it finds the right
        spot where the new 'data' must be inserted and updates the 'head' 
        or 'tail' whenever it is necessary.

        Normally, this method should not return a Node element, but it is
        needed by the MovieStore class to let walk through the structure.
        """
        if data > node.data:
            if node.right == None:
                # The actual node is the 'tail'
                newNode = Node(data, node)
                node.right = newNode
                self.tail = newNode
                return newNode
            else:
                # Advance to the right node to find the adequate place
                return self._add(node.right, data)
        else:
            newNode = Node(data, node.left, node)
            if node.left == None:
                # The left of a node is only empty if the actual node is the 'head'.
                node.left = newNode
                self.head = newNode
            else:
                node.left.right = newNode
                node.left = newNode
            return newNode

class DegeneratedTreePriorityQueue:
    """
    Implementation of a PriorityQueue based on a degenerated tree.

    Adding elements has O(n) complexity.
    Removing elements has O(n) complexity.
    """
    def __init__(self):
        self.root = None
        self.depth = 0

    def add(self, element):
        return self._add(self.root, element, 1)

    def _add(self, root, element, currentDepth):
        """
        'Private' recursive method used by 'self.add' to add an element in the queue.
        """
        if root == None:
            root = Node()
            root.data = element
            if currentDepth > self.depth:
                self.depth = currentDepth
            return root
        else:
            return self._add(root.right, element, currentDepth + 1)

class BinarySearchTreePriorityQueue:
    """
    Implementation of a PriorityQueue based on a binary search tree.

    Adding elements to the priority queue has O(log n) complexity.
    Removing elements from the priority queue has O(log n) complexity.

    Do not use this data structure with an ordered set of items, or it will become a
    degenerate tree, uprising operations complexity to O(n^2).

    The priority of the elements is evaluated by their own comparator implementation.
    """
    def __init__(self):
        self.root = None
        self.depth = 0

    def __iter__(self):
        """ Returns a python's iterator. """
        return self._next(self.root)

    def _next(self, node):
        """ Iterator function """
        if node != None:
            if node.left != None:
                self._next(node.left)
            yield node.data
            if node.right != None:
                self._next(node.right)

    def add(self, element):
        """ Adds the element to the priority queue. """
        return self._add(self.root, element, 1)

    def _add(self, root, element, currentDepth):
        """
        'Private' recursive method used by 'self.add' to add an element in the queue.
        """
        if root == None:
            root = Node()
            root.data = element
            if currentDepth > self.depth:
                self.depth = currentDepth
            return root
        else:
            # When adding an element from the actual node, all elements less important
            # than the actual node are ALWAYS in the left branch, but the most importants
            # are on the right branch
            if root.data > element:
                return self._add(root.left, element, currentDepth + 1)
            else:
                return self._add(root.right, element, currentDepth + 1)

    def poll(self):
        """ Returns and removes the element with the utmost priority. """
        return self._poll(self.root)

    def _poll(self, root):
        """
        'Private' method used by 'self.poll' to fetch the element.

        In this structure, the most important element is always at the branch
        with the highest 'degree', i.e. the first element visible from the right
        side of the graph.
        """
        if self.isEmpty():
            # If someone tries to poll from an empty queue...
            return None
        else:
            if root.right != None:
                # The actual node is not the most important one yet, so advance to the right
                data = self._poll(root.right)
                # If the actual node's right children does not have a right children, it means that
                # it was the most important element, and it may has a left children; this children
                # will be the most important one
                if root.right.right == None:
                    root.right = root.right.left
                return data
            else:
                if root == self.root:
                    # Consider a queue with one or two element as a unique case. In this case,
                    # the root should be assigned the left children of the actual node
                    temp = root.data
                    self.root = root.left
                    return temp
                else:
                    return root.data

    def isEmpty(self):
        return self.root == None

class Movie:
    """
    Movie model. It stores all the information about a movie.
    It also gives several methods to import and export data.
    """
    def __init__(self,
            title = "",
            director = [],
            cast = [],
            producer = [],
            writer = [],
            country = [],
            language = [],
            year = "",
            genres = [],
            votes = "",
            rating = "0.0",
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
        self.rating = float(rating)
        self.runtime = runtime
        self.plot = plot
        self.coverUrl = coverUrl

    def __ne__(self, other):
        """ Not Equal comparator override needed to treat None as special case. """
        if other != None:
            return self != other
        else:
            return True

    def __eq__(self, other):
        """ Equal comparator override needed to treat None as special case. """
        if other != None:
            return self == other
        else:
            return False
    
    def __cmp__(self, other):
        """ Comparator overloading. """
        if self.rating < other.rating:
            return -1
        elif self.rating > other.rating:
            return 1
        else:
            return 0
    
    def __str__(self):
        """ Returns a reduced set of movie information """
        directors = ""
        if isinstance(self.director, types.StringTypes):
            directors = self.director
        else:
            directors = ', '.join(self.director)

        return "%s | %s | %s | %s" % ( self.title, directors, self.insertionTime, self.rating )
    
    def parseArray(self, data):
        """ 
        Given a multi-sized array that contains the movie information,
        this method loads the data from it inside the object.
        """
        self.title = data[0]
        self.director = data[1]
        self.cast = data[2]
        self.producer = data[3]
        self.writer = data[4]
        self.country = data[5]
        self.language = data[6]
        self.year = data[7]
        self.genres = data[8]
        self.votes = data[9]
        self.rating = float(data[10])
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

    def exportAsArray(self):
        """
        Returns a multi-sized array containing the movie information.
        """
        data = []
        data.append(self.title)
        data.append(self.director)
        data.append(self.cast)
        data.append(self.producer)
        data.append(self.writer)
        data.append(self.country)
        data.append(self.language)
        data.append(self.year)
        data.append(self.genres)
        data.append(self.votes)
        data.append(self.rating)
        data.append(self.runtime)
        data.append(self.plot)
        data.append(self.coverUrl)
        return data

    def exportAsString(self):
        """
        Returns a string containing the movie information, with fields
        separated by '|' character, and composed fields separated by
        '&&' character.
        """
        dataString = ""
        data = self.exportAsArray()
        content = ""
        for field in data:
            if isinstance(field, types.StringTypes):
                content = field
            else:
                content = '&&'.join(field)
            dataString = '|'.join([dataString, content])

        return dataString[1:] # Remove the first '|' character from the output.

class MovieStore:
    """
    This class is in charge of saving all the movies, and walking through each of the
    records available and withing the specified range of rating.
    """
    def __init__(self, filename = None):
        """
        Given a string containing the name of the file, it tries to
        parse the file information, looking up for movies data.
        """
        self.movies = LinkedListPriorityQueue()

        # Only used for benchmarking purposes
        self._degenerateTree = DegeneratedTreePriorityQueue()
        self._binarySearchTree = BinarySearchTreePriorityQueue()

        self._filterRatingMin = 0   # The minimal value that a movie's rating could have.
        self._filterRatingMax = 100 # The maximum value that a movie's rating could have.
        self._startingMovie = None  # A reference to the movie with the lowest rating, depending on '_filterRatingMin'.
        self._currentMovie = None   # A reference to the movie pointed by MovieStore.

        if filename != None:
            print "Loading movies from '%s'" % ( filename )
            try:
                f = open(filename, 'r')
                filmEntries = f.readlines()
                f.close()

                for entry in filmEntries:
                    self.insert(entry, true)
            except IOError:
                print "Error while trying to read file:", filename

    def insert(self, movie, movieStringData = False):
        """ Inserts a new movie in the store, and updates its movie pointer. """
        if movieStringData:
            movie = Movie().importFromString(movie)

        # Set the current movie to the new one being added, and
        # update starting and current movie pointers.
        self._currentMovie = self.movies.add(movie)
        self._updateMoviePointers(self._startingMovie == None)

        # Update auxiliary starting movie pointer to the new movie being added,
        # if this movie has a lower rate and is inside the demanded threshold.
        if self._startingMovie != None and self._startingMovie.data.rating > movie.rating and ( movie.rating * 10 ) > self._filterRatingMin:
            self._startingMovie = self._currentMovie

    def insertDegenerateTree(self, movie):
        self._degenerateTree.add(movie)

    def insertBinarySearchTree(self, movie):
        self._binarySearchTree.add(movie)

    def setRatingFilter(self, min, max):
        """
        This method updates the minimal and maximum rating that filters the movies
        being showed.
        """
        # If any of the old values differ with the new ones, then the movie record pointer is updated.
        update = self._filterRatingMin != min or self._filterRatingMax != max
        self._filterRatingMin, self._filterRatingMax = min, max
        if update:
            self._updateMoviePointers(True)

    def getCurrentMovie(self):
        """ It returns the movie currently selected or None if not available. """
        if self._currentMovie != None:
            return self._currentMovie.data
        else:
            return None

    def getNextMovie(self):
        """ It returns the movie next to the current one. """
        if self._currentMovie != None:
            if self._currentMovie.right != None:
                # Check whether there's a movie next to the current one and meets the rating
                # filter values. If so, advance, else, go back to the beginning.
                if ( self._currentMovie.right.data.rating * 10 ) <= self._filterRatingMax:
                    self._currentMovie = self._currentMovie.right
                else:
                    self._currentMovie = self._startingMovie
            else:
                # If there's no movie next to the current one, go back to the beginning.
                self._currentMovie = self._startingMovie

            return self._currentMovie.data
        else:
            return None

    def _updateMoviePointers(self, updateStartingMoviePointer = False):
        """
        'Private' method. When called, it updates the starting movie pointer, and also checks
        if the current movie pointer is referencing to the right movie, depending on the
        rating minimum and maximum values.
        """
        if updateStartingMoviePointer:
            # Walk through all the nodes of the priority queue until the movie with
            # the lowest rating and higher than '_filterRatingMin' is found, and
            # update the '_startingMovie' pointer.
            node = self.movies.head
            self._startingMovie = None
            while node != None:
                rating = int(node.data.rating * 10)
                if rating >= self._filterRatingMin and rating <= self._filterRatingMax:
                    self._startingMovie = node
                    break
                node = node.right

        if self._currentMovie != None:
            # Verify that the current movie has a rating within the range specified
            # by '_filterRatingMin' and '_filterRatingMax', and change it to the
            # starting one if the current movie doesn't meet the range.
            rating = self._currentMovie.data.rating
            if rating > self._filterRatingMax or rating < self._filterRatingMin:
                self._currentMovie = self._startingMovie
        else:
            # The current movie pointer can be None if an invalid or impossible range
            # is specified.
            # For example, if the rating values are specified to 0/0, then
            # even if there are movies stored, no one will meet this range, and won't be
            # showed. But, if then a valid range is specified, and no movie has been
            # selected, simply select the starting one.
            self._currentMovie = self._startingMovie

    def size(self):
        """ Returns the amount of movies stored. """
        return len(self.movies)

class MovieDisplay(Frame):
    """ This widget displays Movie information. """
    def __init__(self, master):
        """ Constructor. It creates all the needed components to render movie data. """
        Frame.__init__(self, master)

        self.titleText = StringVar()
        self.titleLabel = Label(self, text = "Title:").grid(row = 0, sticky = E)
        self.title = Label(self, textvariable = self.titleText)
        self.title.grid(row = 0, column = 1)

        self.directorText = StringVar()
        self.directorLabel = Label(self, text = "Director: ").grid(row = 1, sticky = E)
        self.director = Label(self, textvariable = self.directorText, width = 40, wraplength = 256)
        self.director.grid(row = 1, column = 1)

        self.yearText = StringVar()
        self.yearLabel = Label(self, text = "Year: ").grid(row = 2, sticky = E)
        self.year = Label(self, textvariable = self.yearText)
        self.year.grid(row = 2, column = 1)

        self.ratingText = StringVar()
        self.ratingLabel = Label(self, text = "Rating: ").grid(row = 3, sticky = E)
        self.rating = Label(self, textvariable = self.ratingText)
        self.rating.grid(row = 3, column = 1)

        self.picture = Canvas(self, width = 100, height = 168, bg = "black")
        self.picture.grid(row = 0, column = 2, rowspan = 4, padx = 4)
        self.photoImage = None

    def setMovie(self, movie):
        """
        Given a "movie" object, the display will modify its data to
        show the movie information provided.
        """
        if movie != None:
            self.titleText.set(movie.title)
            if isinstance(movie.director, types.StringTypes):
                self.directorText.set(movie.director)
            else:
                self.directorText.set(', '.join(movie.director))
            self.yearText.set(movie.year)
            self.ratingText.set(movie.rating)
            self._setMoviePicture(movie.coverUrl)
        else:
            self.reset()

    def reset(self):
        self.titleText.set("")
        self.directorText.set("")
        self.yearText.set("")
        self.ratingText.set("")
        self.clearMoviePicture()

    def clearImageCache(self):
        """
        It removes the image cache folder. Do not call if images are being used.
        """
        if os.path.exists("./cache/"):
            shutil.rmtree("./cache/")

    def _setMoviePicture(self, imageUrl):
        """
        'Private' method that renders the image designated by 'imageUrl'.
        """
        imageFilename = imageUrl.split("/")[-1]
        imagePath = "cache/" + imageFilename

        # Create 'cache' folder if it does not exist.
        if not os.path.exists("./cache/"):
            os.makedirs("./cache/")

        try:
            if not os.path.exists(imagePath):
                # print "Creating '%s'..." % ( imagePath )
                urllib.urlretrieve(imageUrl, imagePath)
            urllib.urlcleanup()

            try:
                # Scaffold image loading. If any exception arises for image
                # parsing, the 'image' file won't be locked.
                with open(imagePath, 'rb') as imageFile:
                    image = Image.open(imageFile)
                    self.photoImage = ImageTk.PhotoImage(image)
                    self.picture.create_image(0, 0, image = self.photoImage, anchor = NW)
                    return
            except IOError:
                print "Unable to load cache image '%s'." % ( imagePath )
                os.remove(imagePath)
        except IOError:
            print "Unable to retrieve the movie image."

        self.clearMoviePicture()

    def clearMoviePicture(self):
        self.picture.create_rectangle(0, 0, 100, 168, fill = "black")

class OutputLabel(Frame):
    """
    A little component to display descriptive data.
    """
    def __init__(self, master, label = "Label", content = None):
        Frame.__init__(self, master)
        self.label = StringVar()
        self.label.set(label)

        self.data = StringVar()
        self.data.set(content)

        self._labelLabel = Label(self, textvariable = self.label, width = 24, anchor = E)
        self._labelLabel.grid(row = 0, column = 0)

        self._contentLabel = Label(self, textvariable = self.data, relief = SUNKEN, width = 32)
        self._contentLabel.grid(row = 0, column = 1)

    def set(self, data):
        self.data.set(data)

class BenchmarkDisplay(Frame):
    """
    A frame used to display several performance statistics of the structures being studied.
    """
    def __init__(self, master):
        Frame.__init__(self, master)

        self.linked = OutputLabel(self, "\"LINKED\" cost:", 0)
        self.linked.grid(row = 0, sticky = W+E)

        self.degeneratedTree = OutputLabel(self, "\"DEGENERATED TREE\" cost:", 0)
        self.degeneratedTree.grid(row = 1, sticky = W+E)

        self.binarySearchTree = OutputLabel(self, "\"BINARY SEARCH TREE\" cost:", 0)
        self.binarySearchTree.grid(row = 2, sticky = W+E)

        self.degeneratedTreeDepth = OutputLabel(self, "\"DEGENERATED TREE\" depth:", 0)
        self.degeneratedTreeDepth.grid(row = 3, sticky = W+E)

        self.binarySearchTreeDepth = OutputLabel(self, "\"BINARY SEARCH TREE\" depth:", 0)
        self.binarySearchTreeDepth.grid(row = 4, sticky = W+E)

class StatusBar(Frame):
    """
    Effbot's Simple Status Bar widget.

    Take a look at: http://effbot.org/tkinterbook/tkinter-application-windows.htm
    """
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def write(self, message):
        self.clear()
        self.set('%s', message)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

class MovieApp(Frame):
    """
    Main application.
    """
    def __init__(self, master, filename):
        """ Film data is loaded (sorted by title), and the GUI is loaded. """
        Frame.__init__(self, master)

        innerFrame = Frame(master)
        innerFrame.grid(row = 0)

        print "WARNING: This program creates a folder named 'cache' where MovieApp will save movie covers."

        self.store = MovieStore()     # This is where all the movies are stored.

        self._data = []               # A hidden field that stores all movie entries to be added afterwards with add button.
        self._impDataIndex = 0        # Index of the new movie to be imported.

        self.lastJobTimeTaken = None  # It indicates how much time has taken to add a new movie.
        self.lastFilteringTime = None # It indicates how much time has taken to get the filtered list of movies.

        self.movieDisplay = MovieDisplay(innerFrame)
        self.movieDisplay.grid(row = 0)

        self.benchmarkDisplay = BenchmarkDisplay(innerFrame)
        self.benchmarkDisplay.grid(row = 0, column = 1)

        buttonFrame = Frame(innerFrame)
        buttonFrame.grid(row = 1, pady = 8)
        addMovieButton = Button(buttonFrame, text = "Add Movie", command = self.addMovie).grid(row = 1, column = 0)
        nextMovieButton = Button(buttonFrame, text = "Next Movie", command = self.nextMovie).grid(row = 1, column = 1, sticky = W)

        inputFrame = Frame(innerFrame)
        inputFrame.grid(row = 2, pady = 16)
        minRatingText = Label(inputFrame, text = "From: ").grid(row = 2, column = 0)
        maxRatingText = Label(inputFrame, text = "To: ").grid(row = 3, column = 0)
        self.minRatingInput = Entry(inputFrame)
        self.minRatingInput.grid(row = 2, column = 1, sticky = W+E+N+S)
        self.minRatingInput.bind('<Return>', self.updateMovieList)
        self.maxRatingInput = Entry(inputFrame)
        self.maxRatingInput.grid(row = 3, column = 1, sticky = W+E+N+S)
        self.maxRatingInput.bind('<Return>', self.updateMovieList)

        master.protocol("WM_DELETE_WINDOW", self.onApplicationClose)

        self.statusBar = StatusBar(master)
        self.statusBar.grid(row = 1, sticky = W+E)

        try:
            f = open('peliculas100.dat', 'r')
            self._data = f.readlines()
            f.close()
        except IOError:
            print "Error while trying to read file:", 'peliculas100.dat'
    
    def showMovie(self, movie):
        """ Displays the current movie. """
        self.updateStatusBar()
        self.movieDisplay.setMovie(movie)

    def nextMovie(self):
        """
        Displays the movie next to the current one. Notice that if the last
        movie is being displayed, the next movie will be the first one.
        """
        movie = self.store.getNextMovie()

        self.showMovie(movie)

    def addMovie(self):
        """ Adds a movie. """
        if self._impDataIndex < len(self._data):
            movie = Movie()
            movie.importFromString(self._data[self._impDataIndex])

            print "Adding movie '%s'..." % ( movie.title )

            self.insertMovieBenchmark(movie, self.store.insert, self.benchmarkDisplay.linked.set)

            self._impDataIndex += 1
            self.updateMovieList(None)
        else:
            print "No more movies available."

    def insertMovieBenchmark(self, movie, callbackInsert, callbackSet):
        start = time.clock() * 1000000
        callbackInsert(movie)
        end = time.clock() * 1000000
        self.lastJobTimeTaken = end - start
        callbackSet(end - start)


    def updateMovieList(self, event):
        """
        Updates the movie list. Called when a new movie is added, or any of the rating input fields
        have been updated.
        """
        min, max = self.getValidRatingInputs()

        start = time.clock() * 1000000
        self.store.setRatingFilter(min, max)
        end = time.clock() * 1000000
        self.lastFilteringTime = end - start

        movie = self.store.getCurrentMovie()
        if movie == None:
            self.updateStatusBar()
            self.movieDisplay.reset()
        else:
            self.showMovie(movie)

    def updateStatusBar(self):
        """ Updates the status bar text with some statistics. """
        text = "(#: %d) (Last Addition: %.3fms / Last Filtering: %.3fms)" % ( self.store.size(), self.lastJobTimeTaken, self.lastFilteringTime )
        self.statusBar.write(text)

    def getValidRatingInputs(self):
        """ Returns the valid minimum and maximum integer values of rating to be accepted. """
        min = self.minRatingInput.get()
        max = self.maxRatingInput.get()

        try:
            min = int(min)
        except ValueError:
            min = 0

        try:
            max = int(max)
        except ValueError:
            max = 100

        return min, max

    def onApplicationClose(self):
        """
        Method called whe widget is about to be closed. In this method, the
        movie display's image cache is cleared, and the widget is closed.
        """
        self.movieDisplay.clearImageCache()
        self.quit()

# Bootstrap
tk = Tk()
instance = MovieApp(master = tk, filename = "peliculas100.dat")

tk.mainloop()
