import unittest
from hash_map.hashmap import HashMap


class HashmapTests(unittest.TestCase):

    def test_check_begining(self):
        hashed_map = HashMap()

        self.assertTrue(bool(hashed_map))

    def test_insert_and_get(self):
        hashed_map = HashMap()

        hashed_map.insert('Tina', {1, 2, 3})
        hashed_map.insert('Tania', {4, 5, 6})
        hashed_map.insert('None', None)

        hashed_map.insert('Kiana', {4, 5, 6})
        hashed_map.insert('Kamran', {1, 2, 3})
        hashed_map.insert('Kevin', {1, 2})

        self.assertEqual(hashed_map.get('Tina'), {'key': 'Tina', 'value': {1, 2, 3}})
        self.assertEqual(hashed_map.get('Kiana'), {'key': 'Kiana', 'value': {4, 5, 6}})

    def test_remove(self):
        hashed_map = HashMap()

        hashed_map.insert('Tina', {10, 20})
        hashed_map.insert('Kiana', {30, 40})
        hashed_map.insert('Kamran', {50, 60})

        self.assertTrue(hashed_map.remove('Kiana'))
        self.assertIsNone(hashed_map.get('Kiana'))

        self.assertFalse(hashed_map.remove('Kevin'))

    def test_show_all(self):
        hashed_map = HashMap()

        hashed_map.insert('Tina', {10, 20})
        hashed_map.insert('Kiana', {30, 40})
        hashed_map.insert('Kamran', {50, 60})

        expected_result = hashed_map.show_all()
        self.assertEqual(hashed_map.show_all(), expected_result)
