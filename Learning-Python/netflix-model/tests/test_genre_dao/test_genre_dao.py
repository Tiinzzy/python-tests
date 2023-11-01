import unittest
from model.genre.genre_dao import GenreDao


class TestGenreDao(unittest.TestCase):

    def test_save_to_table(self):
        gnr = GenreDao(description="Test Genre")
        gnr.save_to_table()

        self.assertTrue(gnr.get_oid() > 0)
        self.assertEqual(gnr.get_description(), "Test Genre")


    def test_load_all(self):
        gnr = GenreDao.load_all()
        print(gnr)
        self.assertTrue(len(gnr) > 0)
    #
    def test_add_and_delete(self):
        gnr = GenreDao()
        gnr.set_description("Test1")
        gnr.save_to_table()
        self.assertEqual(gnr.get_description(), "Test1")

        new_oid = gnr.get_oid()
        result = gnr.delete_genre(new_oid)
        self.assertEqual(result, None)


    def test_update(self):
        gnr = GenreDao(oid=56)
        gnr.set_description("Musical")
        gnr.save_to_table()
        self.assertEqual(gnr.get_description(), "Musical")
