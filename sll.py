class MyNode:

    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return f"Node with value:{self.value}"


class MySLL:

    def __init__(self,
                    head=None,
                    tail=None):

        self.head = head
        self.tail = tail
        self._length = 0

    # "read-only" length property
    @property
    def length(self):
        return self._length

    # Comments truncated

    def traverse(self, idx):

        # If list empty
        # If idx out of bounds
        if (
            self._length == 0 or
            idx > (self._length - 1)
        ):
            raise IndexError("idx out of range")

        # If idx not an integer
        if not isinstance(idx, int):
            raise TypeError("idx must be an integer")

        i = 0
        _current_node = self.head

        while i < idx:
            _current_node = _current_node.link
            i += 1

        return _current_node

    def insert(self, val, idx=None):

        _new_node = MyNode(val, link=None)

        # idx None (default)
        if idx is None:
            idx = self._length

        # list empty, inserting first node
        if self.head is None:
            self.head = _new_node
            self.tail = _new_node
            self._length += 1
            return None

        # insert at tail (default)
        elif (idx == self._length):
            self.tail.link = _new_node
            self.tail = _new_node
            self._length += 1
            return None

        # insert before head
        elif idx == 0:
            _new_node.link = self.head
            self.head = _new_node
            self._length += 1
            return None

        # insert between two nodes
        else:

            this_idx_node = self.traverse(idx - 1)
            next_idx_node = this_idx_node.link

            _new_node.link = next_idx_node
            this_idx_node.link = _new_node

            self._length += 1
            return None

    def remove(self, idx=0):

        # If list empty
        # If idx out of bounds
        if (
            self._length == 0 or
            idx > (self._length - 1)
        ):
            raise IndexError("idx out of range")

        # If idx not an integer
        if not isinstance(idx, int):
            raise TypeError("idx must be an integer")

        # If idx 0
        if idx == 0:
            _val = self.head.value
            self.head = self.head.link
            self._length -= 1

            # If no other members
            if self._length == 0:
                self.tail = None

            return _val

        # Other indices
        previous_idx_node = self.traverse(idx - 1)
        this_idx_node = previous_idx_node.link

        _val = this_idx_node.value

        next_idx_node = this_idx_node.link

        # connect previous to next
        previous_idx_node.link = next_idx_node

        if next_idx_node is None:
            self.tail = previous_idx_node

        self._length -= 1
        return _val

# class MySLL:

#     def __init__(self,
#                  head=None,
#                  tail=None):

#         self.head = head
#         self.tail = tail

#     # Length instance attribute

#     # Value can be returned
#     # from any location

#     # Values can be inserted
#     # into the list at any index

#     # Values can be removed
#     # from the list from any location

#     # The list can be searched
