def is_equilateral(sides):
    if check_triangle_ineq(sides):
        return len(set(sides)) == 1
    else:
        return False


def is_isosceles(sides):
    if check_triangle_ineq(sides):
        return (len(set(sides)) == 1) or (len(set(sides)) == 2)
    else:
        return False


def is_scalene(sides):
    if check_triangle_ineq(sides):
        return len(set(sides)) == 3
    else:
        return False

def check_triangle_ineq(sides):
    if any(side <= 0 for side in sides):
        return False
    else:
        return (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[0] + sides[2] > sides[1])
