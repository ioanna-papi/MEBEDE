from VRP import *
from SOLVER import *

m = Model()
m.BuildModel()
s = Solver(m)
print("Nearest Neighbor")
solution = s.ApplyNearestNeighborMethod()
print(s.objective(solution))
print()
# print("Local Search")
# solution2 = s.LocalSearch()
# print(s.objective(solution2))
# print()
print("VND")
solution3 = s.VND()
print(s.objective(solution3))
