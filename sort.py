import DoublyLinkedList as dll


def insertion_sort(data, comp_func):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(3)
    >>> data1.insert(1)
    >>> data1.insert(6)
    >>> data1.insert(4)
    >>> data1.insert(2)
    >>> data1.insert(5)
    >>> ascending1 = data1.copy()
    >>> insertion_sort(ascending1, comp_func = lambda x, y: x < y)
    insertion sort
    >>> ascending1.show()
    1 2 3 4 5 6
    >>> descending1 = data1.copy()
    >>> insertion_sort(descending1, comp_func = lambda x, y: x > y)
    insertion sort
    >>> descending1.show()
    6 5 4 3 2 1
    >>> odd_even1 = data1.copy()
    >>> insertion_sort(odd_even1, comp_func = (
            lambda x, y: (
                True if (x < y and not(x % 2 == 0 and y % 2 == 1)) else (
                    True if (x % 2 == 1 and y % 2 == 0) else False
                )
            )
            )
        )
    insertion sort
    >>> odd_even1.show()
    1 3 5 2 4 6
    >>> ascending2 = [5,2,4,6,1,3]
    >>> insertion_sort(ascending2, comp_func = lambda x, y: x < y)
    insertion sort
    >>> print(ascending2)
    [1, 2, 3, 4, 5, 6]
    >>> descending2 = [5,2,4,6,1,3]
    >>> insertion_sort(descending2, comp_func = lambda x, y: x > y)
    insertion sort
    >>> print(descending2)
    [6, 5, 4, 3, 2, 1]
    >>> odd_even2 = [5,2,4,6,1,3]
    >>> insertion_sort(odd_even2, comp_func = (
            lambda x, y: (
                True if (x < y and not(x % 2 == 0 and y % 2 == 1)) else (
                    True if (x % 2 == 1 and y % 2 == 0) else False
                )
            )
            )
        )
    insertion sort
    >>> print(odd_even2)
    [1, 3, 5, 2, 4, 6]
    """
    print("insertion sort")
    if type(data) is list:
        # print(data)
        for i in range(1, len(data)):
            target = data[i]
            j = i - 1
            while j >= 0 and comp_func(target, data[j]):
                data[j+1] = data[j]
                j -= 1
            data[j+1] = target
            # print(data)

    else:
        # data.show()
        target = data.head.next.next
        while target is not data.tail:
            sorted = target.prev
            while sorted is not data.head and comp_func(target.x, sorted.x):
                sorted = sorted.prev
            new_target = target.next  # 次のtargetはtargetの次．上書きされないように保持
            # ここから 挿入処理 sortedの後ろにtargetを挿入
            target.prev.next = target.next
            target.next.prev = target.prev
            target.next = sorted.next
            target.prev = sorted
            sorted.next.prev = target
            sorted.next = target
            # ここまで 挿入処理
            target = new_target
            # data.show()


def bubble_sort(data, comp_func):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(1)
    >>> data1.insert(4)
    >>> data1.insert(2)
    >>> data1.insert(3)
    >>> data1.insert(5)
    >>> ascending1 = data1.copy()
    >>> count = bubble_sort(ascending1, comp_func = lambda x, y: x < y)
    bubble sort
    >>> ascending1.show()
    1 2 3 4 5
    >>> descending1 = data1.copy()
    >>> count = bubble_sort(descending1, comp_func = lambda x, y: x > y)
    bubble sort
    >>> descending1.show()
    5 4 3 2 1
    >>> odd_even1 = data1.copy()
    >>> count = bubble_sort(odd_even1, comp_func = (
            lambda x, y: (
                True if (x < y and not(x % 2 == 0 and y % 2 == 1)) else (
                    True if (x % 2 == 1 and y % 2 == 0) else False
                )
            )
            )
        )
    bubble sort
    >>> odd_even1.show()
    1 3 5 2 4
    >>> ascending2 = [5,2,4,6,1,3]
    >>> count = bubble_sort(ascending2, comp_func = lambda x, y: x < y)
    bubble sort
    >>> print(ascending2)
    [1, 2, 3, 4, 5, 6]
    >>> descending2 = [5,2,4,6,1,3]
    >>> bubble_sort(descending2, comp_func = lambda x, y: x > y)
    bubble sort
    >>> print(descending2)
    [6, 5, 4, 3, 2, 1]
    >>> odd_even2 = [5,2,4,6,1,3]
    >>> bubble_sort(odd_even2, comp_func = (
            lambda x, y: (
                True if (x < y and not(x % 2 == 0 and y % 2 == 1)) else (
                    True if (x % 2 == 1 and y % 2 == 0) else False
                )
            )
            )
        )
    bubble sort
    >>> print(odd_even2)
    [1, 3, 5, 2, 4, 6]
    """
    print("bubble sort")
    if type(data) is list:
        count = 0
        flag = True
        i = 1
        while flag:
            flag = False
            for j in range(len(data)-i):
                j = len(data) - j - 1  # N-1 ~ i+1
                if (
                    type(data[j]) is str and comp_func(
                        data[j][1], data[j-1][1])
                ) or (
                    type(data[j]) is int and comp_func(data[j], data[j-1])
                ):
                    tmp = data[j]
                    data[j] = data[j-1]
                    data[j-1] = tmp
                    flag = True
                    count += 1
            i += 1
    else:
        count = 0
        flag = True
        unsorted_top = data.head.next
        while flag:
            flag = False
            target = data.tail.prev
            while target is not unsorted_top:
                if comp_func(target.x, target.prev.x):
                    unsorted_top_prev = unsorted_top.prev  # 上書き防止
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
                    unsorted_top = unsorted_top_prev.next
                    flag = True
                    count += 1
                else:
                    target = target.prev
            unsorted_top = unsorted_top.next
    return count


def selection_sort(data, comp_func):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(3)
    >>> data1.insert(1)
    >>> data1.insert(2)
    >>> data1.insert(4)
    >>> data1.insert(6)
    >>> data1.insert(5)
    >>> ascending1 = data1.copy()
    >>> count = selection_sort(ascending1, comp_func = lambda x, y: x < y)
    selection sort
    >>> ascending1.show()
    1 2 3 4 5 6
    >>> descending1 = data1.copy()
    >>> count = selection_sort(descending1, comp_func = lambda x, y: x > y)
    selection sort
    >>> descending1.show()
    5 4 3 2 1
    >>> odd_even1 = data1.copy()
    >>> count = selection_sort(odd_even1, comp_func = (
            lambda x, y: (
                True if (x < y and not(x % 2 == 0 and y % 2 == 1)) else (
                    True if (x % 2 == 1 and y % 2 == 0) else False
                )
            )
            )
        )
    selection sort
    >>> odd_even1.show()
    1 3 5 2 4
    >>> ascending2 = [5,2,4,6,1,3]
    >>> count = selection_sort(ascending2, comp_func = lambda x, y: x < y)
    selection sort
    >>> print(ascending2)
    [1, 2, 3, 4, 5, 6]
    >>> descending2 = [5,2,4,6,1,3]
    >>> selection_sort(descending2, comp_func = lambda x, y: x > y)
    selection sort
    >>> print(descending2)
    [6, 5, 4, 3, 2, 1]
    >>> odd_even2 = [5,2,4,6,1,3]
    >>> selection_sort(odd_even2, comp_func = (
            lambda x, y: (
                True if (x < y and not(x % 2 == 0 and y % 2 == 1)) else (
                    True if (x % 2 == 1 and y % 2 == 0) else False
                )
            )
            )
        )
    selection sort
    >>> print(odd_even2)
    [1, 3, 5, 2, 4, 6]
    """
    print("selection sort")
    if type(data) is list:
        count = 0
        for i in range(len(data)):
            count_flag = False
            minj = i
            for j in range(i, len(data)):
                if (
                    type(data[j]) is str and comp_func(
                        data[j][1], data[minj][1])
                ) or (
                    type(data[j]) is int and comp_func(data[j], data[minj])
                ):
                    minj = j
                    count_flag = True
            tmp = data[i]
            data[i] = data[minj]
            data[minj] = tmp
            if count_flag:
                count += 1
    else:
        count = 0
        unsorted_top = data.head.next
        while unsorted_top is not data.tail:
            count_flag = False
            min = unsorted_top
            target = unsorted_top.next
            while target is not data.tail:
                if comp_func(target.x, min.x):
                    min = target
                    count_flag = True
                target = target.next
            # ここから minとunsorted_topの交換
            tmp_prev = min.prev
            tmp_next = min.next
            unsorted_top.prev.next = min
            unsorted_top.next.prev = min
            min.prev = unsorted_top.prev
            min.next = unsorted_top.next
            tmp_prev.next = unsorted_top
            tmp_next.prev = unsorted_top
            unsorted_top.prev = tmp_prev
            unsorted_top.next = tmp_next
            if min.next is min:
                # minとunsorted_topが隣り合っていたときの対策
                min.next = unsorted_top
                unsorted_top.prev = min
            # ここまで minとunsorted_topの交換
            unsorted_top = min.next
            if count_flag:
                count += 1
    return count


def stable_sort(data):
    """
    >>> data1 = dll.DoubleDataDoublyLinkedList()
    >>> data1.insert("C3")
    >>> data1.insert("D2")
    >>> data1.insert("S4")
    >>> data1.insert("C9")
    >>> data1.insert("H4")
    >>> stable_sort(data1)
    stable sort
    bubble sort
    D2 C3 H4 S4 C9
    Stable
    selection sort
    D2 C3 S4 H4 C9
    Not stable
    >>> data2 = dll.DoubleDataDoublyLinkedList()
    >>> data2.insert("H1")
    >>> data2.insert("S1")
    >>> stable_sort(data2)
    stable sort
    bubble sort
    S1 H1
    Stable
    selection sort
    S1 H1
    Stable
    >>> data3 = ['H4', 'C9', 'S4', 'D2', 'C3']
    >>> stable_sort(data3)
    stable sort
    bubble sort
    ['D2', 'C3', 'H4', 'S4', 'C9']
    Stable
    selection sort
    ['D2', 'C3', 'S4', 'H4', 'C9']
    Not stable
    """
    print("stable sort")
    is_dll = type(data) is dll.DoubleDataDoublyLinkedList
    bubble = data.copy()
    bubble_sort(bubble, comp_func=lambda x, y: x < y)
    if is_dll:
        bubble.show()
    else:
        print(bubble)
    print("Stable")  # Bubble sort is always stable
    selection = data.copy()
    selection_sort(selection, comp_func=lambda x, y: x < y)
    if is_dll:
        selection.show()
    else:
        print(selection)
    if bubble == selection:
        print("Stable")
    elif is_dll:
        bubble_data = bubble.head.next
        selection_data = selection.head.next
        while bubble_data is not bubble.tail:
            if (
                bubble_data.x != selection_data.x
                or
                bubble_data.picture != selection_data.picture
            ):
                print("Not stable")
                return
            bubble_data = bubble_data.next
            selection_data = selection_data.next
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
