from gso.glowworm import Glowworm
from gso.grid import Grid
from gso.movement import Movement
from gso.neighborhood import Neighborhood

__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'


def run():
    grid = Grid()
    grid.create()
    grid.fill_random_position()
    grid.show()

    glowworms = []
    for index, glowworm_location in enumerate(grid.get_glowworms()):
        glowworm = Glowworm(location=glowworm_location, name=index)
        glowworms.append(glowworm)

    for i in range(2):

        for glowworm in glowworms:
            glowworm.update_luciferin()

            x, y = glowworm.get_location()

            grid.update_cell_value(x=x, y=y, luciferin=glowworm.get_luciferin())

            print(f"Glowworms: {glowworm.get_name()}, luciferin: {glowworm.get_luciferin()}")
            neighbors = grid.has_neighbour(x=x, y=y)

            if len(neighbors) > 0:
                print(f"Neighbors: {neighbors}")
                move = Movement(luciferin_i=glowworm.get_luciferin(), neighbors=neighbors)
                probability = move.probability()

                if probability:
                    print(f"probability: {probability[0]} x: {probability[1]} y: {probability[2]}")

                    new_x, new_y = move.move(from_x=x, from_y=y, to_x=probability[1], to_y=probability[2])
                    glowworm.update_location(x=new_x, y=new_y,)
                    grid.update_cell_value(x=x, y=y, luciferin=0)
                    grid.show()
                    print(f"Update Glowworms: {glowworm.get_name()},"
                          f" luciferin: {glowworm.get_luciferin()}, location: {glowworm.get_location()}")

                    neighbourhood_range = Neighborhood(number_of_neighbors=len(neighbors))
                    value_of_neighbourhood_range = neighbourhood_range.update()
                    glowworm.update_field_of_view_range(value_of_neighbourhood_range)

                    print(f"Update field of view range:  {value_of_neighbourhood_range}\n")
            else:
                print("There are not neighbors in its field of view\n")


if __name__ == '__main__':
    run()
