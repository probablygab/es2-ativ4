# Aula Prática 4 - Engenharia de Software II
# Gabriel Pains de Oliveira Cardoso - 2021096887


import math


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Raises an error if the discriminant (b^2 - 4ac) is negative.
    """

    discriminant: float = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("Negative discriminant, no real roots.")

    root1: float = (-b + math.sqrt(discriminant)) / (2 * a)
    root2: float = (-b - math.sqrt(discriminant)) / (2 * a)

    return root1, root2
