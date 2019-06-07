__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'


class Neighborhood(object):
    """
    for every worm in an iteration algorithm changes neighbourhood range
    """
    def __init__(self, max_field_of_view=1, field_of_view=1, max_neighbors=1, number_of_neighbors=1):
        self.max_field_of_view = max_field_of_view
        self.field_of_view = field_of_view
        self.max_neighbors = max_neighbors
        self.number_of_neighbors = number_of_neighbors

    def update(self):
        return min(
            self.max_field_of_view,
            max(0, (self.field_of_view + 0.08 * (self.max_neighbors - self.number_of_neighbors)))
        )
