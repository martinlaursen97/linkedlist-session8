from itertools import count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.__curr = self.head
        return self

    def __next__(self):
        curr = self.__curr
        if curr is None:
            raise StopIteration
        self.__curr = curr.next
        return curr

    def __getitem__(self, key):
        length = len(self)

        if isinstance(key, slice):
            start = key.start if key.start > 0 else key.start + length
            stop = key.stop if key.stop > 0 else key.stop + length
            step = key.step if key.step is not None else 1

            new_llist = LinkedList()
            new_llist.head = Node(self[start].data)

            curr = new_llist.head
            for i in range(start + step, stop, step):
                curr.next = Node(self[i].data)
                curr = curr.next

            return new_llist
        else:
            _key = key if key >= 0 else key + length

            if _key >= length or _key < 0:
                raise Exception(f'Out of bounds with LinkedList length {length}, key {key}')

            it = iter(self)
            node = next(it)
            for i in range(_key):
                node = next(it)
            return node

    def __setitem__(self, key, value):
        length = len(self)

        if key >= length:
            raise Exception(f'Out of bounds with LinkedList length {length}, key {key}')

        if key == 0:
            value.next = self.head
            self.head = value
            return

        if key == -1:
            self[-1].next = value
            return

        value.next = self[-1]
        self[key].next = value

    def __add__(self, other):
        self[-1].next = other.head

    def __repr__(self):
        return str([self[i].data for i in range(len(self))])

    def __len__(self):
        return len([i for i in self])

    def __del__(self):
        self.head = None


llist = LinkedList()
llist.head = Node(1)
llist.head.next = Node(2)
llist.head.next.next = Node(3)
llist.head.next.next.next = Node(4)

llist[0] = Node(10)
print(llist)
llist[-1] = Node(12)

print(llist)
