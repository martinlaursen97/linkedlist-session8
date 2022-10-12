class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __getitem__(self, position):
        length = len(self)

        if isinstance(position, slice):
            start = position.start if position.start >= 0 else position.start + length
            stop = position.stop if position.step >= 0 else position.stop + length
            step = position.step if position.step is not None else 1

            print(start, stop, step)

            return [self[i] for i in range(start, stop, step)]

        if position < length:
            if position < 0:
                position += length

            curr = self.head

            for i in range(position):
                curr = curr.next

            return curr.data
        raise Exception(f'Out of bounds with LinkedList length: {length}, position: {position}')

    def __repr__(self):
        curr = self.head
        rep = [str(curr.data)]
        while curr.next is not None:
            curr = curr.next
            rep.append(str(curr.data))

        return f"[{', '.join(rep)}]"

    def __len__(self):
        length = 1

        curr = self.head
        while curr.next is not None:
            curr = curr.next
            length += 1

        return length


llist = LinkedList()
llist.head = Node(1)
llist.head.next = Node(2)
llist.head.next.next = Node(3)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(5)
llist.head.next.next.next.next.next = Node(6)
llist.head.next.next.next.next.next.next = Node(7)
llist.head.next.next.next.next.next.next.next = Node(8)

print(llist[-1:-7:-1])

lst = [1, 2, 3, 4, 5, 6, 7, 8]

print(lst[-1:-7:-1])
# print(len(llist))
