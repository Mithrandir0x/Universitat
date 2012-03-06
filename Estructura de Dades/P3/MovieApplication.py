#
# MovieApplication.py
#
# author: olopezsa13
#

from Tkinter import *

import Image
import ImageTk
import os
import random
import types
import urllib

class Movie:
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
    
    def __cmp__(self, other):
        """ Comparator overloading. """
        if self.title < other.title:
            return -1
        elif self.title == other.title:
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

        return "%s | %s | %s | %s" % ( self.title, directors, self.year, self.rating )
    
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

class MovieDisplay(Frame):
    """ This widget displays Movie information. """
    def __init__(self, master):
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
        self._setMoviePicture(movie.coverUrl)

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

        self.picture.create_rectangle(0, 0, 100, 168, fill = "black")

class MovieApp(Frame):
    """
    Main application.
    """
    def __init__(self, master, filename):
        """ Film data is loaded, and the GUI is stablished. """
        Frame.__init__(self, master)

        print "WARNING: This program creates a folder named 'cache' where MovieApp will save movie covers."

        self.movies = []           # An array containing the data of the movies
        self.currentMovieIndex = 0 # Index of the current movie being displayed.

        self.loadMovieFile(filename)
        self.movieDisplay = MovieDisplay(master)
        self.movieDisplay.grid(row = 0)

        self.nextMovieButton = Button(master, text = "Next Movie", command = self.nextMovie).grid(row = 1, column = 0, sticky = W)
        self.randomMovieButton = Button(master, text = "Random Movie", command = self.randomMovie).grid(row = 1, column = 1)

        self.showMovie()
    
    def showMovie(self):
        """ Displays the current movie. """
        try:
            print self.movies[self.currentMovieIndex]
            self.movieDisplay.setMovie(self.movies[self.currentMovieIndex])
        except IndexError:
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
        
    def randomMovie(self):
        """ Displays a random movie. It may be somewhat random, I don't sow many seeds... """
        if len(self.movies) > 0:
            self.currentMovieIndex = random.randint(0, len(self.movies) - 1)
            self.showMovie()
        
    def orderMovies(self):
        """
        Sorts "self.movies" by title increasing
        """
        # YOU U NO LIEK MERGESORT?
        self.movies = self._mergeSort(self.movies)

    def _mergeSort(self, movies):
        """
        Classic mergesort top-down implementation.

        @author John von Neumann
        """
        if len(movies) < 2:
            return movies

        half = len(movies) / 2
        left = self._mergeSort(movies[half:])
        right = self._mergeSort(movies[:half])
        return self._merge(left, right)

    def _merge(self, left, right):
        """
        The merge function, needed by mergesort.

        @author John von Neumann
        """
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
        result += left[i:]
        result += right[j:]
        return result

    def loadMovieFile(self, filename):
        """
        Given a string containing the name of the file, this method
        parses the file information, looking up for movies data.
        """
        print "Loading movies from '%s'" % ( filename )
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
                self.movies.append(movie)
                movieData = []

            self.orderMovies()
        except IOError:
            print "Error while trying to read file:", filename
            return

# Bootstrap
tk = Tk()
instance = MovieApp(master = tk, filename = "peliculas100.dat")

tk.mainloop()
