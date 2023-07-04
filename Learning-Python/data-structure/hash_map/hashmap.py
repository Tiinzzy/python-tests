from hash_map.bidirectional_linkedlist import BidirectionalLinkelist


class HashMap:
    def __init__(self):
        self.hash_keys = {}

    @staticmethod
    def _hash_function(key):
        if len(key) > 0:
            return key[0]
        else:
            return ''

    @staticmethod
    def _search_criteria(x, key):
        return isinstance(x, dict) and x['key'] == key

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        if hash_key not in self.hash_keys.keys():
            self.hash_keys[hash_key] = BidirectionalLinkelist()
        self.hash_keys[hash_key].add({'key': key, 'value': value})

    def get(self, key):
        hash_key = self._hash_function(key)
        if hash_key not in self.hash_keys.keys():
            return None
        return self.hash_keys[hash_key].find_first(lambda x: self._search_criteria(x, key))

    def remove(self, key):
        hash_key = self._hash_function(key)
        if hash_key not in self.hash_keys.keys():
            return False
        else:
            linked_list = self.hash_keys[hash_key]
            node_to_remove_index = linked_list.find_first_index(lambda x: self._search_criteria(x, key))
            if node_to_remove_index < 0:
                return False
            else:
                linked_list.remove(node_to_remove_index)
                return True

    def show_all(self):
        print(self.hash_keys)
        for key, linked_list in self.hash_keys.items():
            print(key)
            linked_list.show_all()
            print('--------')
            # current_node = linked_list.head
            # while current_node is not None:
            #     print(current_node.payload['key'], current_node.payload['value'])
            #     current_node = current_node.next
