#
# author: olopezsa13
#

import math

class BinaryHeap():
    """
    A priority queue (min-heap) implementation used in each of the problems.
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
            s += "%s, " % e.__str__()
        return "[" + s[:-2] + "]"

class Program():
    """
    A program. A resource-hog one...
    """
    uid = 0
    def __init__(self, size = 0):
        self.uid = Program.uid
        self.size = float(size)
        Program.uid += 1
    def __str__(self):
        return "(%d) %dMB" % ( self.uid, self.size )
    def __repr__(self):
        return self.__str__()

class Disk():
    """
    Best disk representation ever. Who cares about B-Trees...
    """
    def __init__(self, size = 0):
        self.programs = []
        self.size = size
        self.currentSize = 0
    def install(self, p):
        if self.isInstallable(p):
            self.programs.append(p)
            self.currentSize += p.size
    def isInstallable(self, p):
        return p.size < self.size and p.size + self.currentSize <= self.size
    def __str__(self):
        s = ""
        for p in self.programs:
            s += "%s, " % str(p)
        return "[%s] %d/%d" % ( s[:-2], self.currentSize, self.size )
    def __repr__(self):
        return self.__str__()

def maxProgs(P, diskSize = 32):
    """
    This program returns a list with the maximum amount of programs possible within
    the disk size desired.

    The algorithm's complexity is O(n*log(n)), where 'n' is the quantity of programs
    supplied.

    This algorithm's approach is to select always the smallest program available and
    add it to the list.
    """
    def sortByProgramSize(p):
        return p.size

    d = Disk(diskSize)
    programList = BinaryHeap(sortByProgramSize)
    for program in P:
        programList.append(program)

    for program in programList:
        if d.isInstallable(program):
            d.install(program)

    return d

def maxSpace(P, diskSize = 32):
    """
    This program returns a list of programs that fills as much as possible the disk space.

    As the other implementation, this algorithm's complexity is O(n*log(n)), where 'n' is
    te quantity of programs supplied.

    This algorithm's approach is to select those programs whose ratio between the disk's
    space and the program's size is near or are 1. A program whose ratio is near or is 1
    means that could fill almost or totally the disk space.

    Something to be noted is that it does not always return the optimal solution. For
    example, the file "disk02.in", with a disk size of 63MB should return:
        
        [(85) 23MB, (81) 19MB, (80) 13MB, (82) 7MB, (83) 1MB] 63/63
    
    This configuration fills all the disk space. Instead it returns:

        [(85) 23MB, (81) 19MB, (80) 5MB, (82) 13MB, (83) 1MB, (84) 1MB] 62/63

    The heuristic is not always succeful selecting the best program for the current problem.
    """
    def sortByProgramDiskRatio(p):
        return diskSize / p.size

    d = Disk(diskSize)
    programList = BinaryHeap(sortByProgramDiskRatio)
    for program in P:
        programList.append(program)

    for program in programList:
        if d.isInstallable(program):
            d.install(program)

    return d

def readProgramList(file):
    programList = []
    with open(file) as handle:
        lines = handle.readlines()
        for line in lines:
            programSize = float(line.strip())
            programList.append(Program(programSize))
    return programList

"""
AWFULL PROBLEM WITH CURRENT IMPLEMENTATION

It does not make sense to iterate a binary heap, if you don't
pop the elements from the heap. Iteration in both algorithms is
broken and should be fixed!
"""
print maxProgs(readProgramList('inputs/disk00.in'), 6)
print maxSpace(readProgramList('inputs/disk00.in'), 6)
print maxProgs(readProgramList('inputs/disk01.in'), 6)
print maxSpace(readProgramList('inputs/disk01.in'), 6)
print maxSpace(readProgramList('inputs/disk01.in'), 55)
print maxSpace(readProgramList('inputs/disk02.in'), 63)
