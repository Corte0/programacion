class Tank:
    def __init__(self, name, mass, preassure):
        assert isinstance(mass, (float, int))
        assert isinstance(preassure, (float,int))

        self.name = name
        self.INIT_MASS = mass
        self.INIT_PREASSURE = preassure
        self.mass = mass
        self._preassure = preassure

    def extract(self, mass_flow, time):
        assert isinstance(mass_flow,(float,int))
        assert isinstance(time,(float,int))

        mass = mass_flow * time

        if self.mass > mass:
            self.mass -= mass
            self._preassure = self.INIT_PREASSURE * (self.mass / self.INIT_MASS)
            return mass
        else:
            return None

    def getMass(self):
        return self.mass

    def getInitMass(self):
        return self.INIT_MASS

    def getPreassure(self):
        return self._preassure

    def getInitPreassure(self):
        return self.INIT_PREASSURE
