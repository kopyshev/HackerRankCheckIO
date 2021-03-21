from math import hypot
from typing import List, Tuple
Coords = List[Tuple[int, int]]

def triangle_sides(coords: Coords) -> list:

    a = hypot(coords[0][0]-coords[1][0], coords[0][1] - coords[1][1])
    b = hypot(coords[1][0]-coords[2][0], coords[1][1] - coords[2][1])
    c = hypot(coords[0][0]-coords[2][0], coords[0][1] - coords[2][1])
    return sorted([a,b,c]) 

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    return len(set([x/y for x,y in zip(triangle_sides(coords_1), triangle_sides(coords_2))])) == 1

if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
