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

    def __str__(self):
        return f"Sll with length {self.length}"

    # Length instance attribute
    # "read-only" length property
    @property
    def length(self):
        return self._length

    # Traverse
    def traverse(self, idx):

        # handle negative indices
        if (idx < 0):
            idx = self._length + idx

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

        # handle negative indices
        if (idx < 0):
            idx = self._length + idx

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


        # handle negative indices
        if (idx < 0):
            idx = self._length + idx

        # If idx 0
        if idx == 0:
            _val = self.head.value
            self.head = self.head.link
            self._length -= 1

            # If no other members
            if self._length == 0:
                self.tail = None

            return _val

        # other indices
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

    def search(self, given_val):
        """
        search
        if given_val is in the sll, return the idx
        of the first occurrence
        else return -1
        """


        # If list empty
        # if (
        #     self._length == 0
        # ):
        #     raise IndexError("idx out of range")

        i = 0
        _current_node = self.head

        while _current_node != None:
            val = _current_node.value
            if val == given_val:
                return i
            _current_node = _current_node.link
            i += 1

        return -1


tail = MyNode(3, None)
mid = MyNode(2, tail)
head = MyNode(1, mid)


sll = MySLL(head=head, tail=tail)
print(sll.length)
print(sll.traverse)
print(sll.length)
print(sll.search(5))
sll = MySLL(head=1,tail=2)
print(sll.length)
