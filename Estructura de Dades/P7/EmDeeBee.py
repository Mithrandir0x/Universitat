#
# EmDeeBee.py
#
# author: olopezsa13
#

from Tkinter import *

import Image
import ImageTk
import math
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

class BinarySearchTreePriorityQueue:
    """
    Implementation of a PriorityQueue based on a binary search tree.

    Adding elements to the priority queue has O(log n) complexity.

    Do not use this data structure with an ordered set of items, or it will become a
    degenerate tree, uprising operations complexity to O(n^2).

    The priority of the elements is evaluated by their own comparator implementation.
    """
    def __init__(self):
        self.root = None
        self.depth = None

    def __str__(self):
        s = "--\n"
        for node in self:
            s += node.__str__() + "\n"
        return s + "--"

    def __iter__(self):
        """ Returns a generator to be used to iterate the tree. """
        return self._next(self.root)

    def _next(self, parent):
        """ 'Private' method. This method is a python's generator used to iterate the tree. """
        if parent.left != None:
            for child in self._next(parent.left):
                yield child
        yield parent
        if parent.right != None:
            for child in self._next(parent.right):
                yield child

    def add(self, element):
        """
        Adds the element to the priority queue and returns the node
        reference in the tree structure.
        """
        if self.root == None:
            # A root is None when the binary tree is empty
            # print "Empty tree, adding root", element
            self.root = Node(element)
            self.depth = 1
            return self.root
        else:
            return self._add(self.root, element, 1)

    def _add(self, root, element, currentDepth):
        """
        'Private' recursive method used by 'self.add' to add an 
        element in the tree structure.
        """
        # When adding an element from the actual node, all elements less important
        # than the actual node are ALWAYS in the left branch, but the most importants
        # are on the right branch
        if root.data > element:
            if root.left == None:
                root.left = Node(element)
                if currentDepth > self.depth:
                    self.depth = currentDepth
                return root.left
            else:
                # print "Going to left branch at depth", currentDepth
                return self._add(root.left, element, currentDepth + 1)
        else:
            if root.right == None:
                # print "Adding new right leave", element
                root.right = Node(element)
                if currentDepth > self.depth:
                    self.depth = currentDepth
                return root.right
            else:
                # print "Going to right branch at depth", currentDepth
                return self._add(root.right, element, currentDepth + 1)

class BinaryHeap:
    """
    A 'min-heap' implementation of a binary heap.

    When adding or removing elements from the heap, this won't be ordered until
    'self.sort' has been called. Each node of the heap only complies that its left
    children is lower than the parent node, and the right one is greater.
    """
    def __init__(self, maxSize = 100):
        """ Class constructor. The default maximum amount of elements that a heap may contain is 100. """
        self.data = [None] * maxSize
        self.size = 0
        self.maxSize = maxSize

    def __str__(self):
        """ Returns a string representation of the binary heap's content. """
        s = "--\n"
        for node in self:
            s += node.__str__() + "\n"
        return s + "--"

    def __iter__(self):
        """ Returns a generator to be used to iterate the heap. """
        return self._next()

    def _next(self):
        """ 'Private' method. This method is a python's generator used to iterate the tree. """
        i = 0
        while i < self.size:
            yield self.data[i]
            i += 1

    def add(self, element):
        """
        Adds the element passed by to the heap.

        NOTICE that the element must have a comparator implemented.
        """
        self.data[self.size] = element
        self.size += 1
        i = self.size - 1
        while i > 0 and self.data[i/2] < self.data[i]:
            self.data[i], self.data[i/2] = self.data[i/2], self.data[i]
            i = i / 2

    def sort(self):
        """ This method sorts the heap, heapster-heapsort style. """
        def sift(start, count):
            """

            """
            root = start
            while root * 2 + 1 < count:
                child = root * 2 + 1
                if child < count - 1 and self.data[child] < self.data[child + 1]:
                    child += 1
                if self.data[root] < self.data[child]:
                    self.data[root], self.data[child] = self.data[child], self.data[root]
                    root = child
                else:
                    return
     
        count = self.size
        start = count / 2 - 1
        end = count - 1

        # Is this really necessary? If the structure is already a heap...
        while start >= 0:
            sift(start, count)
            start -= 1
     
        while end > 0:
            self.data[end], self.data[0] = self.data[0], self.data[end]
            sift(0, end)
            end -= 1

    @property
    def depth(self):
        """
        This 'method' returns the actual depth of the heap. If the heap is
        empty, it will return 0, otherwise, it will return a value >= 1.

        (Instead of adding a new property for displaying the depth, this
        method works as a 'read-only' field, and takes away the need to
        update the depth each time an element is being added, thus making
        the whole operation quite faster...)
        """
        if self.size == 0:
            return 0
        return int(math.log(self.size, 2)) + 1

    def __len__(self):
        """ Returns the quantity of elements added to the heap. """
        return self.size

class HashTable:
    """ A simple implementation of a hash table. """
    def __init__(self, buckets = 200):
        """ Class constructor. By default, it has 200 buckets. """
        self.data = [None] * buckets
        self.slot = [None] * buckets
        self.size = buckets

    def __getitem__(self, key):
        """ Array-format getter method to get elements from the table. """
        return self.get(key)

    def __setitem__(self, key, value):
        """ Array-format setter method to set elements from the table. """
        self.add(key, value)

    def set(self, key, value):
        """ This methods maps the key to the value in the container. """
        h = self._hash(key)
        if self.slot[h] != None:
            # If the hash already exists, simply recalculate the hash until a new one is found.
            h = self._rehash(key)
            while self.slot[h] != None:
                h = self._rehash(key)
        self.slot[h] = key
        self.data[h] = value

    def get(self, key):
        """ This methods returns the value mapped to the key. """
        sh = self._hash(key)
        data = None   # The element to be returned
        h = sh        # The current hash value being accesed
        stop = False  # A flag to indicate whether the search must be stop
        found = False # A flag to indicate that the element has been found and the search must end
        while self.slot[h] != None and not found and not stop:
            if self.slot[h] == h:
                found, data = True, self.data[h]
            else:
                h = self._rehash(h)
                if h == sh:
                    stop = True
        return data

    def _hash(self, key):
        """ Returns the index of the bucket to be used given a hashable key. """
        return hash(key) % self.size

    def _rehash(self, key):
        """ Returns a new index of a bucket. """
        return ( hash(key) + 1 ) % self.size

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

    def __hash__(self):
        """ Calculates a 'unique' integer hash of the movie object. """
        return int(self.rating * 10)
    
    def __str__(self):
        """ Returns a reduced set of movie information """
        directors = ""
        if isinstance(self.director, types.StringTypes):
            directors = self.director
        else:
            directors = ', '.join(self.director)

        return "%s | %s | %s" % ( self.title, directors, self.rating )
    
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
        """ This method tries to parse the given string to get the movie data from it. """
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
        """ Returns a multi-sized array containing the movie information. """
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

class MovieStoreTree:
    """
    This class stores the movies and can filter through them, like MovieStore. But it is baced on a
    Binary Search Tree structure.
    """
    def __init__(self):
        """ Class constructor. """
        self.movies = BinarySearchTreePriorityQueue()

        self._filterRatingMin = 0   # The minimal value that a movie's rating could have.
        self._filterRatingMax = 100 # The maximum value that a movie's rating could have.

        # This properties are required to store temporally the movies that abide for the rating filter values
        self._filteredMovieList = None
        self._updateMovieList = False   # A flag that indicates when the list of movies between the range specified must be updated.

    def insert(self, movie):
        """ Adds a new movie in the list. """
        self._currentMovie = self.movies.add(movie)
        self._updateMovieList = True

    def getCurrentMovie(self):
        """ It returns the movie currently selected or None if not available. """
        if self._currentMovie != None:
            return self._currentMovie.data
        else:
            return None

    def setRatingFilter(self, min = 0, max = 100):
        """ This method updates the minimal and maximum rating that filters the movies being showed. """
        self._updateMovieList = self._updateMovieList or self._filterRatingMin != min or self._filterRatingMax != max
        self._filterRatingMin, self._filterRatingMax = min, max

    def getFilteredMovies(self):
        """ This method returns a list of the movies that comply with the ranges configured. """
        if self._updateMovieList:
            # Every time a movie is added, or the filter range is changed, a new temporal
            # list of movies must be created, thus decreasing performance when getting the
            # next movie.
            # But calling again to fetch a new movie will perform faster.
            self._filteredMovieList = []
            for node in self.movies:
                rating = node.data.rating * 10
                if rating >= self._filterRatingMin and rating <= self._filterRatingMax:
                    self._filteredMovieList.append(node.data)
            self._updateMovieList = False

        return self._filteredMovieList

    def getDepth(self):
        """ This method returns the current depth of the internal tree structure. """
        return self.movies.depth

class MovieStoreHeap:
    """
    This class stores movies in a binary heap. It is possible to add movies and fetch movies with
    the rating ranges that may be specified.
    """
    def __init__(self):
        """ Class constructor. """
        self.movies = BinaryHeap()

        self._filterRatingMin = 0   # The minimal value that a movie's rating could have.
        self._filterRatingMax = 100 # The maximum value that a movie's rating could have.

        # This properties are required to store temporally the movies that abide for the rating filter values
        self._filteredMovieList = None
        self._updateMovieList = False   # A flag that indicates when the list of movies between the range specified must be updated.
        self._sortHeap = False          # A flag that indicates whether the heap must be sorted. (This only is required when a new element has been added)

    def insert(self, movie):
        """ Adds a new movie in the list. """
        self._currentMovie = self.movies.add(movie)
        self._updateMovieList = True
        self._sortHeap = True

    def getCurrentMovie(self):
        """ It returns the movie currently selected or None if not available. """
        if self._currentMovie != None:
            return self._currentMovie.data
        else:
            return None

    def setRatingFilter(self, min = 0, max = 100):
        """ This method updates the minimal and maximum rating that filters the movies being showed. """
        self._updateMovieList = self._updateMovieList or self._filterRatingMin != min or self._filterRatingMax != max
        self._filterRatingMin, self._filterRatingMax = min, max

    def getFilteredMovies(self):
        """ This method returns a list of ordered movies (by increasing rating) that complies the ranges specified. """
        if self._sortHeap:
            self.movies.sort()
            self._sortHeap = False

        if self._updateMovieList:
            # Every time a movie is added, or the filter range is changed, a new temporal
            # list of movies must be created, thus decreasing performance when getting the
            # next movie.
            # But calling again to fetch a new movie will perform faster.
            self._filteredMovieList = []
            for node in self.movies:
                rating = node.rating * 10
                if rating >= self._filterRatingMin and rating <= self._filterRatingMax:
                    self._filteredMovieList.append(node)
            self._updateMovieList = False

        return self._filteredMovieList

    def getDepth(self):
        """ This method returns the current depth of the internal tree structure. """
        return self.movies.depth

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

        self.binarySearchTree = OutputLabel(self, "ABB ORIGINAL COST:", 0)
        self.binarySearchTree.grid(row = 0, sticky = W+E)

        self.binaryHeap = OutputLabel(self, "HEAP COST:", 0)
        self.binaryHeap.grid(row = 1, sticky = W+E)

        self.hashMap = OutputLabel(self, "HASH COST:", 0)
        self.hashMap.grid(row = 2, sticky = W+E)

        self.binarySearchTreeDepth = OutputLabel(self, "ABB ORIGINAL DEPTH:", 0)
        self.binarySearchTreeDepth.grid(row = 3, sticky = W+E)

        self.binaryHeapDepth = OutputLabel(self, "HEAP DEPTH:", 0)
        self.binaryHeapDepth.grid(row = 4, sticky = W+E)

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

        print "WARNING: This program creates a folder named 'cache' where MovieApp will save movie covers."

        self.storeTree = MovieStoreTree()
        self.storeHeap = MovieStoreHeap()
        # self.storeHash = MovieStore()

        # self.storeBalanced = MovieStoreTree()    # A store based on a BST where movies from 'self._data' will be saved.
        # self.storeUnbalanced = MovieStoreTree()  # A store based on a BST where movies from 'self.store' will be saved.

        self._data = []                          # A hidden field that stores all movie entries to be added afterwards with add button.
        self._impDataIndex = 0                   # Index of the new movie to be imported.

        try:
            f = open(filename, 'r')
            self._data = f.readlines()
            f.close()
        except IOError:
            print "Error while trying to read file:", filename

        # UI/Private frame where all elements but the Status Bar are added
        innerFrame = Frame(master)
        innerFrame.grid(row = 0)

        # UI/Movie Display
        self.movieDisplay = MovieDisplay(innerFrame)
        self.movieDisplay.grid(row = 0)

        # UI/Benchmark Display
        self.benchmarkDisplay = BenchmarkDisplay(innerFrame)
        self.benchmarkDisplay.grid(row = 1, pady = 8)

        # UI/Buttons
        buttonFrame = Frame(innerFrame)
        buttonFrame.grid(row = 2, pady = 8)
        addMovieButton = Button(buttonFrame, text = "Add Movie", command = self.addMovie).grid(row = 0, column = 0, sticky = W+E+N+S)
        searchMovieButton = Button(buttonFrame, text = "Search", command = self.searchFilteredMovies).grid(row = 0, column = 1, sticky = W+E+N+S)
            # UI/Buttons for debugging purposes
        printTreeButton = Button(buttonFrame, text = "Print Tree", command = self.printTree).grid(row = 1, column = 0, sticky = W+E+N+S)
        printHeapButton = Button(buttonFrame, text = "Print Heap", command = self.printHeap).grid(row = 1, column = 1, sticky = W+E+N+S)

        # UI/Inputs
        inputFrame = Frame(innerFrame)
        inputFrame.grid(row = 3, pady = 16)
        minRatingText = Label(inputFrame, text = "From: ").grid(row = 0, column = 0)
        maxRatingText = Label(inputFrame, text = "To: ").grid(row = 1, column = 0)
        self.minRatingInput = Entry(inputFrame)
        self.minRatingInput.grid(row = 0, column = 1, sticky = W+E+N+S)
        self.maxRatingInput = Entry(inputFrame)
        self.maxRatingInput.grid(row = 1, column = 1, sticky = W+E+N+S)

        master.protocol("WM_DELETE_WINDOW", self.onApplicationClose)

        self.statusBar = StatusBar(master)
        self.statusBar.grid(row = 1, sticky = W+E)
        self.updateStatusBar()

    def printTree(self):
        """ Prints the internal container of MovieStoreTree. """
        print self.storeTree.movies

    def printHeap(self):
        """ Prints the internal container of MovieStoreHeap. """
        print self.storeHeap.movies
    
    def showMovie(self, movie):
        """ Displays the current movie. """
        self.updateStatusBar()
        self.movieDisplay.setMovie(movie)

    def searchFilteredMovies(self):
        """  """
        min, max = self.getValidRatingInputs()

        # BENCHMARK - bTREE - SEARCH
        start = time.clock() * 1000000
        self.storeTree.setRatingFilter(min, max)
        self.storeTree.getFilteredMovies()
        end = time.clock() * 1000000
        self.benchmarkDisplay.binarySearchTree.set(end - start)

        # BENCHMARK - HEAP - SEARCH
        start = time.clock() * 1000000
        self.storeHeap.setRatingFilter(min, max)
        self.storeHeap.getFilteredMovies()
        end = time.clock() * 1000000
        self.benchmarkDisplay.binaryHeap.set(end - start)

    def addMovie(self):
        """ Adds a movie. """
        if self._impDataIndex < len(self._data):
            movie = Movie()
            movie.importFromString(self._data[self._impDataIndex])

            print "Adding movie '%s'..." % ( movie.title )

            # BENCHMARK - bTREE - ADD
            start = time.clock() * 1000000
            self.storeTree.insert(movie)
            end = time.clock() * 1000000
            self.benchmarkDisplay.binarySearchTree.set(end - start)
            self.benchmarkDisplay.binarySearchTreeDepth.set(self.storeTree.getDepth())

            # BENCHMARK - HEAP - ADD
            start = time.clock() * 1000000
            self.storeHeap.insert(movie)
            end = time.clock() * 1000000
            self.benchmarkDisplay.binaryHeap.set(end - start)
            self.benchmarkDisplay.binaryHeapDepth.set(self.storeHeap.getDepth())

            self._impDataIndex += 1
        else:
            print "No more movies available."

    def updateStatusBar(self):
        """ Updates the status bar text with some statistics. """
        text = "#: %d" % ( 100 )
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
