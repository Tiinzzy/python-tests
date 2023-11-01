import unittest
from model.movies.movies_dao import MoviesDao


class TestMovieDao(unittest.TestCase):

    def test_save_to_table(self):
        movie = MoviesDao("Test Movie", "2023-11-01","7")
        movie.save_to_table()

        self.assertTrue(movie.get_oid() > 0)
        self.assertEqual(movie.get_title(), "Test Movie")
        self.assertEqual(movie.get_release_date(), "2023-11-01")
        self.assertEqual(movie.get_rating(), "7")


    def test_load_all(self):
        movies = MoviesDao.load_all()
        print(movies)
        self.assertTrue(len(movies) > 0)
    #
    def test_add_and_delete(self):
        movie = MoviesDao("Test Movie2", "2023-11-20","10")
        movie.save_to_table()

        self.assertTrue(movie.get_oid() > 0)
        self.assertEqual(movie.get_title(), "Test Movie2")
        self.assertEqual(movie.get_release_date(), "2023-11-20")
        self.assertEqual(movie.get_rating(), "10")

        new_oid = movie.get_oid()
        result = movie.delete(new_oid)
        self.assertEqual(result, None)


    def test_update(self):
        movie = MoviesDao(oid=98)
        movie.set_title("Test Movie2")
        movie.set_rating("10")
        movie.set_release_date("2023-11-20")
        movie.save_to_table()

        self.assertEqual(movie.get_title(), "Test Movie2")
        self.assertEqual(movie.get_release_date(), "2023-11-20")
        self.assertEqual(movie.get_rating(), "10")