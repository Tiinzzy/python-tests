from one_directional_linked_list import Node, OneDirectionLinkedList


def initial_tests():
    n1 = Node('tina')
    n2 = Node({'name': 'kamran'})
    n3 = Node('kiana')

    n1.set_next(n2)
    n2.set_next(n3)

    print('------------------')

    n1.show()
    n2.show()
    n3.show()

    print('------------------')

    n1.show_chain()


def test_head_tail():
    ll = OneDirectionLinkedList()
    tasks = ['T1', 'T2', 'T3', 'T4', 'T264']

    for t in tasks:
        a_task = Node(t)
        if ll.head is None:
            ll.head = a_task
            ll.tail = a_task
        else:
            ll.tail.next = a_task
            ll.tail = a_task

    return ll


def one_directional_linked_list():
    ll = OneDirectionLinkedList()
    tasks = ['T1', 'T2', 'T3', 'T4', 'T264']
    for t in tasks:
        ll.add_to_tail(t)
    return ll


def more_tests():
    my_ll = one_directional_linked_list()
    my_ll.describe()
    my_ll.add_to_tail('T500')
    my_ll.describe()
    my_ll.add_to_head('T00')
    my_ll.describe()

    my_ll.remove_from_tail()
    my_ll.remove_from_tail()

    my_ll.remove_from_head()
    my_ll.remove_from_head()
    my_ll.remove_from_head()
    my_ll.remove_from_head()
    my_ll.remove_from_head()
    my_ll.remove_from_head()

    my_ll.describe()

    my_ll.add_to_head('NEW-BORN')
    my_ll.describe()


if __name__ == '__main__':
    # initial_tests()

    # my_ll = test_head_tail()
    # my_ll.describe()

    my_ll = one_directional_linked_list()
    my_ll.describe()
    res = my_ll.payload_exist('T3')
    if res is not None:
        print(res.payload)
