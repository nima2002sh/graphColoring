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
        for i in range(self.numberOfCities):
            degree = 0
            for j in range(self.numberOfCities):
                if self.map[i][j] == 1:
                    degree+=1
            degreeList.append(degree)
        return degreeList

    def getBestCity(self,degreeList,expendList):
        bestCitis = []
        maxDegree = 0
        for city in expendList:
            if degreeList[city] >= maxDegree:
                maxDegree = degreeList[city]
        for city in expendList:
            if degreeList[city] == maxDegree:
                bestCitis.append(city)       
        return bestCitis

    def MRV(self,domains):
        expendList = []
        minDomane = self.numberOfColors
        for i in range(self.numberOfCities):
            if len(domains[i]) < minDomane:
                minDomane = len(domains[i])
        for i in range(self.numberOfCities):
            if len(domains[i]) == minDomane:
                expendList.append(i)
        return expendList

    def LCV(self,city,domain):
        numberOfColor = [0] * self.numberOfColors
        for i in range(numberOfCities):
            if self.map[city][i] == 1:
                for color in (domain[i]):
                    numberOfColor[color-1]+=1
        bestColor = numberOfColor[numberOfColor.index(min(numberOfColor))]+1
        return bestColor




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

AustraliaCSP = CSP(AustraliaMap)
AustraliaCSP.solve()