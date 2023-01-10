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
        self.numberOfColors = 4
        self.solv = False

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
        maxDegree = 0
        for city in expendList:
            if degreeList[city] >= maxDegree:
                maxDegree = degreeList[city]
        for city in expendList:
            if degreeList[city] == maxDegree:
                bestCity = city       
        return bestCity

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
        colors = {}
        for color in domain[city]:
            colors[color] = 0
        for i in range(self.numberOfCities):
            if self.map[city][i] == 1:
                for color in (domain[i]):
                    if color in domain[city]:
                        colors[color]+=1
        minColor=min(colors.values())
        bestColors = [color for color in colors if colors[color]==minColor]
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
            bestCity = self.getBestCity(node.degreeList,expendList)
            expendList.remove(bestCity)
            bestColors = self.LCV(bestCity, node.domain)
            for color in bestColors:
                if self.solv:
                    return
                newCitiesColor[bestCity] = color
                newDegreeList[bestCity] = -1
                newDomain = self.setDomain(newDomain,color,bestCity)
                newNode = Node(newCitiesColor,newDomain,newDegreeList,node)
                self.backTrack(newNode)
        else:
            for color in newCitiesColor:
                if color == 0:
                    return
            print(node.citiesColor)
            self.solv = True
            return
        

MyMap=[
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
MyCSP = CSP(MyMap)
MyCSP.solve()


AustraliaMap=[
    [0,1,1,0,0,0,0],
    [1,0,1,1,0,0,0],
    [1,1,0,1,1,1,0],
    [0,1,1,0,1,0,0],
    [0,0,1,1,0,1,0],
    [0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0],
]
AustraliaMapCSP = CSP(AustraliaMap)
AustraliaMapCSP.solve()


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
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
]
SwedenCSP = CSP(SwedenMap)
SwedenCSP.solve()
