class Node:

    def __init__(self,state,parent):
        self.state = state
        self.parent = parent

class CSP:

    def __init__(self,map):
        self.map = map
        self.numberOfCities = len(map)
        self.numberOfColors = 4

    def createInitalDomain(self):
        domain = {}
        for i in range(self.numberOfCities):
            domain[i]=[]
            for j in range(self.numberOfColors):
                domain[i].append(j+1)
        return domain

    def setDegree(self):
        degreeList = []
        for i in range(numberOfCities):
            degree = 0
            for j in range(numberOfCities):
                if map[i][j] == 1:
                    degree+=1
            degreeList.append(degree)
        return degreeList

    def MRV(self,domains):
        expendList = []
        minDomane = self.numberOfColors
        for i in range(numberOfCities):
            if len(domains[i]) < minDomane:
                minDomane = len(domains[i])
        for i in range(numberOfCities):
            if len(domains[i]) == minDomane:
                expendList.append(i)
        return expendList




SwedenMap = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
]
AustraliaMap=[
    [0,1,1,0,0,0,0],
    [1,0,1,1,0,0,0],
    [1,1,0,1,1,1,0],
    [0,1,1,0,1,0,0],
    [0,0,1,1,0,1,0],
    [0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0],
]