class Item:
    def __init__(self, value):
        self.prev = None
        self.value = value
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

    def insert(self, value):
        item = Item(value)
        item.next = self.head.next
        self.head.next = item
        item.next.prev = item
        item.prev = self.head

    def delete(self, value):
        tmp = self.head.next
        while tmp is not self.tail:
            if tmp.value == value:
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
            result = result + " " + str(tmp.value)
            tmp = tmp.next
        result = result[1:]
        print(result)

    def copy(self):
        dll_copy = DoublyLinkedList()
        original = self.tail.prev
        while original is not self.head:
            dll_copy.insert(original.x)
            original = original.prev
        return dll_copy


class DoubleDataDoublyLinkedList(DoublyLinkedList):
    """
    >>> dll3 = DoubleDataDoublyLinkedList()
    >>> dll3.insert("H4")
    >>> dll3.insert("C9")
    >>> dll3.insert("S4")
    >>> dll3.insert("D2")
    >>> dll3.insert("C3")
    >>> dll3.show()
    C3 D2 S4 C9 H4
    >>> dll4 = DoubleDataDoublyLinkedList()
    >>> dll4.insert("H4")
    >>> dll4.insert("C9")
    >>> dll4.insert("S4")
    >>> dll4.insert("D2")
    >>> dll4.insert("C3")
    >>> dll4.delete("D2")
    >>> dll4.delete("S4")
    >>> dll4.deleteFirst()
    >>> dll4.deleteLast()
    >>> dll4.show()
    C9
    """

    def insert(self, raw_input):
        picture = raw_input[0]
        value = int(raw_input[1])
        super(DoubleDataDoublyLinkedList, self).insert(value)
        self.head.next.picture = picture

    def delete(self, raw_input):
        picture = raw_input[0]
        value = int(raw_input[1])
        tmp = self.head.next
        while tmp is not self.tail:
            if tmp.value == value and tmp.picture == picture:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                return
            tmp = tmp.next

    def show(self):
        tmp = self.head.next
        result = ""
        while tmp is not self.tail:
            result = result + " " + tmp.picture + str(tmp.value)
            tmp = tmp.next
        result = result[1:]
        print(result)

    def copy(self):
        dll_copy = DoubleDataDoublyLinkedList()
        original = self.tail.prev
        while original is not self.head:
            dll_copy.insert(original.picture + str(original.value))
            original = original.prev
        return dll_copy


if __name__ == "__main__":
    import doctest
    doctest.testmod()
