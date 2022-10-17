import unittest
from average import average_scores

class MyTestCase(unittest.TestCase):
    def test_average(self):
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    # test com a média de 5 elementos
    def test_average_five(self):
        self.scores_dict = {"Test 1": 45, "Test 2": 87, "Test 3": 67, "Test 4": 76, "Test 5": 57}
        expected = 66.4
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    # teste se o dicionário está vazio
    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}
        # Assert
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)

    # teste se a entrada não é um dicionário
    def test_average_zero(self):
        # Arrange
        self.list = list()
        # Assert
        with self.assertRaises(TypeError):
            average_scores(self.list)