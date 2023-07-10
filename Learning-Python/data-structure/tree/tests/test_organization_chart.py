import unittest
from tree.organization_chart import OrganizationChart


class OrganizationChartTests(unittest.TestCase):

    def test_add_child_no_parent(self):
        org_chart = OrganizationChart()

        node = org_chart.add_child("CEO")

        self.assertEqual(node.name, "CEO")
        self.assertEqual(node.children, [])
        self.assertEqual(org_chart.root, node)

    def test_add_child_with_parent(self):
        org_chart = OrganizationChart()

        org_chart.add_child("CEO")
        parent = org_chart.root

        node = org_chart.add_child("Manager", parent)
        self.assertEqual(node.name, "Manager")
        self.assertEqual(node.children, [])
        self.assertIn(node, parent.children)

    def test_find_first_node(self):
        org_chart = OrganizationChart()

        org_chart.add_child("CEO")
        parent = org_chart.root
        child1 = org_chart.add_child("Manager", parent)
        mang_child = org_chart.add_child("Staff1", child1)
        node = org_chart.find_first_node("Manager")

        self.assertEqual(node.name, "Manager")
        self.assertEqual(node.children, [mang_child])
        self.assertEqual(node, child1)

    def test_show_org_chart(self):
        org_chart = OrganizationChart()

        ceo = org_chart.add_child('CEO')
        manager = org_chart.add_child('Manager', ceo)
        org_chart.add_child('Secretary', manager)
        staff1 = org_chart.add_child('Staff1', manager)
        org_chart.add_child('Kiana', staff1)
        staff2 = org_chart.add_child('Staff2', manager)
        org_chart.add_child('Kevin', staff2)

        display = org_chart.show_org_chart()

        self.assertEqual(org_chart.show_org_chart(), display)

    def test_find_first_parent(self):
        org_chart = OrganizationChart()

        ceo = org_chart.add_child('CEO')
        manager = org_chart.add_child('Manager', ceo)
        org_chart.add_child('Secretary', manager)
        staff1 = org_chart.add_child('Staff1', manager)
        org_chart.add_child('Kiana', staff1)
        staff2 = org_chart.add_child('Staff2', manager)
        org_chart.add_child('Kevin', staff2)

        find = org_chart.find_first_parent('Kevin')
        self.assertEqual(find.name, "Staff2")

    def test_add_sibling(self):
        org_chart = OrganizationChart()

        ceo = org_chart.add_child('CEO')
        manager = org_chart.add_child('Manager', ceo)
        parent = org_chart.find_first_parent("Manager")

        self.assertTrue(org_chart.add_sibling(parent, "Vice President"))
        self.assertEqual(parent.children[-1].name, "Vice President")
        self.assertEqual(parent.children[-1].children, [])
