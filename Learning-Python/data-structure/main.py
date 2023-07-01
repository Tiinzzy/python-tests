from bidirectional_linkedlist import BidirectionalLinkelist

if __name__ == '__main__':
    bll = BidirectionalLinkelist()
    bll.add(0)
    bll.add(1)
    bll.add(2)

    bll.add(3)
    bll.add(4)
    bll.add(5)
    bll.add(-1, 0)
    bll.add(300, 3)
    bll.add(700, 7)
    bll.show_all()

