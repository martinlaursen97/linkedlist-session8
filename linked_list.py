class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


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
        self[key].value = value

    def __len__(self):
        return self.size

    def __eq__(self, other):
        return all(i.value == j.value for i, j in zip(self, other))

    def __str__(self):
        return f'LinkedList{tuple(node.value for node in self)}'

    def __add__(self, other):
        return LinkedList(*[node.value for ll in [self, other] for node in ll])


if __name__ == '__main__':
    list1 = LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(list1[-1:1:-2])
    print(list2[-1:1:-2])
