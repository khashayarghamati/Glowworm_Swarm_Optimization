__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'


class Movement(object):
    """
        select a neighbour, identify orientation between two points and move worm to new position
    """

    def __init__(self, luciferin_i, neighbors):
        self.neighbors = neighbors
        self.luciferin_i = luciferin_i
        self.probabilities_meta = []

    def probability(self):
        total_sum = 0.0
        self.probabilities_meta = []

        for neighbor in self.neighbors:
            difference = float(neighbor['l']) - self.luciferin_i
            self.probabilities_meta.append({
                'value': difference,
                'x': neighbor['x'],
                'y': neighbor['y']
            })
            total_sum += difference

        for i in range(len(self.neighbors)):
            self.probabilities_meta[i]['value'] /= total_sum

        if len(self.probabilities_meta) > 0:
            return max(
                [(item['value'], item['x'], item['y']) for item in self.probabilities_meta]
            )
        return None

    def move(self, from_x, from_y, to_x, to_y, step_size=1):

        if to_x < from_x and to_y < from_y:
            return from_x - step_size, from_y - step_size

        elif to_x == from_x and to_y < from_y:
            return from_x, from_y - step_size

        elif to_x == from_x and to_y > from_y:
            return from_x, from_y + step_size

        elif to_x > from_x and from_y == to_y:
            return from_x + step_size, from_y

        elif to_x > from_x and to_y > from_y:
                return from_x + step_size, from_y + step_size

        elif to_x > from_x and to_y < from_y:
                return from_x + step_size, from_y - step_size

        elif to_x < from_x and to_y == from_y:
                return from_x - step_size, from_y

        elif to_x < from_x and to_y > from_y:
                return from_x - step_size, from_y + step_size
