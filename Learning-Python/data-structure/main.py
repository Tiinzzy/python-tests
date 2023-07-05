# from bidirect_linkedlist.bidirectional_linkedlist import BidirectionalLinkelist

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
    brute_force()
