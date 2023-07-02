from bidirectional_linkedlist import BidirectionalLinkelist


if __name__ == '__main__':
    bll = BidirectionalLinkelist()
    bll.add(0)
    bll.add(1)
    bll.add(2)
    bll.add({'a': 1, 'name': 'Tina'}, 3)
    bll.add(3)
    bll.add(4)
    bll.add(5)
    bll.add(-1, 0)
    bll.add(300, 3)
    bll.add(700, 7)
    bll.add({'a': 1, 'name': 'Tina'})

    bll.show_all()
    bll.show_all(reverse=True)
    print('-----------------------')

    def my_search(e):
        return isinstance(e, dict) and e['name'] == 'Tina'

    print(bll.find_first(my_search))
    print(bll.find_first(lambda x: isinstance(
        x, dict) and x['name'] == 'Tina'))
