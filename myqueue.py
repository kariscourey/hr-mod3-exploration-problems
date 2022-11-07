class MyQueue:

    def __init__(self, head=None, tail=None):

        self.head = head
        self.tail = tail

    # Enqueue: add Node to back of the queue
    def enqueue(self, val):

        # Instantiate new node with value
        n = Node(val)

        # If queue empty add node
        if self.head is None:

            # n should be Node, having value and link

            self.head = n
            self.tail = n

            # enqueue does not need to return a value
            return None

        else:
            # link for old tail becomes new node
            self.tail.link = n

            # tail points to new tail
            self.tail = n

    # Dequeue: remove from front of the queue and return value

    def dequeue(self):

        # Queue cannot be empty
        assert self.head, "Queue is empty."

        # Temporarily store value for node at head
        _value = self.head.value

        # Reassign head property to node
        # current head's link points to
        self.head = self.head.link

        # If final item removed
        # set tail to None as well
        if self.head is None:
            self.tail = None

        # return value
        return _value
