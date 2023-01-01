class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        self.size = 0

        [self.append(value) for value in values if values]

    def append(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = self.tail
        self.size += 1

    def extend(self, other):
        self.tail.next = other
        self.tail = other.tail
        self.size += len(other)

    def __get_nodes_sliced(self, slice):
        start = slice.start if slice.start >= 0 else slice.start + len(self)
        stop = slice.stop
        step = slice.step or 1

        return LinkedList(*[self[index].value for index in range(start, stop, step)])

    def __get_node_indexed(self, index):
        if index >= len(self) or index < -len(self):
            raise IndexError('LinkedList index out of range')

        index += len(self) if index < 0 else 0

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration

        node = self.current
        self.current = self.current.next
        return node

    def __getitem__(self, key):
        if not self.head:
            raise IndexError('LinkedList index out of range')

        if isinstance(key, slice):
            return self.__get_nodes_sliced(key)
        return self.__get_node_indexed(key)

    def __setitem__(self, key, value):
        if key < -len(self) or key >= len(self):
            raise IndexError('LinkedList index out of range')

        key += len(self) if key < 0 else 0

        self[key].value = value

    def __len__(self):
        return self.size

    def __eq__(self, other):
        return all(i.value == j.value for i, j in zip(self, other))

    def __str__(self):
        return f'LinkedList{tuple(node.value for node in self)}'

    def __add__(self, other):
        return LinkedList(*[node.value for ll in [self, other] for node in ll])

    def __mul__(self, other):
        return LinkedList(*[node.value for node in self] * other)

    def __abs__(self):
        return LinkedList(*[abs(node.value) for node in self])


if __name__ == '__main__':
    list1 = LinkedList(-1, 2, -3, 4, -5)
    list2 = LinkedList(6, -7, 8, -9, 10)
    list3 = list1 + list2
    list4 = [i.value for i in list3]

    print(list3)
    print(list3[0])
    list3[-1] = -1000
    print(list3[-4:0:-1])
    print(list4[-4:0:-1])

    print()

    print(len(list3))
    print(LinkedList(1, 2, 3) == LinkedList(1, 2, 3))

    print()

    print(list3)
    print(list3 * 3)
    print(abs(list3))

