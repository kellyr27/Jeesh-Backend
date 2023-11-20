from django.test import TestCase
from play.core.stars import generate_star_coordinates

class GenerateStarCoordinatesTest(TestCase):
    def test_generate_star_coordinates(self):

        # Call the function
        result = generate_star_coordinates()

        for coordinate in result:
            self.assertIsInstance(coordinate, tuple)
            self.assertEqual(len(coordinate), 3)
            self.assertIsInstance(coordinate[0], int)
            self.assertIsInstance(coordinate[1], int)
            self.assertIsInstance(coordinate[2], int)
            self.assertGreater(coordinate[0], 0)
            self.assertGreater(coordinate[1], 0)
            self.assertGreater(coordinate[2], 0)
            self.assertLessEqual(coordinate[0], 10)
            self.assertLessEqual(coordinate[1], 10)
            self.assertLessEqual(coordinate[2], 10)

        self.assertGreater(len(result), 0)
        self.assertLessEqual(len(result), 81)