from gso.objective_function import J1

__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'


class Glowworm(object):
    """
        This class create a glowworm and keep its data such as: location, luciferin and neighbourhood range
    """

    def __init__(self, location={}, luciferin=0, field_of_view=1, name="unknow"):
        self.location = location
        self.luciferin = luciferin
        self.field_of_view = field_of_view
        self.name = name

    def get_location(self):
        return self.location['x'], self.location['y']

    def get_luciferin(self):
        return self.luciferin

    def get_name(self):
        return self.name

    def update_luciferin(self):
        rho = 0.4
        gamma = 0.6
        x = self.location['x']
        y = self.location['y']
        self.luciferin = ((1-rho) * self.luciferin) + (gamma * J1.j1(x, y))

    def update_location(self, x, y):
        self.location['x'] = x
        self.location['y'] = y

    def get_field_of_view_range(self):
        return self.field_of_view

    def update_field_of_view_range(self, field_of_view):
        self.field_of_view = field_of_view
