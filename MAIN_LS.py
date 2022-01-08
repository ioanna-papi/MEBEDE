from LOCAL_SEARCH import *

# 1ο Ερώτημα
m = Model()
m.BuildModel()

# 2ο Ερώτημα
s = Solver(m)
solution = s.ApplyBestNodeMethod()
print(" TOTAL PROFIT =", s.objective(solution))

# 3ο και 4ο ερώτημα
print("VND")
solution3 = s.VND()
print(s.objective(solution3))
