from z3 import *

# Define a first-order logic formula
x = Int('x')
y = Int('y')
formula = ForAll(x, Exists(y, x + y > 0))

# Create a Z3 solver
solver = Solver()

# Add the formula to the solver
solver.add(formula)

# Check if the formula is satisfiable
if solver.check() == sat:
    print("The formula is satisfiable")
else:
    print("The formula is not satisfiable")
