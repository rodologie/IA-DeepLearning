from propositional_logic import *

# Define propositions
P = Proposition("L'eau est présente")
Q = Proposition("Il y a du sable")
R = Proposition("Des oiseaux marins sont présents")
S = Proposition("Des bateaux sont visibles")

# Define compound propositions
rule1 = And(P, Q)
rule2 = And(P, R)
rule3 = And(P, S)

# Define the main proposition
image_de_la_mer = Or(Or(rule1, rule2), rule3)

# évaluer des propositions
P.value = True
Q.value = True
R.value = False
S.value = False
print(image_de_la_mer.evaluate())  # Sortie: True
