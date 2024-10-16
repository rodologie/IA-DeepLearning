from propositional_logic import *

# Définir les propositions
A = Proposition("L'utilisateur aime l'image actuelle")
B = Proposition("L'image actuelle est un portrait")
C = Proposition("L'image actuelle est une œuvre abstraite")
D = Proposition("L'utilisateur a aimé une œuvre similaire par le passé")
E = Proposition("L'image est en noir et blanc")
F = Proposition("L'image est en couleur")
G = Proposition("L'utilisateur préfère les œuvres d'art réalistes")
H = Proposition("L'image est une peinture réaliste")
I = Proposition("L'utilisateur a aimé les œuvres de cet artiste dans le passé")
J = Proposition("L'utilisateur n'aime pas les images très saturées")
K = Proposition("L'image a une saturation élevée")

# Définir les règles de recommandation
# 1. Si l'utilisateur aime l'image actuelle et qu'il a aimé une œuvre similaire par le passé,
# alors il aimera probablement des œuvres du même style à l'avenir.
recommandation_style_futur = Implication(And(A, D), A)

# 2. Si l'image est soit un portrait soit une œuvre abstraite (mais pas les deux),
# et que l'utilisateur a une préférence pour les œuvres réalistes, alors il n'aimera pas l'image actuelle.
recommandation_abstrait_ou_portrait = Implication(Xor(B, C), Not(G))

# 3. Si l'image est en couleur et que l'utilisateur aime les œuvres de cet artiste,
# alors l'utilisateur aimera cette image si et seulement si elle est une peinture réaliste (équivalence).
recommandation_realiste_couleur = Equivalence(And(F, I), H)

# 4. Si l'utilisateur n'aime pas les images très saturées, alors il n'aimera pas une image avec
# une saturation élevée (implication inverse).
recommandation_non_sature = Implication(J, Not(K))

# 5. Si l'image actuelle est une peinture réaliste et que l'utilisateur a déjà aimé une œuvre similaire,
# alors il aimera l'image actuelle (implication directe).
recommandation_peinture_realiste = Implication(And(H, D), A)

# 6. Si l'utilisateur préfère les œuvres réalistes ou a aimé des œuvres similaires dans le passé,
# alors il n'aimera pas une œuvre abstraite (implication avec OU logique).
recommandation_non_abstrait = Implication(Or(G, D), Not(C))

# 7. Si l'image actuelle est soit en noir et blanc soit un portrait,
# et que l'utilisateur a aimé cet artiste dans le passé, alors il aimera l'image actuelle (XOR logique).
recommandation_noir_et_blanc_ou_portrait = Implication(Xor(E, B), I)

# 8. Si l'utilisateur n'aime pas les images abstraites et qu'il aime les œuvres de cet artiste,
# alors il aimera probablement les portraits du même artiste.
recommandation_portrait_artiste = Implication(And(Not(C), I), B)

B.value = True
G.value = True
D.value = False
C.value = False
print(recommandation_non_abstrait.evaluate())
print(recommandation_abstrait_ou_portrait.evaluate())
