
import math
import networkx as nx

distance = distance
previous = previous

class Node:
    """
    The most basic element in a bi-directional linked structure.
    """
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev # Only used by EfficientQueue class.

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

    def append(self, data):
        """ Adds a new element at the beginning of the queue. """
        if self.isEmpty():
            # If the queue is empty, simply create a new node at the
            # end, and refer the head to this one
            self.tail = Node(data)
            self.head = self.tail
        else:
            temp = Node(data, self.head)
            self.head.prev = temp
            self.head = temp

    def pop(self):
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

        return temp

class BinaryHeap():
    """
    A min-heap structure.
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
        print self.data

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
        if len(self.data) == 0:
            return "[]"
        s = "["
        for e in self.data:
            s += "%s, " % e.__str__()
        return s[:-2] + "]"

def dfs(G):
    path = []
    for node in G:
        G[node]['explored'] = False
    
    def explore(n):
        G[n]['explored'] = True
        for neighbourNode in G.neighbours(n):
            if not G[neighbourNode]['explored']:
                explore(neighbourNode)
        path.insert(n, 0)

    for node in G:
        if not G[node]['explored']:
            explore(node)

    return path

def bfs(G, s):
    q = Queue()
    inf = float('inf')
    for node in G:
        G[node][distance] = inf
        G[node][previous] = None
    G[s][distance] = 0
    q.append(s)
    while not q.isEmpty():
        u = q.pop()
        for _u, v in G.edges_iter(u):
            if G[v][distance] == inf:
                q.append(v)
                G[v][distance] = G[u][distance] + 1
                G[v][previous] = u

def dijkstra(G, s):
    """
    Given a directed graf G created with NetworkX, and G being a graf
    with every weight from the edge being positive, or zero, this method
    search the shortest path from the node s. 
    """
    def getDistFromNode(node):
        # This little function is used by the binary heap in order
        # to obtain a comparable value from the node.
        return G[node][distance]
    h = BinaryHeap(getDistFromNode)
    for node in G:
        G[node][distance] = float('inf')
        G[node][previous] = None
        h.append(node)
    G[s][distance] = 0
    while len(h) > 0:
        u = h.peak()
        for _u, v in G.edges_iter(u):
            if G[v][distance] > G[u][distance] + G[u][v]['l']:
                G[v][distance] = G[u][distance] + G[u][v]['l']
                G[v][previous] = u
                h.pop()

def bellman_ford_shortest_path(G, s):
    n = len(G.nodes) - 1
    for node in G:
        G[node][distance] = float('inf')
        G[node][previous] = None

    def update(u, v):
        d_v = G[v][distance]
        d_u_l = G[u][distance] + G[u][v]['l']
        G[v][distance] = min(d_v, d_u_l)
        if d_v > d_u_l:
            G[v][previous] = u

    while n > 0:
        for u, v in G.edges_iter():
            update(u, v)
        n -= 1

def dag_shortest_path(G, s):
    for node in G:
        G[node][distance] = float('inf')
        G[node][previous] = None
    G[s][distance] = 0
    linearizedG = dfs(G)

    def update(u, v):
        G[v][distance] = min(G[v][distance], G[u][distance] + G[u][v]['l'])

    for u in linearizedG:
        for _u, v in G.edges_iter(u):
            update(u, v)

G = nx.DiGraph([
    ('S', 'A', {"l":10}),
    ('S', 'G', {"l":8}),
    ('A', 'E', {"l":2}),
    ('B', 'A', {"l":1}),
    ('B', 'C', {"l":1}),
    ('C', 'D', {"l":3}),
    ('D', 'E', {"l":-1}),
    ('E', 'B', {"l":-2}),
    ('F', 'A', {"l":-4}),
    ('F', 'E', {"l":-1}),
    ('G', 'F', {"l":1})])

for u, v in G.edges_iter():
    print "(%s, %s) %s" % (u, v, G[u][v]['l'])
