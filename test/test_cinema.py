import unittest

from src.cinema import Cinema


class CinemaTest(unittest.TestCase):

    def test_cinema_initialization(self):
        number_of_halls = 5

        cinema = Cinema(number_of_halls)
        self.assertEqual(cinema.get_number_of_halls(), number_of_halls)


    def test_expand_cinema(self):
        initial_number_of_halls = 5
        number_of_halls_to_add = 3

        cinema = Cinema(initial_number_of_halls)
        cinema.expand_cinema(number_of_halls_to_add)

        self.assertEqual(cinema.get_number_of_halls(), initial_number_of_halls + number_of_halls_to_add)

    def test_get_currently_playing_movies(self):
        cinema = Cinema(5)
        self.assertListEqual(cinema.get_currently_playing_movies(), [])


if __name__ == '__main__':
    unittest.main()
