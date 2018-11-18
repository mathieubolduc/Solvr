from CubeSolver import CubeRotation
from Cube import CubeColor, Cube

        

def rotateAlgo(algorithm, facing=CubeColor.RED):
    algo = []
    rotation = [CubeColor.RED, CubeColor.GREEN, CubeColor.ORANGE, CubeColor.BLUE]
    offset = rotation.index(facing)
    for move in algorithm:
        newSide = move.side
        if move.side in rotation:
            newSide = rotation[(rotation.index(move.side) + offset) % 4]
        algo.append(CubeRotation(newSide, move.angle))
    return algo

def flipAlgo(algorithm):
    algo = []
    for move in algorithm:
        newSide = move.side
        if move.side == CubeColor.BLUE:
            newSide = CubeColor.GREEN
        elif move.side == CubeColor.GREEN:
            newSide = CubeColor.BLUE
        algo.append(CubeRotation(newSide, -move.angle))
    return algo


# right hand side F2L
F2L         = [ CubeRotation(CubeColor.YELLOW, 90),
                CubeRotation(CubeColor.GREEN, 90),
                CubeRotation(CubeColor.YELLOW, -90),
                CubeRotation(CubeColor.GREEN, -90),
                CubeRotation(CubeColor.YELLOW, -90),
                CubeRotation(CubeColor.RED, -90),
                CubeRotation(CubeColor.YELLOW, 90),
                CubeRotation(CubeColor.RED, 90)
                ]

# right hand side edge orienter
OLL_EDGE    = [ CubeRotation(CubeColor.RED, -90),
                CubeRotation(CubeColor.YELLOW, -90),
                CubeRotation(CubeColor.BLUE, -90),
                CubeRotation(CubeColor.YELLOW, 90),
                CubeRotation(CubeColor.BLUE, 90),
                CubeRotation(CubeColor.RED, 90),
                ]