import unittest

from lesson23._unittest.project_1.code.my_calculations import Calculations


class TestCalculations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, 'Сумма посчитана неправильно.')

    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(), 6, 'Разность посчитана неправильно.')

    def test_product(self):
        self.assertEqual(self.calculation.get_product(), 16, 'Умножение посчитано неправильно.')

    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, 'Деление посчитано неправильно.')


if __name__ == '__main__':
    unittest.main()
