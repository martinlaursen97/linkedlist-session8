class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def new_deref(llist):
    new_llist = LinkedList()

    new_llist.head = Node(llist[0].data)
    curr = new_llist.head
    for i in range(1, len(llist)):
        curr.next = Node(llist[i].data)
        curr = curr.next
    return new_llist


class LinkedList:
    def __init__(self):
        self.head = None

    # TODO: ...

    def append(self, node):
        pass

    def copy(self):
        pass

    def count(self):
        pass

    def clear(self):
        pass

    def index(self):
        pass

    def sort(self):
        pass

    def remove(self, element):
        pass

    def __reversed__(self):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        pass

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
        llist1 = new_deref(self)
        llist2 = new_deref(other)
        llist1[-1].next = llist2.head
        return llist1

    def __mul__(self, val):
        llist = new_deref(self)
        for i in range(val):
            llist += llist
        return llist

    def __repr__(self):
        return f'LinkedList({str([self[i].data for i in range(len(self))])})'

    def __len__(self):
        return len([i for i in self])


llist = LinkedList()
llist.head = Node(1)
llist.head.next = Node(2)
llist.head.next.next = Node(3)
llist.head.next.next.next = Node(4)

llist2 = LinkedList()
llist2.head = Node(11)
llist2.head.next = Node(22)
llist2.head.next.next = Node(33)
llist2.head.next.next.next = Node(44)

llist3 = llist + llist2
