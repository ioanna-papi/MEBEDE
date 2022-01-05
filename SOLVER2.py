from VRP import *

class Solution:
    def __init__(self):
        self.profit = 0
        self.routes = []
        
class RelocationMove(object):
    def __init__(self):
        self.originRoutePosition = None
        self.targetRoutePosition = None
        self.originNodePosition = None
        self.targetNodePosition = None
        self.costChangeOriginRt = None
        self.costChangeTargetRt = None
        self.moveCost = None

    def Initialize(self):
        self.originRoutePosition = None
        self.targetRoutePosition = None
        self.originNodePosition = None
        self.targetNodePosition = None
        self.costChangeOriginRt = None
        self.costChangeTargetRt = None
        self.moveCost = 10 ** 9

        
class SwapMove(object):
    def __init__(self):
        self.positionOfFirstRoute = None
        self.positionOfSecondRoute = None
        self.positionOfFirstNode = None
        self.positionOfSecondNode = None
        self.costChangeFirstRt = None
        self.costChangeSecondRt = None
        self.moveCost = None
    def Initialize(self):
        self.positionOfFirstRoute = None
        self.positionOfSecondRoute = None
        self.positionOfFirstNode = None
        self.positionOfSecondNode = None
        self.costChangeFirstRt = None
        self.costChangeSecondRt = None
        self.moveCost = 10 ** 9



class TwoOptMove(object):
    def __init__(self):
        self.positionOfFirstRoute = None
        self.positionOfSecondRoute = None
        self.positionOfFirstNode = None
        self.positionOfSecondNode = None
        self.moveCost = None
    def Initialize(self):
        self.positionOfFirstRoute = None
        self.positionOfSecondRoute = None
        self.positionOfFirstNode = None
        self.positionOfSecondNode = None
        self.moveCost = 10 ** 9

class Solver2:
    
    def __init__(self, m):
        self.allNodes = m.allNodes
        self.depot = m.allNodes[0]
        self.distanceMatrix = m.matrix
        self.timeMatrix = m.time
        self.total_route_time = 0
        self.total_route_profit = 0
        self.sol = Solution()
        self.bestSolution = Solution()
        self.route = None
    
    def solve(self):
        self.ApplyBestNodeMethod()
        self.sol = Solution()
        self.ObjectiveFunction(self.sol)
        return self.sol
    
    
    def ApplyBestNodeMethod(self):
        
        for r in range(5):
            
            total_route_time = 0
            total_route_profit = 0
            node = 0
            self.route = Route(150)
            self.route.sequenceOfNodes.append(self.allNodes[0])
            self.allNodes[0].isRouted = True
            total_time = 0
            position = 0
            
            while total_route_time <= 150:
                max1 = -10000000
                flag = False
                
                for i in range(len(self.allNodes)):
                    if self.allNodes[i].isRouted == False:
                        flag = True
                        if (self.allNodes[i].profit - (self.distanceMatrix[node][i] +  self.allNodes[i].service_time)) > max1:
                            max1 = self.allNodes[i].profit - (self.distanceMatrix[node][i] +  self.allNodes[i].service_time)
                            position = i
                
                if not flag:
                    break
                elif (total_route_time + (self.distanceMatrix[node][position] +  self.allNodes[position].service_time) <= 150):
                    self.route.sequenceOfNodes.append(self.allNodes[position])
                    self.allNodes[position].isRouted = True
                    a = self.allNodes[position]
                    
                    total_route_time += (self.distanceMatrix[node][position] +  self.allNodes[position].service_time)
                    total_route_profit += self.allNodes[position].profit
                    node = position
                else:
                    break 
                    
                self.route.time_limit = 150 - total_route_time
                self.route.time = total_route_time
                self.route.profit = total_route_profit
                self.sol.routes.append(self.route)
                self.sol.profit += total_route_profit
                  
                          
            
    ## method that calculates the total profit of the solution given (total revenue - total cost of routed nodes)
    def ObjectiveFunction(self, solution):
        total_profit = 0
        single_profit = []
        for i in range(len(solution.routes)):
            time = 0
            rt = solution.routes[i]
            for j in range (0, len(rt.sequenceOfNodes)):
                print(rt.sequenceOfNodes[j].ID, end=' ')
            print(rt.profit)    
            for j in range(len(rt.sequenceOfNodes) - 1):
                index1 = rt.sequenceOfNodes[j]
                index2 = rt.sequenceOfNodes[j + 1]
                profit += (self.allNodes[index2.ID].profit - (self.allNodes[index2.ID].service_time + self.distanceMatrix[index1.ID][index2.ID]))
            single_profit.append(profit)
            self.sol.routes[i].profit = profit
            total_profit += profit
        print(total_profit)  
            
            
        