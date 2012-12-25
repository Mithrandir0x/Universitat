# LOPEZ SANCHEZ ORIOL
#
# P5.py
#
# author: olopezsa13
#

import math

"""
README!

IT IS HIGHLY RECOMMENDED TO EXECUTE THIS PROGRAM UNDER UNIX
ENVIRONMENT.

WINDOWS DOES NOT LOVE TERMINAL COLOURS...

IF IT IS NECESSARY TO EXECUTE THIS PROGRAM UNDER THE CLUNKY
WINDOWS CMD, COMMENT LINE 126 AND UNCOMMENT LINE 125.

NO CAPS-LOCK WAS HURT WHILE WRITING THIS MESSAGE.
"""

class BinaryHeap():
    """
    A priority queue (min-heap) implementation.
    """
    def __init__(self, scoreFunction):
        if scoreFunction == None:
            raise Exception('A score function must be passed by.')
        self.data = []
        self.sf = scoreFunction

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return self._next()

    def _next(self):
        n = len(self.data)
        i = 0
        while i < n:
            yield self.data[i]
            i += 1

    def append(self, o):
        self.data.append(o)
        self._bubbleUp(len(self.data) - 1)

    def pop(self):
        if len(self.data) > 0:
            result = self.data[0]
            end = self.data.pop()
            if len(self.data) > 0:
                self.data[0] = end
                self._sinkDown(0)
            return result
        else:
            raise Exception("Trying to pop from an empty heap.")

    def peak(self, i = None):
        l = len(self.data)
        if i != None and i < l:
            return self.data[i]
        elif l > 0:
            return self.data[0]
        else:
            return None

    def _bubbleUp(self, n):
        node = self.data[n]
        while n > 0:
            parentNodeIndex = int(math.floor((n+1)/2) - 1)
            parentNode = self.data[parentNodeIndex]
            if self.sf(node) < self.sf(parentNode):
                self.data[parentNodeIndex] = node
                self.data[n] = parentNode
                n = parentNodeIndex
            else:
                break

    def _sinkDown(self, n):
        length = len(self.data)
        element = self.data[n]
        while True:
            rightChildIndex = ( n + 1 ) * 2
            leftChildIndex = rightChildIndex - 1
            swapIndex = None
            leftChild = None
            rightChild = None
            if leftChildIndex < length:
                leftChild = self.data[leftChildIndex]
                if self.sf(leftChild) < self.sf(element):
                    swapIndex = leftChildIndex
            if rightChildIndex < length:
                rightChild = self.data[rightChildIndex]
                resultComparison = None
                if swapIndex == None:
                    resultComparison = self.sf(rightChild) < self.sf(element)
                else:
                    resultComparison = self.sf(rightChild) < self.sf(leftChild)
                if resultComparison:
                    swapIndex = rightChildIndex
            if swapIndex:
                self.data[n] = self.data[swapIndex]
                self.data[swapIndex] = element
                n = swapIndex
            else:
                break
    def __str__(self):
        s = ""
        for e in self.data:
            s += "%s (%d), " % ( e.__str__(), self.sf(e) )
        return "[" + s[:-2] + "]"

class Cell():
    """
    Data structure that represents a cell of the sudoku.
    """
    def __init__(self):
        self.value = None
        self.locked = False
    def __str__(self):
        if self.value == None:
            return " "
        if not self.locked:
            #return str(self.value)
            return "\033[1;33m%s\033[0m" % ( str(self.value) )
        else:
            return str(self.value)
    def __repr__(self):
        return self.__str__()

class Sudoku():
    """
    Data structure that represents a sudoku.
    """
    def __init__(self):
        self.data = [ [ Cell() for j in range(9) ] for i in range(9) ]
    def __getitem__(self, key):
        return self.data[key]
    def __str__(self):
        s = ""
        for i in range(9):
            for j in range(9):
                s += str(self.data[i][j]) + " "
                if j in [2, 5]:
                    s += "| "
            if i in [2, 5]:
                s += "\n------+-------+------"
            s += "\n"
        return s[:-1]
    def candidates(self, row, column):
        c = [ i + 1 for i in range(9) ]
        for i in range(9):
            if self.data[row][i].value in c:
                c.remove(self.data[row][i].value)
            if self.data[i][column].value in c:
                c.remove(self.data[i][column].value)
        for i in range(( row / 3 ) * 3, (( row / 3 ) * 3 ) + 3):
            for j in range(( column / 3 ) * 3, (( column / 3 ) * 3 ) + 3):
                if self.data[i][j].value in c:
                    c.remove(self.data[i][j].value)
        return c
    def read_from_file(self, path):
        with open(path) as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i > 9:
                    break
                for j, c in enumerate(line):
                    if j > 9:
                        break
                    try:
                        c = int(c)
                        self.data[i][j].value = c
                        self.data[i][j].locked = True
                    except ValueError:
                        pass

class Delta():
    """
    A little container that stores a different value of a cell
    of the sudoku.
    """
    def __init__(self, i, j, old):
        self.i = i
        self.j = j
        self.old = old
    def __str__(self):
        return "(%s, %s) = %s" % ( self.i, self.j, self.old )

REC_COUNTER = 0

def add_recursion():
    global REC_COUNTER
    REC_COUNTER += 1
    return REC_COUNTER

def naive_sudoku_resolution(S):
    """
    An implementation that solves a Sudoku. Returns True if the sudoku has been
    solved, otherwise, False.

    This algorithm goes through each row and column from the first row and column,
    and fills each empty cell with a valid value.

    Obviously, the solution proposed is not unique.
    """
    WRONG_BRANCH = 0
    PASS = 1
    SUDOKU_SOLVED = 2

    def candidates(row, column):
        """
        Returns a list of integer values that can be put in the cell at the
        row and column supplied.
        """
        c = [ i + 1 for i in range(9) ]
        for i in range(9):
            # The row restriction
            if S[row][i].value in c:
                c.remove(S[row][i].value)
            # The column restriction
            if S[i][column].value in c:
                c.remove(S[i][column].value)
        # The submatrix restriction
        for i in range(( row / 3 ) * 3, ( ( row / 3 ) * 3 ) + 3):
            for j in range(( column / 3 ) * 3, ( ( column / 3 ) * 3 ) + 3):
                if S[i][j].value in c:
                    c.remove(S[i][j].value)
        return c

    def revert_cells_states(deltas):
        """
        Whenever a branch of the algorithm leads to an unsatisfactional
        solution of the sudoku, it is necessary to revert all the changes
        done on the current recursive call. 
        """
        for delta in deltas:
            S[delta.i][delta.j].value = delta.old

    def fill(deltas, diagonal_index, i, j):
        """
        This method fills the empty cell at (i, j) with a valid number.

        It returns SUDOKU_SOLVED if the sudoku has been solved, or WRONG_BRANCH
        if it is not possible to solve the sudoku with the possible numbers 
        at the current cell.

        If the cell at (i, j) is locked, then it simply returns PASS.
        """
        if not S[i][j].locked and S[i][j].value == None:
            numList = candidates(i, j)
            if len(numList) > 1:
                """
                The branching heuristic. Quite simple and stoopid.

                For each value possible at the current cell, get one value and
                set it to the cell, and next branch to the next cell of the row
                or column.
                """
                old = S[i][j].value
                for number in numList:
                    S[i][j].value = number
                    if j < 9:
                        solved = solve(diagonal_index, i, j + 1)
                    else:
                        solved = solve(diagonal_index, i + 1, j)
                    if solved:
                        return SUDOKU_SOLVED
                S[i][j].value = old
                revert_cells_states(deltas)
                return WRONG_BRANCH
            elif len(numList) == 1:
                """
                If there's only one value possible for the current cell, just
                annotate its position to the list of deltas, and assign it to the cell.
                """
                deltas.append(Delta(i, j, S[i][j].value))
                S[i][j].value = numList[0]
            else:
                revert_cells_states(deltas)
                return WRONG_BRANCH
        return PASS

    def solve(diagonal_index = 0, starting_row = 0, starting_column = 0):
        """
        The recursive method that walks through each cell of the sudoku,
        filling it if possible with a valid value.
        """
        i = starting_row
        j = starting_column
        deltas = []
        add_recursion()
        while True:
            """
            Let's talk a little about this loop. Essentially, in each iteration of 
            this loop, we look at the row and column at "diagonal_index", starting
            from (diagonal_index, diagonal_index).

            Then why use "starting_row" and "starting_column"? When traversing the
            matrix, eventually, there will be a cell which may hold multiple numbers,
            so "solve" will be called recursively, and this loop's state should be
            maintained on each recursion.
            """
            if diagonal_index == 9:
                """
                The recursion exit condition.

                If "diagonal_index" is 9, it means that every cell's value is a valid
                value and the sudoku has been solved.
                """
                return True
            while j < 9:
                """
                This loop goes through the row at "diagonal_index".
                """
                result = fill(deltas, diagonal_index, i, j)
                if result == WRONG_BRANCH:
                    return False
                elif result == SUDOKU_SOLVED:
                    return True
                j += 1
            j_aux = diagonal_index
            while i < 9:
                """
                This loop goes through the column at "diagonal_index".
                """
                result = fill(deltas, diagonal_index, i, j_aux)
                if result == WRONG_BRANCH:
                    return False
                elif result == SUDOKU_SOLVED:
                    return True
                i += 1
            diagonal_index += 1
            i = j = diagonal_index
    return solve()

def minrc_sudoku_resolution(S):
    """
    An alternative implementation to the proposed one. Following the same pattern,
    it returns True if the sudoku could be solved, or False if not.

    With this algorithm, instead of blindly iterating over each empty cell in order,
    the algorithm searches always for the cell with the lowest amount of empty cells
    in both row and column. Thus converging faster to a posible solution.
    """
    def sort_by_rowcolumn_spaces(p):
        """
        The sorting criteria for the binary heap. Sort by the number of empty cells
        available at a specific row and column.
        """
        row, column = p[0], p[1]
        emptyFills = 0
        for i in range(9):
            if S[i][column].value == None:
                emptyFills += 1
        for j in range(9):
            if S[row][j].value == None:
                emptyFills += 1
        emptyFills -= 2
        return emptyFills

    def candidates(row, column):
        """
        Returns a list of integer values that can be put in the cell at the
        row and column supplied.
        """
        c = [ i + 1 for i in range(9) ]
        for i in range(9):
            # The row restriction
            if S[row][i].value in c:
                c.remove(S[row][i].value)
            # The column restriction
            if S[i][column].value in c:
                c.remove(S[i][column].value)
        # The submatrix restriction
        for i in range(( row / 3 ) * 3, ( ( row / 3 ) * 3 ) + 3):
            for j in range(( column / 3 ) * 3, ( ( column / 3 ) * 3 ) + 3):
                if S[i][j].value in c:
                    c.remove(S[i][j].value)
        return c

    def revert_cells_states(deltas):
        """
        Whenever a branch of the algorithm leads to an unsatisfactory
        solution of the sudoku, it is necessary to revert all the changes
        done on the current recursive call.

        There's a little difference with the other implementation. As the
        queue is modified when a position is popped from it, it is necessary
        to add these positions again to the queue.
        for delta in deltas:
            S[delta.i][delta.j].value = delta.old
            route.append((delta.i, delta.j))
        """
        for k in range(len(deltas) - 1, -1, -1):
            S[deltas[k].i][deltas[k].j].value = deltas[k].old
            route.append((deltas[k].i, deltas[k].j))

    """
    A priority queue is created with each of the empty cells of the sudoku, sorted
    by increasing quantity of the sum of empty cells in rows and columns.
    """
    route = BinaryHeap(sort_by_rowcolumn_spaces)
    for i in range(9):
        for j in range(9):
            if not S[i][j].locked:
                route.append((i, j))
    print len(route)

    def solve():
        """
        The recursive call that solves the sudoku.
        """
        add_recursion()
        deltas = []
        while True:
            """
            In stark contrast with the loop of the naive implementation, this loop
            iterates over all the empty cells stored in the priority queue, instead of
            iterating over each of the rows and columns starting from the diagonal.
            """
            if len(route) == 0:
                return True
            i, j = route.pop()
            numList = candidates(i, j)
            if len(numList) > 1:
                """
                Same ol' simple and stoopid branching heuristic.

                It performs the same way as in the naive approach.
                """
                old = S[i][j].value
                for number in numList:
                    S[i][j].value = number
                    solved = solve()
                    if solved:
                        return solved
                S[i][j].value = old
                route.append((i, j))
                revert_cells_states(deltas)
                return False
            elif len(numList) == 1:
                deltas.append(Delta(i, j, S[i][j].value))
                S[i][j].value = numList[0]
            else:
                route.append((i, j))
                revert_cells_states(deltas)
                return False
    return solve()

"""
To compare the performance of both algorithms, in a very simple way, both do
increase a global counter that indicates how many iterations have been done.

I initially expected that the second implementation would outperform the first
one:

    s0.in, 37, 19   , 17  
    s1.in, 46, 52   , 25
    s3.in, 72, 29936, 1405

And It seemed initially that the amount of empty cells was directly related to the 
quantity of recursive calls done by each algorithm, but both files "s5.in" and "s6.in"
proved wrong such statement:

    s5.in, 56, 13746, 379
    s6.in, 55, 8967 , 2821

And there are some cases that the second algorithm performs considerably worse than
the naive approach:

    s2.in, 56, 19085, 101370
    s4.in, 53, 2385 , 14936

It heavily depends on the sudoku's configuration to see how it will perform.

Table descriptions:
    - The first column is the file with the sudoku
    - The second column is the quantity of empty cells.
    - The third column is the quantity of recursive calls done by the naive algorithm.
    - The fourth column is the quantity of recursive calls done by the minrc algorithm.
"""
files = [ 's%d.in' % i for i in range(7) ]
for file in files:
    REC_COUNTER = 0
    print "----------------------------"
    s = Sudoku()
    s.read_from_file('inputs/' + file)
    print s
    print naive_sudoku_resolution(s), REC_COUNTER
    print
    print s
    print
    s = Sudoku()
    s.read_from_file('inputs/' + file)
    REC_COUNTER = 0
    print minrc_sudoku_resolution(s), REC_COUNTER
    print
    print s
    print "----------------------------"
    print
