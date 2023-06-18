from one_directional_linked_list import Node, OneDirectionLinkedList
from bi_directional_linked_list import BiDirectionLinkedList


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
    ll = one_directional_linked_list()
    ll.describe()
    ll.add_to_tail('T500')
    ll.describe()
    ll.add_to_head('T00')
    ll.describe()

    ll.remove_from_tail()
    ll.remove_from_tail()

    ll.remove_from_head()
    ll.remove_from_head()
    ll.remove_from_head()
    ll.remove_from_head()
    ll.remove_from_head()
    ll.remove_from_head()

    ll.describe()

    ll.add_to_head('NEW-BORN')
    ll.describe()


def bi_directional_tests():
    bd_ll = BiDirectionLinkedList()
    bd_ll.add_to_tail('N1')
    bd_ll.add_to_tail('N2')
    bd_ll.add_to_tail('N3')
    bd_ll.add_to_tail('N4')
    bd_ll.add_to_tail('N5')
    bd_ll.add_to_head('N0')
    bd_ll.add_to_middle('2.5', 3)
    bd_ll.show_list()
    print('---------')
    bd_ll.remove_from_middle('2.5')
    bd_ll.show_list()
    print('---------')

def test_stack():
    from stack import Stack
    stack = Stack(100)
    stack.push(1)
    stack.push(31)
    stack.push(51)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.push(5134)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    # initial_tests()

    # my_ll = test_head_tail()
    # my_ll.describe()

    # To see all linked lists and then see the removed one
    my_ll = one_directional_linked_list()
    my_ll.describe()
    my_ll.remove_payload('T4')
    my_ll.describe()

    # p1 = {'a': 'T33'}
    # my_ll.add_to_tail(p1)
    # my_ll.describe()
    # p2 = {'a': 'T33'}
    # res = my_ll.payload_exist(p2)

    # Go to the main function on the top and change the node name to see it removed
    # you can test remove from tail or head and remove from middle
    bi_directional_tests()

    # test_stack()
