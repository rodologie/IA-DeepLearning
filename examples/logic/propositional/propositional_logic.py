class Proposition:
    def __init__(self, name):
        self.name = name
        self.value = None

    def evaluate(self):
        return self.value


class Not(Proposition):
    def __init__(self, proposition):
        super().__init__("NOT " + proposition.name)
        self.proposition = proposition

    def evaluate(self):
        return not self.proposition.evaluate()


class And(Proposition):
    def __init__(self, proposition1, proposition2):
        super().__init__(f"{proposition1.name} AND {proposition2.name}")
        self.proposition1 = proposition1
        self.proposition2 = proposition2

    def evaluate(self):
        return self.proposition1.evaluate() and self.proposition2.evaluate()


class Or(Proposition):
    def __init__(self, proposition1, proposition2):
        super().__init__(f"{proposition1.name} OR {proposition2.name}")
        self.proposition1 = proposition1
        self.proposition2 = proposition2

    def evaluate(self):
        return self.proposition1.evaluate() or self.proposition2.evaluate()


class Implication(Proposition):
    def __init__(self, proposition1, proposition2):
        super().__init__(f"{proposition1.name} IMPLIES {proposition2.name}")
        self.proposition1 = proposition1
        self.proposition2 = proposition2

    def evaluate(self):
        return not self.proposition1.evaluate() or self.proposition2.evaluate()


class Equivalence(Proposition):
    def __init__(self, proposition1, proposition2):
        super().__init__(f"{proposition1.name} IFF {proposition2.name}")
        self.proposition1 = proposition1
        self.proposition2 = proposition2

    def evaluate(self):
        return self.proposition1.evaluate() == self.proposition2.evaluate()


class Biconditional(Proposition):
    def __init__(self, proposition1, proposition2):
        super().__init__(f"{proposition1.name} IFF {proposition2.name}")
        self.proposition1 = proposition1
        self.proposition2 = proposition2

    def evaluate(self):
        return self.proposition1.evaluate() == self.proposition2.evaluate()


class Xor(Proposition):
    def __init__(self, proposition1, proposition2):
        super().__init__(f"{proposition1.name} XOR {proposition2.name}")
        self.proposition1 = proposition1
        self.proposition2 = proposition2

    def evaluate(self):
        return self.proposition1.evaluate() != self.proposition2.evaluate()


class Tautology(Proposition):
    def __init__(self):
        super().__init__("TAUTOLOGY")
        self.value = True

    def evaluate(self):
        return self.value


class Contradiction(Proposition):
    def __init__(self):
        super().__init__("CONTRADICTION")
        self.value = False

    def evaluate(self):
        return self.value


class TrueProposition(Proposition):
    def __init__(self):
        super().__init__("TRUE")
        self.value = True


class FalseProposition(Proposition):
    def __init__(self):
        super().__init__("FALSE")
        self.value = False
