from propositional_logic import *

# Create propositions
p = Proposition("p")
q = Proposition("q")
r = Proposition("r")

# Create compound propositions
not_p = Not(p)
p_and_q = And(p, q)
q_or_r = Or(q, r)
p_implies_q = Implication(p, q)
p_iff_q = Equivalence(p, q)

# Evaluate propositions
p.value = True
q.value = True
r.value = False

print(not_p.evaluate())  # Output: False
print(p_and_q.evaluate())  # Output: True
print(q_or_r.evaluate())  # Output: True
print(p_implies_q.evaluate())  # Output: True
print(p_iff_q.evaluate())  # Output: True

# Test with true and false propositions
true_prop = TrueProposition()
false_prop = FalseProposition()

print(true_prop.evaluate())  # Output: True
print(false_prop.evaluate())  # Output: False
print(Implication(true_prop, false_prop).evaluate())  # Output: False
print(Implication(false_prop, true_prop).evaluate())  # Output: True
print(Implication(true_prop, true_prop).evaluate())  # Output: True
print(Implication(false_prop, false_prop).evaluate())  # Output: True
