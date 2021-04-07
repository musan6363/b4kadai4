import DoublyLinkedList as dll


def insertion_sort(data):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(3)
    >>> data1.insert(1)
    >>> data1.insert(6)
    >>> data1.insert(4)
    >>> data1.insert(2)
    >>> data1.insert(5)
    >>> insertion_sort(data1)
    insertion sort
    5 2 4 6 1 3
    2 5 4 6 1 3
    2 4 5 6 1 3
    2 4 5 6 1 3
    1 2 4 5 6 3
    1 2 3 4 5 6
    >>> data2 = [5,2,4,6,1,3]
    >>> insertion_sort(data2)
    insertion sort
    [5, 2, 4, 6, 1, 3]
    [2, 5, 4, 6, 1, 3]
    [2, 4, 5, 6, 1, 3]
    [2, 4, 5, 6, 1, 3]
    [1, 2, 4, 5, 6, 3]
    [1, 2, 3, 4, 5, 6]
    """
    print("insertion sort")
    if type(data) is dll.DoublyLinkedList:
        data.show()
        target = data.head.next.next
        while target is not data.tail:
            sorted = target.prev
            while sorted is not data.head and sorted.x > target.x:
                sorted = sorted.prev
            # ここから 挿入処理
            tmp = target.next
            target.prev.next = target.next
            target.next.prev = target.prev
            target.next = sorted.next
            target.prev = sorted
            sorted.next.prev = target
            sorted.next = target
            target = tmp
            # ここまで 挿入処理
            data.show()
    else:
        print(data)
        for i in range(1, len(data)):
            target = data[i]
            j = i - 1
            while j >= 0 and data[j] > target:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = target
            print(data)


def bubble_sort(data):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(1)
    >>> data1.insert(4)
    >>> data1.insert(2)
    >>> data1.insert(3)
    >>> data1.insert(5)
    >>> bubble_sort(data1)
    bubble sort
    1 2 3 4 5
    8
    >>> data2 = [5,2,4,6,1,3]
    >>> bubble_sort(data2)
    bubble sort
    [1, 2, 3, 4, 5, 6]
    9
    """
    print("bubble sort")
    if type(data) is dll.DoublyLinkedList:
        count = 0
        flag = True
        unsorted_position = 0
        unsorted_top = data.head.next
        while flag:
            flag = False
            target_position = 0
            target = data.tail.prev
            while target is not unsorted_top:
                if target.x < target.prev.x:
                    # ここから 入替処理
                    tmp_prev = target.prev.prev
                    tmp_next = target.prev
                    target.prev.prev.next = target
                    target.prev.prev = target
                    target.prev.next = target.next
                    target.next.prev = target.prev
                    target.prev = tmp_prev
                    target.next = tmp_next
                    # ここまで 入替処理
                    flag = True
                    count += 1
                target_position += 1
                target = data.tail.prev
                for i in range(target_position):
                    target = target.prev
                unsorted_top = data.head.next
                for i in range(unsorted_position):
                    unsorted_top = unsorted_top.next
            unsorted_position += 1
            unsorted_top = data.head.next
            for i in range(unsorted_position):
                unsorted_top = unsorted_top.next
        data.show()
        print(count)
    else:
        count = 0
        flag = True
        i = 1
        while flag:
            flag = False
            for j in range(len(data)-i):
                j = len(data) - j - 1  # N-1 ~ i+1
                if data[j] < data[j-1]:
                    tmp = data[j]
                    data[j] = data[j-1]
                    data[j-1] = tmp
                    flag = True
                    count += 1
            i += 1
        print(data)
        print(count)


def selection_sort(data):
    print("selection sort")
    if type(data) is dll.DoublyLinkedList:
        unsorted_top = data.head.next
        unsorted_position = 0
        while unsorted_top is not data.tail:
            min = unsorted_top
            target = unsorted_top.next
            while target is not data.tail:
                if target.x < min.x:
                    min = target
                target = target.next
            # minとunsorted_topの交換

    else:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
