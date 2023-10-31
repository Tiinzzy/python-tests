import unittest

import os
import sys

project_root = os.path.dirname(os.path.realpath("__file__"))
project_root = project_root.replace("/tests/test_genre_dao", "/model/genre")
sys.path.append(project_root)

import genre_dao


class TestGenreDao(unittest.TestCase):

    def test_save_to_table(self):
        gnr = genre_dao.GenreDao(description="Test Genre")
        gnr.save_to_table()

        self.assertTrue(gnr.get_oid() > 0)
        self.assertEqual(gnr.get_description(), "Test Genre")
