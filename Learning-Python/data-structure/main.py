# from bidirect_linkedlist.bidirectional_linkedlist import BidirectionalLinkelist
from tree.organization_chart import OrganizationChart
from hash_map.hashmap import HashMap, BidirectionalLinkelist
import string
import random
import numpy as np
import time
from binary_tree.binary_tree import BinaryTree
from matrix.matrix import Matrix

letters = string.ascii_lowercase


def random_string():
    return ''.join(random.choice(letters) for i in range(10))


def brute_force():
    your_hash = HashMap()
    for i in range(10000):
        your_hash.insert(random_string(), i)
    your_hash.show_all_sizes()


if __name__ == '__main__':
    # tree = OrganizationChart()
    # ceo = tree.add_child('CEO')
    #
    # manager = tree.add_child('Manager', ceo)
    # secretary = tree.add_child('Secretary', manager)
    # staff1 = tree.add_child('Staff1', manager)
    # Kiana = tree.add_child('Kiana', staff1)
    # staff2 = tree.add_child('Staff2', manager)
    # Kevin = tree.add_child('Kevin', staff2)
    #
    # vice_president = tree.add_child('VicePresident', ceo)
    # secretary = tree.add_child('Secretary', vice_president)
    # gina = tree.add_child('Gina', secretary)
    # staff3 = tree.add_child('Staff3', vice_president)
    # Poopoo = tree.add_child('PooPoo', staff3)
    #
    # tree.show_org_chart()
    # print('>>>>>>>>>>>>>')
    # print(tree.find_first_parent('Staff3').name)
    #
    # tree.add_sibling(tree.find_first_parent('Staff3'), 'Kamran')
    # tree.add_sibling(tree.find_first_parent('Kamran'), 'Tina')
    # tree.show_org_chart()

    # br_tree = BinaryTree()
    # br_tree.insert(40)
    # br_tree.insert(39)
    # br_tree.insert(41)
    # br_tree.insert(38)
    # br_tree.insert(47)
    # br_tree.show()
    #
    # print(br_tree.node_exist(1.5))
    # print('---------------------------')
    #
    # seed = time.time() * 1000
    # count = 100000
    # max_num = 10000
    # search_for = int(random.random() * max_num)
    #
    # random.seed(seed)
    # for i in range(count):
    #     br_tree.insert(int(random.random() * max_num))
    #
    # start_time = time.time()
    # print(br_tree.node_exist(search_for))
    # end_time = time.time()
    # print(end_time - start_time, ' seconds')
    #
    # a = []
    # random.seed(seed)
    # for i in range(count):
    #     a.append(int(random.random() * max_num))
    #
    # start_time = time.time()
    # for i in range(len(a)):
    #     if a[i] == search_for:
    #         print('FOUND!', a[i], search_for)
    #         break
    # end_time = time.time()
    # print(end_time - start_time, ' seconds')


    # br_tree = BinaryTree()
    # br_tree.insert(40)
    # br_tree.insert(39)
    # br_tree.insert(41)
    # br_tree.insert(38)
    # br_tree.insert(47)
    # br_tree.insert(44)
    # br_tree.show()
    # br_tree.remove(41)

    print('----------------------')
    mtr = Matrix()
    rand_array = np.random.choice([0, 1], size=(4, 4))
    mtr.random_insert((4, 4), 4)
    mtr.show_grid()

    start = [3, 0]
    destination = [0, 3]
    # mtr.path_to_destination(start, destination)
