import unittest
from datetime import timedelta

from src.movie import Movie
from src.utils import today


class TestMovie(unittest.TestCase):
    def test_prices(self):
        movie = Movie("Title", ["Genre"], 5.0, 10.0, today() + timedelta(days=8))
        self.assertEqual(movie.get_ticket_price(False), 10.0)
        self.assertEqual(movie.get_ticket_price(True), 12.0)

    def test_number_of_breaks(self):
        movie = Movie("Title", ["Thriller"], 180.0, 10.0, today())
        self.assertEqual(movie.get_number_of_breaks(), 0)

    def test_break_time(self):
        movie = Movie("Title", ["Comedy"], 100.0, 10.0, today())
        self.assertListEqual(movie.get_break_times(), [50.0])


if __name__ == '__main__':
    unittest.main()
