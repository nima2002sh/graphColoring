import copy

class Node:

    def __init__(self,citiesColor,domain,degreeList,parent):
        self.citiesColor = citiesColor
        self.domain = domain
        self.degreeList = degreeList
        self.parent = parent


class CSP:

    def __init__(self,map):
        self.map = map
        self.numberOfCities = len(map)
        self.numberOfColors = 3
        # self.citiesColor = [0] * self.numberOfCities
        # self.domains = self.createInitalDomain()
        # self.degreeList = self.setDegree()
        # self.initialNode = Node(self.citiesColor,None)

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
        bestCities = []
        maxDegree = 0
        for city in expendList:
            if degreeList[city] >= maxDegree:
                maxDegree = degreeList[city]
        for city in expendList:
            if degreeList[city] == maxDegree:
                bestCities.append(city)       
        return bestCities

    def MRV(self,domains):
        expendList = []
        minDomane = self.numberOfColors
        for i in range(self.numberOfCities):
            if len(domains[i]) < minDomane and len(domains[i])!=0:
                minDomane = len(domains[i])
        for i in range(self.numberOfCities):
            if len(domains[i]) == minDomane:
                expendList.append(i)
        return expendList

    def LCV(self,city,domain):
        numberOfColor = [0] * self.numberOfColors
        bestColors = []
        for i in range(self.numberOfCities):
            if self.map[city][i] == 1:
                for color in (domain[i]):
                    numberOfColor[color-1]+=1
        for i in range(self.numberOfColors):
            if numberOfColor[i]==0:
                numberOfColor[i]=float('inf')
        for i in range(self.numberOfColors):
            if numberOfColor[i] == min(numberOfColor) and i+1 in domain[city]:
                bestColors.append(i+1)
        return bestColors

    def setDomain(self,newDomain,color,city):
        for i in range(self.numberOfCities):
            if self.map[city][i] == 1:
                for domain in newDomain[i]:
                    if domain == color:
                        newDomain[i].remove(color)
                        break
        newDomain[city].clear()
        return newDomain

    def solve(self):
        citiesColor = [0] * self.numberOfCities
        domains = self.createInitalDomain()
        degreeList = self.setDegree()
        initialNode = Node(citiesColor,domains,degreeList,None)
        self.backTrack(initialNode)

    def backTrack(self,node):
        newCitiesColor = copy.deepcopy(node.citiesColor)
        newDegreeList = copy.deepcopy(node.degreeList)
        newDomain = copy.deepcopy(node.domain)
        expendList = self.MRV(node.domain)
        if expendList:
            bestCities = self.getBestCity(node.degreeList,expendList)
            for city in bestCities:
                bestColors = self.LCV(city, node.domain)
                for color in bestColors:
                    newCitiesColor[city] = color
                    newDegreeList[city] = -1
                    newDomain = self.setDomain(newDomain,color,city)
                    newNode = Node(newCitiesColor,newDomain,newDegreeList,node)
                    for i in range(self.numberOfCities):
                        number = 0
                        if newDegreeList[i] == -1:
                            number+=1
                    if number==self.numberOfCities:
                        print(node.citiesColor)
                        return
                    self.backTrack(newNode)
        else:
            for color in node.citiesColor:
                if color == 0:
                    return
            print(node.citiesColor)
            return
        
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
MyMap=[
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
MyCSP = CSP(MyMap)
MyCSP.solve()