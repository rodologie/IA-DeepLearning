from z3 import *

x = Int('x')
y = Int('y')

constraint1 = x + y > 5
constraint2 = x - y < 3

solver = Solver()
solver.add(constraint1)
solver.add(constraint2)

if solver.check() == sat:
    print("Les contraintes sont satisfiables")
    print(solver.model())
else:
    print("Les contraintes ne sont pas satisfiables")

