class Item:
    def __init__(self, x):
        self.prev = None
        self.x = x
        self.next = None


class DoublyLinkedList:
    """
    >>> dll1 = DoublyLinkedList()
    >>> dll1.insert(5)
    >>> dll1.insert(2)
    >>> dll1.insert(3)
    >>> dll1.insert(1)
    >>> dll1.delete(3)
    >>> dll1.insert(6)
    >>> dll1.delete(5)
    >>> dll1.show()
    6 1 2
    >>> dll2 = DoublyLinkedList()
    >>> dll2.insert(5)
    >>> dll2.insert(2)
    >>> dll2.insert(3)
    >>> dll2.insert(1)
    >>> dll2.delete(3)
    >>> dll2.insert(6)
    >>> dll2.delete(5)
    >>> dll2.deleteFirst()
    >>> dll2.deleteLast()
    >>> dll2.show()
    1
    """

    def __init__(self):
        self.head = Item("HEAD")
        self.tail = Item("TAIL")
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, x):
        item = Item(x)
        item.next = self.head.next
        self.head.next = item
        item.next.prev = item
        item.prev = self.head

    def delete(self, x):
        tmp = self.head.next
        while tmp is not self.tail:
            if tmp.x == x:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                return
            tmp = tmp.next

    def deleteFirst(self):
        tmp = self.head.next
        if tmp is not self.tail:
            self.head.next = tmp.next
            tmp.next.prev = self.head

    def deleteLast(self):
        tmp = self.tail.prev
        if tmp is not self.head:
            self.tail.prev = tmp.prev
            tmp.prev.next = self.tail

    def show(self):
        tmp = self.head.next
        result = ""
        while tmp is not self.tail:
            result = result + " " + str(tmp.x)
            tmp = tmp.next
        result = result[1:]
        print(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
