# Assignment 4
# Christopher Rico
# CS325
# OSU ID: 933239746

import sys
import math
from collections import deque

#we will link these classes together to form a graph
class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.visited = False
        self.predecessor = None
        self.distance = None


def listObj(vertices, objName):
    for object in vertices:
        if object.data == objName:
            return object
            break


#breadth-first search
def bfs(inputGraph):
    queue = deque()
    faces = []
    heels = []
    impossible = False

    #for all the vertices in the graph
    for j in range(0, len(inputGraph)):
        #if a vertex has not been visited
        if inputGraph[j].visited == False:
            startingIndex = j
            #add it to the queue
            queue.append(startingIndex)
            inputGraph[startingIndex].distance = 0

            #while the queue is not empty
            while len(queue) > 0:
                #pop the first value off the queue and look at its neighbors
                currentVertexIndex = queue.popleft()
                currentNeighbors = inputGraph[currentVertexIndex].edges
                inputGraph[currentVertexIndex].visited = True

                #if the
                for i in range(0, len(currentNeighbors)):
                    if inputGraph[currentNeighbors[i]].visited == False:
                        inputGraph[currentNeighbors[i]].predecessor = currentVertexIndex
                        inputGraph[currentNeighbors[i]].distance = inputGraph[inputGraph[currentNeighbors[i]].predecessor].distance + 1
                        queue.append(currentNeighbors[i])


    for k in range(0, len(inputGraph)):
        #if distance is even, it's a face
        if inputGraph[k].distance % 2 == 0:
            for neighbors in inputGraph[k].edges:
                if inputGraph[neighbors].distance % 2 == 0:
                    impossible = True
            faces.append(inputGraph[k].data)
        #if distance is odd, it's a heel
        else:
            for neighbors in inputGraph[k].edges:
                if inputGraph[neighbors].distance % 2 != 0:
                    impossible = True
            heels.append(inputGraph[k].data)

    if impossible == True:
        return "Impossible", None
    else:
        return faces, heels




def main():
    #get filename from cmd line args, or just use "wrestler.txt"
    fileName = sys.argv[1] or "wrestler.txt"
    #read file in line-by-line and put contents of each line into array
    multiLineArray = open(fileName, "r").readlines()

    isArrayLine = True
    lineArray = []
    lineAmount = 0
    workingGraph = []

    ##construct the graph
    for j in range(0, len(multiLineArray)):
        #get rid of newlines and split the line based on spaces
        lineArray = multiLineArray[j].strip()
        lineArray = lineArray.split(" ")

        if len(lineArray) == 1:
            if lineArray[0].isdigit() != True:
                workingGraph.append(Vertex(lineArray[0]))

        else:
            rival1 = lineArray[0]
            rival2 = lineArray[1]

            obj1 = listObj(workingGraph, rival1)
            obj2 = listObj(workingGraph, rival2)

            index1 = workingGraph.index(obj1)
            index2 = workingGraph.index(obj2)

            workingGraph[index1].edges.append(index2)
            workingGraph[index2].edges.append(index1)


    result1, result2 = bfs(workingGraph)


    #if results are impossible to match
    if result1 == "Impossible":
        print(result1)

    #if there are possible rivalries
    else:
        print("Yes\n")

        print("Babyfaces: ")
        for faces in result1:
            print(str(faces) + " ")

        print("\nHeels: ")
        for heels in result2:
            print(str(heels) + " ")
        print("\n")


if __name__ == '__main__':
    main()
