from Tank import Tank

class Thruster:
    def __init__(self, name, max_thrust, Isp, tank):
        assert isinstance(max_thrust, (float,int))
        assert isinstance(Isp, (float,int))
        assert isinstance(tank, Tank)

        self.G0 = 9,80665

        self.name = name
        self.Isp = Isp
        self.max_mass_flow = (max_thrust / G0 * Isp)
        self.throttle = 0
        self.mass_flow = self.max_mass_flow * self.throttle
        self.tank = tank

    def set_throttle(self, value):
        assert value > 0 and value < 1

        self.throttle = throttle
        self.mass_flow = self.max_mass_flow * self.throttle

    def get_thrust(self):
        return self.thrust

    def fire(self,time):
        boost = self.thrust * time
        self.tank.extract(self.mass_flow, time)
        return boost

    def shutdown(self):
        self.throttle = 0

