from z3 import *

# Créer un solver
solver = Solver()

# Définir une sorte pour les images
Image = DeclareSort('Image')

# Définir des fonctions pour vérifier le contenu d'une image
ContientEau = Function('ContientEau', Image, BoolSort())
ContientSable = Function('ContientSable', Image, BoolSort())
ContientBateaux = Function('ContientBateaux', Image, BoolSort())
ContientOiseauxMarins = Function('ContientOiseauxMarins', Image, BoolSort())

# Définir des relations pour les types d'images
EstMer = Function('EstMer', Image, BoolSort())
EstPort = Function('EstPort', Image, BoolSort())
EstPlage = Function('EstPlage', Image, BoolSort())

# Règles
# 1. Si une image contient de l'eau et du sable, alors c'est une mer
x = Const('x', Image)
solver.add(Implies(And(ContientEau(x), ContientSable(x)), EstMer(x)))

# 2. Si une image contient des bateaux, alors c'est un port
solver.add(Implies(ContientBateaux(x), EstPort(x)))

# 3. Si une image contient des oiseaux marins, alors c'est une plage
solver.add(Implies(ContientOiseauxMarins(x), EstPlage(x)))

# 4. Il existe au moins une image qui contient de l'eau et du sable
solver.add(Exists([x], And(ContientEau(x), ContientSable(x))))

# Exemple d'images à vérifier
img1 = Const('img1', Image)
img2 = Const('img2', Image)

# Définir des contenus pour img1 et img2
solver.add(ContientEau(img1) == True)
solver.add(ContientSable(img1) == True)
solver.add(ContientBateaux(img1) == False)
solver.add(ContientOiseauxMarins(img1) == False)

solver.add(ContientEau(img2) == False)
solver.add(ContientSable(img2) == True)
solver.add(ContientBateaux(img2) == True)
solver.add(ContientOiseauxMarins(img2) == True)

# Vérifier si les images respectent les règles
if solver.check() == sat:
    print("Les images respectent les règles définies.")
else:
    print("Les images ne respectent pas les règles définies.")

# Afficher les modèles (si satisfaisables)
print(solver.model())

