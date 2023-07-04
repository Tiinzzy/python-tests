# from bidirect_linkedlist.bidirectional_linkedlist import BidirectionalLinkelist

from hash_map.hashmap import HashMap, BidirectionalLinkelist


if __name__ == '__main__':
    my_hash = HashMap()

    my_hash.insert('Tina', {1, 2, 3})
    my_hash.insert('Tania', {4, 5, 6})
    #
    my_hash.insert('Kiana', {4, 5, 6})
    my_hash.insert('Kamran', {1, 2, 3})
    my_hash.insert('Kevin', {1, 2})

    my_hash.insert('!', {1, 2, 3})

    my_hash.show_all()

    print('>>>>>>>>>>')
    my_hash.remove('Kiana')
    print('>>>>>>>>>>')
    my_hash.show_all()


