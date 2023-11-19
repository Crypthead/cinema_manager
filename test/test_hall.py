import unittest
from datetime import timedelta

from src.hall import Hall
from src.movie import Movie
from src.utils import today


class HallTest(unittest.TestCase):

    def test_plan_movie(self):
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))
        first_start_time = today() + timedelta(days=1)

        hall = Hall(0, 100)
        screening_id = hall.plan_screening(movie, first_start_time)
        self.assertIn(screening_id, hall.screenings)

    def test_book_tickets(self):
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))
        number_reservations = 10

        hall = Hall(0, 100)
        screening_id = hall.plan_screening(movie, today())
        hall.book_tickets(screening_id, number_reservations)

        self.assertEqual(hall.screenings[screening_id].reservations, number_reservations)

    def test_cancel_screening(self):
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))

        hall = Hall(0, 100)
        screening_id = hall.plan_screening(movie, today())
        hall.cancel_screening(screening_id)

        self.assertNotIn(screening_id, hall.screenings)

    def test_upcoming_screenings(self):
        movie = Movie("Test Movie1", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))

        hall = Hall(0, 100)
        hall.plan_screening(movie, today() + timedelta(days=1))
        hall.plan_screening(movie, today() + timedelta(days=2))
        hall.plan_screening(movie, today() + timedelta(days=3))

        self.assertEqual(len(hall.get_upcoming_screenings()), 3)


if __name__ == '__main__':
    unittest.main()
