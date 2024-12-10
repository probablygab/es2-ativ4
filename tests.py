# Aula Prática 4 - Engenharia de Software II
# Gabriel Pains de Oliveira Cardoso - 2021096887


import unittest
from quadratic_solver import solve_quadratic


class TestQuadraticSolver(unittest.TestCase):

    def test_two_real_roots(self):
        a, b, c = 1, -3, 2
        result = solve_quadratic(a, b, c)
        self.assertEqual(result, (2.0, 1.0))

    def test_one_real_root(self):
        a, b, c = 1, -2, 1
        result = solve_quadratic(a, b, c)
        self.assertEqual(result, (1.0, 1.0))

    def test_no_real_roots(self):
        a, b, c = 1, 2, 5
        with self.assertRaises(ValueError):
            solve_quadratic(a, b, c)

    def test_large_coefficients(self):
        a, b, c = 10000000000, -50000000000, 6000
        result = solve_quadratic(a, b, c)
        self.assertAlmostEqual(result[0], 4.999, places=2)
        self.assertAlmostEqual(result[1], 1.200e-7, places=2)

    def test_negative_a(self):
        a, b, c = -1, 2, 3
        result = solve_quadratic(a, b, c)
        self.assertEqual(result, (-1.0, 3.0))


if __name__ == "__main__":
    unittest.main()
