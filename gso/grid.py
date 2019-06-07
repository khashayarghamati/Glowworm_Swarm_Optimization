import matplotlib.pyplot as plt
import numpy as np

__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'


class Grid(object):
    """
        Create a grid and put worms randomly to it
    """
    def __init__(self):
        self.grid = None
        self.glowworms_locations = []

    def create(self, x=10, y=10):
        self.grid = np.random.binomial(0, 0, size=(x, y))
        return self.grid

    def fill_random_position(self, number_of_glowworms=40, y=10):
        for row in range(number_of_glowworms):
            indices = np.random.randint(0, high=y-1, size=2)
            i = indices[0]
            j = indices[1]

            self.glowworms_locations.append({
                'x': i,
                'y': j,
            })

            self.grid[i, j] = 1

    def show(self):
        a = np.ma.masked_where(self.grid < 0.0, self.grid)
        cmap = plt.cm.OrRd
        cmap.set_bad(color='black')
        plt.imshow(a, interpolation='none', cmap=cmap)
        plt.show()

    def has_neighbour(self, x, y, field_of_view=1):
        neighbours = []
        print(f"CELL: ({x}, {y})")

        if x - field_of_view > -1:
            self.check_is_occupied(neighbours, x - field_of_view, y)

        if x + field_of_view < 10:
            self.check_is_occupied(neighbours, x + field_of_view, y)

        if y - field_of_view > -1:
            self.check_is_occupied(neighbours, x, y - field_of_view)

        if y + field_of_view < 10:
            self.check_is_occupied(neighbours, x, y + field_of_view)

        if x - field_of_view > -1 and y - field_of_view > -1:
            self.check_is_occupied(neighbours, x - field_of_view, y - field_of_view)

        if x - field_of_view > -1 and y + field_of_view < 10:
            self.check_is_occupied(neighbours, x - field_of_view, y + field_of_view)

        if y - field_of_view > -1 and x + field_of_view < 10:
            self.check_is_occupied(neighbours, x + field_of_view, y - field_of_view)

        if y + field_of_view < 10 and x + field_of_view < 10:
            self.check_is_occupied(neighbours, x + field_of_view, y + field_of_view)

        return neighbours

    def check_is_occupied(self, neighbours, x, y):
        if self.grid[x, y] > 0:
            neighbours.append({
                'x': x,
                'y': y,
                'l': self.grid[x, y]
            })

    def get_glowworms(self):
        return self.glowworms_locations

    def update_cell_value(self, x, y, luciferin):
        self.grid[x, y] = luciferin
