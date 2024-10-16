from propositional_logic import *

# Définir les propositions
A = Proposition("Des immeubles sont présents")
B = Proposition("Des voitures sont présentes")
C = Proposition("Des piétons sont présents")
D = Proposition("Des feux de circulation sont visibles")

# Définir les règles
ville = Or(Or(And(A, B), And(A, C)), And(A, D))

# Définir les valeurs des propositions
A.value = True
B.value = True
C.value = False
D.value = False

# Évaluer la valeur de la proposition "ville"
print(ville.evaluate())  # Sortie: True
