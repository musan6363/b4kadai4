class Item:
    def __init__(self, x):
        self.prev = None
        self.x = x
        self.next = None


class DoublyLinkedList:
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
            result = result + " " + tmp.x
            tmp = tmp.next
        result = result[1:]
        print(result)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    with open("./sample1.txt") as f:
        sample = f.readlines()
        for line in sample[1:]:
            tmp = line.split()
            if len(tmp) == 2:
                eval("dll."+tmp[0])(tmp[1])
            else:
                eval("dll."+tmp[0])()
    dll.show()
