# from bidirect_linkedlist.bidirectional_linkedlist import BidirectionalLinkelist
from tree.organization_chart import OrganizationChart
from hash_map.hashmap import HashMap, BidirectionalLinkelist
import string
import random

letters = string.ascii_lowercase


def random_string():
    return ''.join(random.choice(letters) for i in range(10))


def brute_force():
    your_hash = HashMap()
    for i in range(10000):
        your_hash.insert(random_string(), i)
    your_hash.show_all_sizes()


if __name__ == '__main__':
    tree = OrganizationChart()
    ceo = tree.add_child('CEO')

    manager = tree.add_child('Manager', ceo)
    secretary = tree.add_child('Secretary', manager)
    staff1 = tree.add_child('Staff1', manager)
    Kiana = tree.add_child('Kiana', staff1)
    staff2 = tree.add_child('Staff2', manager)
    Kevin = tree.add_child('Kevin', staff2)

    vice_president = tree.add_child('VicePresident', ceo)
    secretary = tree.add_child('Secretary', vice_president)
    gina = tree.add_child('Gina', secretary)
    staff3 = tree.add_child('Staff3', vice_president)
    Poopoo = tree.add_child('PooPoo', staff3)

    tree.show_org_chart()

    print()

    tree.add_child('Suzan', tree.find_first_node('Staff22'))

    tree.show_org_chart()
