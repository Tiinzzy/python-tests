import unittest
from bidirect_linkedlist.bidirectional_linkedlist import BidirectionalLinkelist


class BidirectionalLinkedListTests(unittest.TestCase):

    def test_check_begining(self):
        bll = BidirectionalLinkelist()

        self.assertIsNone(bll.head)
        self.assertIsNone(bll.tail)
        self.assertEqual(bll.size, 0)

    def test_add_single_element(self):
        bll = BidirectionalLinkelist()

        self.assertTrue(bll.add(1))
        self.assertEqual(bll.get_head(), 1)
        self.assertEqual(bll.get_tail(), 1)
        self.assertEqual(bll.size, 1)

    def test_add_multiple_elements(self):
        bll = BidirectionalLinkelist()

        self.assertTrue(bll.add(1))
        self.assertTrue(bll.add(2))
        self.assertTrue(bll.add(3))
        self.assertTrue(bll.add(4))
        self.assertTrue(bll.add(5))
        self.assertEqual(bll.get_head(), 1)
        self.assertEqual(bll.get_tail(), 5)
        self.assertEqual(bll.size, 5)

    def test_add_element_at_specific_index(self):
        bll = BidirectionalLinkelist()

        self.assertTrue(bll.add(1))
        self.assertTrue(bll.add(2))
        self.assertTrue(bll.add(3))
        self.assertTrue(bll.add(10, index=1))
        self.assertEqual(bll.get_head(), 1)
        self.assertEqual(bll.get_tail(), 3)
        self.assertEqual(bll.size, 4)
        self.assertEqual(bll.get_element(1), 10)

    def test_add_element_wrong_index(self):
        bll = BidirectionalLinkelist()

        self.assertTrue(bll.add(1, index=1))
        self.assertFalse(bll.add(1, index=-1))
        self.assertFalse(bll.add(1, index=5))

    def test_remove_single_element(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        self.assertEqual(bll.remove(), 1)
        self.assertIsNone(bll.head)
        self.assertIsNone(bll.tail)
        self.assertEqual(bll.size, 0)

    def test_remove_element_at_specific_index(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        bll.add(2)
        bll.add(3)
        self.assertEqual(bll.remove(index=1), 2)
        self.assertEqual(bll.get_head(), 1)
        self.assertEqual(bll.get_tail(), 3)
        self.assertEqual(bll.size, 2)

    def test_remove_element_from_head(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        bll.add(2)
        bll.add(3)
        self.assertEqual(bll.remove(index=0), 1)
        self.assertEqual(bll.get_head(), 2)
        self.assertEqual(bll.get_tail(), 3)
        self.assertEqual(bll.size, 2)

    def test_remove_element_from_tail(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        bll.add(2)
        bll.add(3)
        self.assertEqual(bll.remove(), 3)
        self.assertEqual(bll.get_head(), 1)
        self.assertEqual(bll.get_tail(), 2)
        self.assertEqual(bll.size, 2)

    def test_remove_element_at_wrong_index(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        bll.add(2)
        bll.add(3)
        self.assertIsNone(bll.remove(index=-1))
        self.assertIsNone(bll.remove(index=6))

    def test_show_all(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        bll.add(2)
        bll.add(3)
        bll.add(4)
        bll.add(5)
        bll.add(6)
        output = bll.show_all()
        self.assertEqual(bll.show_all(), output)

    def test_show_all_reverse(self):
        bll = BidirectionalLinkelist()

        bll.add(1)
        bll.add(2)
        bll.add(3)
        bll.add(4)
        bll.add(5)
        bll.add(6)
        output = bll.show_all(reverse=True)
        self.assertEqual(bll.show_all(
            reverse=True), output)

    def test_get_element(self):
        bll = BidirectionalLinkelist()

        bll.add(10)
        bll.add(20)
        bll.add(30)
        self.assertEqual(bll.get_element(0), 10)
        self.assertEqual(bll.get_element(1), 20)
        self.assertEqual(bll.get_element(2), 30)
        self.assertIsNone(bll.get_element(4))
        self.assertIsNone(bll.get_element(-1))

    def test_clear(self):
        bll = BidirectionalLinkelist()

        bll.add(10)
        bll.add(9)
        bll.add(8)
        bll.clear()
        self.assertIsNone(bll.head)
        self.assertIsNone(bll.tail)
        self.assertEqual(bll.size, 0)

    def test_find_first(self):
        bll = BidirectionalLinkelist()

        def my_search(e):
            return isinstance(e, dict) and e['name'] == 'Tina'

        bll.add(100)
        bll.add(200)
        bll.add(300)
        bll.add({'a': 1, 'name': 'Tina'})
        self.assertEqual(bll.find_first(
            my_search), {'a': 1, 'name': 'Tina'})
        self.assertEqual(bll.find_first(lambda x: isinstance(
            x, dict) and x['name'] == 'Tina'),  {'a': 1, 'name': 'Tina'})

