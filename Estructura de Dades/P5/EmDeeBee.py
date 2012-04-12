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
    def add(self, data):
        """
        @Overrides
        Adds the new element depending on its priority.
        """
        if self.isEmpty():
            # Consider the empty queue as a special case
            self.tail = Node(data)
            self.head = self.tail
        else:
            self._add(self.head, data)
        self.size += 1

    def _add(self, node, data):
        """
        'Private' recursive method called by 'self.add'.

        It iterates over every element in the queue until it finds the right
        spot where the new 'data' must be inserted.

        Obviously, this method updates the 'head' or 'tail' whenever it is
        necessary.
        """
        if data > node.data:
            if node.right == None:
                # The actual node is the 'tail'
                newNode = Node(data, node)
                node.right = newNode
                self.tail = newNode
            else:
                # Advance to the right node to find the adequate place
                self._add(node.right, data)
        else:
            newNode = Node(data, node.left, node)
            if node.left == None:
                # The left of a node is only empty if the actual node is the 'head'.
                node.left = newNode
                self.head = newNode
            else:
                node.left.right = newNode
                node.left = newNode

class PriorityQueue:
    """
    Implementation of a PriorityQueue based on a binary heap.

    Adding elements to the priority queue has O(log n) complexity.
    Removing elements from the priority queue has O(log n) complexity.

    Do not use this data structure with an ordered set of items, or it will become a
    degenerate tree, uprising operations complexity to O(n^2).

    The priority of the elements is evaluated by their own comparator implementation.
    """
    def __init__(self):
        self.root = None

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
        self._add(self.root, element)

    def _add(self, root, element):
        """
        'Private' recursive method used by 'self.add' to add an element in the queue.
        """
        if root == None:
            root = Node()
            root.data = element
        else:
            # When adding an element from the actual node, all elements less important
            # than the actual node are ALWAYS in the left branch, but the most importants
            # are on the right branch
            if root.data > element:
                self._insert(root.left, element)
            else:
                self._insert(root.right, element)

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

        self.insertionTime = None # This field indicates the time it took the movie to be inserted in the store.
    
    def __cmp__(self, other):
        """ Comparator overloading. """
        if self.rating < other.rating:
            return -1
        elif self.rating == other.rating:
            return 0
        else:
            return 1
    
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
    This class acts as a storage and at the same time a Data Access Object
    to provide information about the movie.
    """
    def __init__(self, filename = None):
        """
        Given a string containing the name of the file, it tries to
        parse the file information, looking up for movies data.
        """
        self.movies = LinkedListPriorityQueue()

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
        """ Inserts a new movie. """
        if movieStringData:
            movie = Movie().importFromString(movie)
        self.movies.add(movie)

    def getMoviesByRating(self, min, max):
        """
        Returns an array containing the movies which rating
        is between 'min' and 'max'.
        """
        showMovies = []
        for movie in self.movies:
            rating = int(movie.rating * 10)
            if rating <= max:
                if rating >= min:
                    showMovies.append(movie)
            else:
                break
        print len(showMovies)
        return showMovies

    def size(self):
        """ Returns the amount of movies stored. """
        return len(self.movies)

class MovieDisplay(Frame):
    """ This widget displays Movie information. """
    def __init__(self, master):
        """ Constructor. It creates all the needed components to render movie data. """
        Frame.__init__(self, master)

        self.titleText = StringVar()
        self.titleLabel = Label(self, text = "Title:").grid(row = 0, sticky = W)
        self.title = Label(self, textvariable = self.titleText)
        self.title.grid(row = 0, column = 1)

        self.directorText = StringVar()
        self.directorLabel = Label(self, text = "Director: ").grid(row = 1, sticky = W)
        self.director = Label(self, textvariable = self.directorText, width = 40, wraplength = 256)
        self.director.grid(row = 1, column = 1)

        self.yearText = StringVar()
        self.yearLabel = Label(self, text = "Year: ").grid(row = 2, sticky = W)
        self.year = Label(self, textvariable = self.yearText)
        self.year.grid(row = 2, column = 1)

        self.ratingText = StringVar()
        self.ratingLabel = Label(self, text = "Rating: ").grid(row = 3, sticky = W)
        self.rating = Label(self, textvariable = self.ratingText)
        self.rating.grid(row = 3, column = 1)   

        self.insertionText = StringVar()
        self.insertionLabel = Label(self, text = "Insertion: ").grid(row = 4, sticky = W)
        self.insertion = Label(self, textvariable = self.insertionText)
        self.insertion.grid(row = 4, column = 1)

        self.picture = Canvas(self, width = 100, height = 168, bg = "black")
        self.picture.grid(row = 0, column = 2, rowspan = 4, padx = 4)
        self.photoImage = None

    def setMovie(self, movie):
        """
        Given a "movie" object, the display will modify its data to
        show the movie information provided.
        """
        self.titleText.set(movie.title)
        if isinstance(movie.director, types.StringTypes):
            self.directorText.set(movie.director)
        else:
            self.directorText.set(', '.join(movie.director))
        self.yearText.set(movie.year)
        self.ratingText.set(movie.rating)
        self.insertionText.set(movie.insertionTime)
        self._setMoviePicture(movie.coverUrl)

    def reset(self):
        self.titleText.set("")
        self.directorText.set("")
        self.yearText.set("")
        self.ratingText.set("")
        self.insertionText.set("")
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
                print "Creating '%s'..." % ( imagePath )
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

        self.store = MovieStore()  # This is where all the movies are stored.

        self._data = []            # A hidden field that stores all movie entries to be added afterwards with add button.
        self._impDataIndex = 0     # Index of the new movie to be imported.

        self.movies = []           # An array of the movies loaded from the store.
        self.currentMovieIndex = 0 # Index of the current movie being displayed.

        self.lastJobTimeTaken = None  # It indicates how much time has taken to add a new movie.
        self.lastFilteringTime = None # It indicates how much time has taken to get the filtered list of movies.

        self.movieDisplay = MovieDisplay(master)
        self.movieDisplay.grid(row = 0)

        buttonFrame = Frame(master)
        buttonFrame.grid(row = 1, pady = 8)
        addMovieButton = Button(buttonFrame, text = "Add Movie", command = self.addMovie).grid(row = 1, column = 0)
        nextMovieButton = Button(buttonFrame, text = "Next Movie", command = self.nextMovie).grid(row = 1, column = 1, sticky = W)

        inputFrame = Frame(master)
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
        self.statusBar.grid(row = 4, sticky = W+E+N+S)

        try:
            f = open('peliculas100.dat', 'r')
            self._data = f.readlines()
            f.close()
        except IOError:
            print "Error while trying to read file:", 'peliculas100.dat'

        #self.showMovie()
    
    def showMovie(self):
        """ Displays the current movie. """
        try:
            self.updateStatusBar()
            self.movieDisplay.setMovie(self.movies[self.currentMovieIndex])
        except IndexError:
            self.movieDisplay.reset()
            print "Movie information at index '%d' is not available." % ( self.currentMovieIndex )

    def nextMovie(self):
        """
        Displays the movie next to the current one. Notice that if the last
        movie is being displayed, the next movie will be the first one.
        """
        self.currentMovieIndex += 1
        if self.currentMovieIndex >= len(self.movies):
            self.currentMovieIndex = 0

        self.showMovie()

    def addMovie(self):
        """ Adds a movie. """
        if self._impDataIndex < len(self._data):
            movie = Movie()
            movie.importFromString(self._data[self._impDataIndex])

            print "Adding movie '%s'..." % ( movie.title )
            
            start = time.clock() * 1000000
            self.store.insert(movie)
            end = time.clock() * 1000000
            movie.insertionTime = int(end - start)

            print "Time taken:", movie.insertionTime

            self.lastJobTimeTaken = end - start
            self._impDataIndex += 1
            self.updateMovieList(None)
        else:
            print "No more movies available."

    def updateMovieList(self, event):
        """ Updates the movie list. """
        min, max = self.getValidRatingInputs()

        self.currentMovieIndex = 0
        start = time.clock() * 1000000
        self.movies = self.store.getMoviesByRating(min, max)
        end = time.clock() * 1000000
        self.lastFilteringTime = end - start

        self.showMovie()

    def updateStatusBar(self):
        """ Updates the status bar text with some statistics. """
        text = "%d/%d (%d) (Last Addition: %sms / Last Filtering: %sms)" % ( self.currentMovieIndex + 1, len(self.movies), self.store.size(), self.lastJobTimeTaken, self.lastFilteringTime )
        self.statusBar.write(text)

    def getValidRatingInputs(self):
        """ Returns the valid minimum and maximum of rating to be accepted. """
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
