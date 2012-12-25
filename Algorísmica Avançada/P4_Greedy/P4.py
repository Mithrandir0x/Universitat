#
# P4.py
#
# author: olopezsa13
#

import math
import networkx as nx
import random

"""
About file formats
------------------
    - knapsack_resolution
        Each line represents an item.
        Format of line:
            {WEIGHT}, {VALUE}

    - tasklist_resolution
        Each line represents a task.
        Format of line:
            {STARTING_HOUR}, {ÉXECUTION TIME}

    - kruskal_resolution
        Each line represents an edge of an undirected graph.
        Format of line:
            {STARTING_VERTEX} {ENDING_VERTEX} {EDGE_WEIGHT}
"""

class BinaryHeap():
    """
    A priority queue (min-heap) implementation used in every exercise.
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
        """
        """
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

class ExcessiveWeightException(Exception):
    """
    Who does not love over-engineering?
    """
    pass

class Thing():
    """
    A valuable thing that weights some kilos.
    """
    def __init__(self, weight = 0, value = 0):
        self.weight = float(weight)
        self.value = float(value)
    @property
    def ratio(self):
        if self.value != 0:
            return self.weight / self.value
        else:
            return None
    def __str__(self):
        return "(%s, %s, %s)" % ( self.weight, self.value, self.ratio )
        #return str(self.ratio)

    def __repr__(self):
        return self.__str__()

class Knapsack():
    """
    A cloth sack able to carry valuable thingies.
    """
    def __init__(self, maxWeight = 15):
        self.maxWeight = maxWeight
        self.weight = 0
        self.wealth = 0
        self.things = []
    @property
    def ratio(self):
        return self.weight / self.wealth
    def add(self, thing):
        if self.weight + thing.weight <= self.maxWeight:
            self.things.append(thing)
            self.weight += thing.weight
            self.wealth += thing.value
        else:
            raise ExcessiveWeightException()
    def allows(self, thing):
        return self.weight + thing.weight <= self.maxWeight
    def __str__(self):
        return "(w: %s, v: %s, r: %s, i: %s)" % ( self.weight, self.wealth, self.ratio, self.things.__str__() )

def knapsack_resolution(file, knWeight = 15):
    """
    Given a text file of objects described by its weight and value separated
    by comma, it tries to find an optimal combination of objects which have
    the greatest value possible. (Great for thieves)

    The algorithm's complexity is O(n), where n is the number of things in
    the list.

    Looking at the optimality of the algorithm, it should be said that it is
    not optimal. Let's make a counter-example by calling it with:

    knapsack_resolution('inputs/knapsack_2.in', knWeight = 12)

    It should return:
        (w: 12.0, v: 11.96, r: 1.00334448161, i: [(3.0, 2.99, 1.00334448161),
            (3.0, 2.99, 1.00334448161), (3.0, 2.99, 1.00334448161),
            (3.0, 2.99, 1.00334448161)])

    But instead, it returns:
        (w: 10.0, v: 11.0, r: 0.909090909091, i: [(10.0, 11.0, 0.909090909091)])

    Even though the ratio of the last knapsack is less than the expected one,
    the value of the expected one is greater than the given one. The minimal
    ratio of an item, or its combination does not always translate into an
    optimal selection.

    "knWeight" defines the maximum weight of the knapsack.
    """
    def scoreByRatio(thing):
        """
        This function is used by the binary heap used to return a numerical
        value used in the comparisons.
        """
        return thing.ratio
    def readThingList(file):
        """
        Return a binary heap of the things listed in the file and ordered
        increasingly by its ratio.
        """
        kn = BinaryHeap(scoreByRatio)
        with open(file) as handle:
            lines = handle.readlines()
            for line in lines:
                if line[0] != "#":
                    thingData = line.strip().replace(' ', '').rsplit(',')
                    if len(thingData)== 2:
                        t = Thing(thingData[0], thingData[1])
                        kn.append(t)
        return kn
    knapsack = Knapsack(knWeight)
    things = readThingList(file)
    while len(things) > 0:
        """
        The binary heap returned by "readThingList" is ordered by increasing ratio.
        This means that potentially, the things near the beginning of the structure
        are the best candidates to be fetched.

        But beware, it may happen to have an object with a good ratio, but weights
        more than the knapsack's capacity. Those objects, obviously, should be
        discarded.
        """
        t = things.pop()
        #print t
        if knapsack.allows(t):
            knapsack.add(t)
    print knapsack

def generate_sample_knapsack(file, n = 50, minWeight = 1, maxWeight = 15, minValue = 1, maxValue = 100):
    """
    This method writes a sample file of a knapsack.
    """
    with open(file, 'w') as handle:
        while n > 0:
            weight = int(minWeight + random.random() * maxWeight)
            value = int(minValue + random.random() * maxValue)
            handle.write(('%s, %s\n') % ( weight, value ))
            n -= 1

class Task():
    """
    A task with a snappy name.
    """
    uid = 0
    def __init__(self, startHour, worktime):
        self.name = "T%s" % Task.uid
        self.worktime = int(worktime)
        self.startHour = int(startHour)
        Task.uid += 1
    def __str__(self):
        return "(%s, %sh, %s)" % ( self.name, self.startHour, self.worktime )
    def __repr__(self):
        return self.__str__()

def tasklist_resolution(file, minutesPerHour = 60):
    """
    Given a list of tuples expressed by:

        T = [(SH(0), ET(0)), (SH(1), ET(1)), ... , (SH(M), ET(N))]

    and not expressed necessarily in a particular order, this method returns
    a list of tasks sorted so that it maximize the amount of tasks to be
    executed each hour.

    Any value of SH(n), 0 <= n <= M, may not be uniformly distributed, but
    they must be integer.

    The algorithm's complexity is O(N). N is the quantity of tasks.

    Starting hours must be positive integers.
    """
    def scoreByWorkTime(task):
        """
        Each of the priority queues should be ordered by increasing tasks'
        execution time.
        """
        return task.worktime
    def readTasksFile(file):
        """
        This method returns a tuple containing a 'dictionary', where each key is
        a specific hour defined in the file to be read, and its value is a binary
        heap with every task that begins at that hour, ordered increasingly by its
        execution time; and an 'integer', with the most late hour that a task can
        begin to execute.
        """
        tasks = {}
        with open(file) as handle:
            maxStartHour = -1
            lines = handle.readlines()
            for line in lines:
                if line[0] != "#":
                    taskData = line.strip().replace(' ', '').rsplit(',')
                    taskStartingHour = int(taskData[0])
                    if not taskStartingHour in tasks:
                        tasks[taskStartingHour] = BinaryHeap(scoreByWorkTime)
                    tasks[taskStartingHour].append(Task(taskStartingHour, taskData[1]))
                    if taskStartingHour > maxStartHour:
                        maxStartHour = taskStartingHour
        print maxStartHour
        return ( tasks, maxStartHour )
    tasks, maxStartHour = readTasksFile(file)
    tasksDone = [] # A list of all done tasks.
    t = 0 # Time accumulated executing tasks.
    h = 0 # Current hour.
    ah = 0 # Additional hour.
    _loop_0 = 0
    _loop_1 = 0
    while True:
        """
        With each iteration, we look up for the task with the lowest execution
        time possible that may begin.
        """
        minTaskWorktime = float('inf')
        taskHourGroup = None
        i = 0
        while i <= h and i <= maxStartHour:
            """
            For each iteration, the range of hours to look up goes from 0 to MAX[SH(n)], 0 <= n < M
            """
            if i in tasks and len(tasks[i]) > 0 and tasks[i].peak().worktime < minTaskWorktime:
                """
                Let's take a look at this group of conditions:
                
                  - "i in tasks": We look at every possible hour, looking for tasks to be fetched.
                    It may be possible that an hour does not even exist in the list of tasks,
                    so a check must be done to see if there are tasks.

                  - "len(tasks[i]) > 0": It may be possible that all the tasks have been done,
                    so the queue may be empty.

                  - "tasks[i].peak().worktime < minTaskWorktime": Verify if the first task of
                    the current queue is the smallest one to be done.
                
                So, why only peaking at the first element of each queue? The first element will be
                the task with the smallest execution time possible. So we're always looking at tasks
                with the smallest execution time.
                """
                minTaskWorktime = tasks[i].peak().worktime
                taskHourGroup = i
            i += 1
            _loop_1 += 1
        if taskHourGroup != None:
            task = tasks[taskHourGroup].pop()
            tasksDone.append(task)
            t += task.worktime
        else:
            if h > maxStartHour:
                break
            ah += 1
        print _loop_0, _loop_1, i, h, ah, t, task.name
        h = int( t / minutesPerHour ) + ah
        _loop_0 += 1
    print tasksDone
    print _loop_0, _loop_1

def generate_sample_tasklist(file, n = 20, minStartHour = 0, maxStartHour = 10, minWorkTime = 1, maxWorkTime = 120):
    with open(file, 'w') as handle:
        while n > 0:
            startHour = int(minStartHour + random.random() * minStartHour)
            workTime = int(minWorkTime + random.random() * maxWorkTime)
            handle.write(('%s, %s\n') % ( startHour, workTime ))
            n -= 1

class Edge():
    """
    A little class used to describe an edge of a graph.
    """
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = float(weight)
    def __str__(self):
        return "(%s, %s, weight: %s)" % ( self.u, self.v, self.weight )
    def __repr__(self):
        return self.__str__()

class DisjointedSet():
    """
    A little structure that will aid to keep track of the connected components
    of an undirected graph.

    This structure represents a forest of trees, representing the connectivity
    of a graph.
    """
    def __init__(self):
        self.root = {}
        self.rank = {}

    def append(self, u):
        """
        Create a new tree.
        """
        if not u in self.root:
            self.root[u] = u
            self.rank[u] = 0

    def find(self, u):
        """
        It returns the root node from the node being called.

        This algorithm has complexity O(Log(N)), being N the number
        of nodes of the tree.
        """
        while u != self.root[u]:
            u = self.root[u]
        return u

    def union(self, u, v):
        """
        Join the tree where 'u' is from to the tree where 'v' is from.

        This algorithm has complexity O(Log(N)), being N the number
        of nodes of the tree.
        """
        x = self.find(u)
        y = self.find(v)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.root[y] = self.root[x]
        else:
            self.root[x] = self.root[y]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

def kruskal_resolution(file):
    """
    Given a file with the content of an undirected graph, it finds the
    minimum spanning tree of the graph.

    The cost of the algorithm is, being E the number of edges, and V is the
    number of vertex of the graph:
        O(E*Log(V))
    """
    K = None
    forest = DisjointedSet()
    
    def scoreByWeight(edge):
        """
        When sorting the binary heap, do it by the edge's weight.
        """
        return edge.weight

    def readGraphFile():
        """
        This method returns a priority queue containing all the edges of an
        undirected graph, ordered by weight increasing read from a file.
        """
        pq = BinaryHeap(scoreByWeight)
        with open(file) as handle:
            lines = handle.readlines()
            for line in lines:
                if line[0] != "#":
                    edge_data = line.strip().rsplit(' ')
                    if len(edge_data) == 3:
                        e = Edge(edge_data[0], edge_data[1], edge_data[2])
                        pq.append(e)
                        forest.append(edge_data[0])
                        forest.append(edge_data[1])
        return pq

    K = nx.Graph()
    sorted_edges_weight = readGraphFile()
    for edge in sorted_edges_weight:
        if forest.find(edge.u) != forest.find(edge.v):
            # Verify that the current edge may be in a cycle.
            K.add_node(edge.u)
            K.add_node(edge.v)
            K.add_edge(edge.u, edge.v, weight = edge.weight)
            forest.union(edge.u, edge.v)
    print forest.root
    print forest.rank
    print K.nodes()
    print K.edges()

#generate_sample_knapsack('inputs/knapsack_10.in', n = 10)
#knapsack_resolution('inputs/knapsack.in')
#knapsack_resolution('inputs/knapsack_10.in')
#knapsack_resolution('inputs/knapsack_2.in', knWeight = 12) #Demonstrates unoptimal behaviour of the algorithm

#tasklist_resolution('inputs/tasklist.in')
#tasklist_resolution('inputs/tasklist_2.in')
#tasklist_resolution('inputs/tasklist_3.in')

#kruskal_resolution('inputs/kruskal_1.in')
#kruskal_resolution('inputs/kruskal_2.in')
#kruskal_resolution('inputs/kruskal_3.in')
