import DoublyLinkedList as dll


def insert_list_to_dll(list, has_pic=None):
    if has_pic:
        new_dll = dll.DoubleDataDoublyLinkedList()
    else:
        new_dll = dll.DoublyLinkedList()
    # dllは値が先頭に追加されていく．
    # listの順番を守るために，末尾から追加していく．
    for value in reversed(list):
        new_dll.insert(value)
    return new_dll


def insertion_sort(sort_target, comp_func):
    """
    >>> sort_target_list = [5, 2, 4, 6, 1, 3]

    >>> ascending_target_list   = sort_target_list.copy()
    >>> descending_target_list  = sort_target_list.copy()
    >>> odd_even_list           = sort_target_list.copy()

    >>> insertion_sort(ascending_target_list, comp_func = lambda x, y: x > y)
    insertion sort
    >>> print(ascending_target_list)
    [1, 2, 3, 4, 5, 6]

    >>> insertion_sort(descending_target_list, comp_func = lambda x, y: x < y)
    insertion sort
    >>> print(descending_target_list)
    [6, 5, 4, 3, 2, 1]

    >>> # 前の値(x)が大きい かつ 奇数<偶数が成り立っていない時
    >>> # または 偶数<奇数のときTrueを返して入れ替える
    >>> insertion_sort(odd_even_list, comp_func = lambda x, y: True if x > y and not(x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1) else False)
    insertion sort
    >>> print(odd_even_list)
    [1, 3, 5, 2, 4, 6]


    >>> ascending_target_dll    = insert_list_to_dll(sort_target_list)
    >>> descending_target_dll   = insert_list_to_dll(sort_target_list)
    >>> odd_even_dll            = insert_list_to_dll(sort_target_list)

    >>> insertion_sort(ascending_target_dll, comp_func = lambda x, y: x > y)
    insertion sort
    >>> ascending_target_dll.show()
    1 2 3 4 5 6

    >>> insertion_sort(descending_target_dll, comp_func = lambda x, y: x < y)
    insertion sort
    >>> descending_target_dll.show()
    6 5 4 3 2 1

    >>> # 前の値(x)が大きい かつ 奇数<偶数が成り立っていない時
    >>> # または 偶数<奇数のときTrueを返して入れ替える
    >>> insertion_sort(odd_even_dll, comp_func = lambda x, y: True if x > y and not(x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1) else False)
    insertion sort
    >>> odd_even_dll.show()
    1 3 5 2 4 6
    """
    print("insertion sort")
    if type(sort_target) is list:
        # "cp" は comparison_position．
        # "tp" は target_position．
        for cp in range(1, len(sort_target)):
            comparison = sort_target[cp]
            tp = cp - 1
            while tp >= 0 and comp_func(sort_target[tp], comparison):
                sort_target[tp+1] = sort_target[tp]
                tp -= 1
            sort_target[tp+1] = comparison

    else:
        ct = sort_target.head.next.next  # comparison_target
        while ct is not sort_target.tail:
            sorted = ct.prev
            while (
                sorted is not sort_target.head
                and
                comp_func(sorted.value, ct.value)
            ):
                sorted = sorted.prev

            # 次のcomparison_targetはcomparison_targetの次．上書きされないように保持
            new_target = ct.next

            # sortedの後ろにcomparison_targetを挿入
            # 改善点: swap関数としてまとめたほうが良いかも．
            ct.prev.next = ct.next
            ct.next.prev = ct.prev
            ct.next = sorted.next
            ct.prev = sorted
            sorted.next.prev = ct
            sorted.next = ct

            ct = new_target


def bubble_sort(sort_target, comp_func):
    """
    >>> sort_target_list = [5, 2, 4, 6, 1, 3]

    >>> ascending_target_list   = sort_target_list.copy()
    >>> descending_target_list  = sort_target_list.copy()
    >>> odd_even_list           = sort_target_list.copy()

    >>> bubble_sort(ascending_target_list, comp_func = lambda x, y: x > y)
    bubble sort
    >>> print(ascending_target_list)
    [1, 2, 3, 4, 5, 6]

    >>> bubble_sort(descending_target_list, comp_func = lambda x, y: x < y)
    bubble sort
    >>> print(descending_target_list)
    [6, 5, 4, 3, 2, 1]

    >>> # 前の値(x)が大きい かつ 奇数<偶数が成り立っていない時
    >>> # または 偶数<奇数のときTrueを返して入れ替える
    >>> bubble_sort(odd_even_list, comp_func = lambda x, y: True if x > y and not(x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1) else False)
    bubble sort
    >>> print(odd_even_list)
    [1, 3, 5, 2, 4, 6]


    >>> ascending_target_dll    = insert_list_to_dll(sort_target_list)
    >>> descending_target_dll   = insert_list_to_dll(sort_target_list)
    >>> odd_even_dll            = insert_list_to_dll(sort_target_list)

    >>> bubble_sort(ascending_target_dll, comp_func = lambda x, y: x > y)
    bubble sort
    >>> ascending_target_dll.show()
    1 2 3 4 5 6

    >>> bubble_sort(descending_target_dll, comp_func = lambda x, y: x < y)
    bubble sort
    >>> descending_target_dll.show()
    6 5 4 3 2 1

    >>> # 前の値(x)が大きい かつ 奇数<偶数が成り立っていない時
    >>> # または 偶数<奇数のときTrueを返して入れ替える
    >>> bubble_sort(odd_even_dll, comp_func = lambda x, y: True if x > y and not(x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1) else False)
    bubble sort
    >>> odd_even_dll.show()
    1 3 5 2 4 6
    """
    print("bubble sort")
    if type(sort_target) is list:
        # replace_count = 0
        exist_unsorted_pair = True
        unsorted_top_position = 1
        has_picture = type(sort_target[0]) is str

        while exist_unsorted_pair:
            exist_unsorted_pair = False
            # "tp" は target_position
            for tp in range(len(sort_target)-unsorted_top_position):
                tp = len(sort_target) - tp - 1  # N-1 ~ unsorted_top_position+1
                if (
                    has_picture and comp_func(
                        sort_target[tp-1][1], sort_target[tp][1])
                ) or (
                    not has_picture and comp_func(
                        sort_target[tp-1], sort_target[tp])
                ):
                    tmp = sort_target[tp]
                    sort_target[tp] = sort_target[tp-1]
                    sort_target[tp-1] = tmp
                    exist_unsorted_pair = True
                    # replace_count += 1
            unsorted_top_position += 1
    else:
        # replace_count = 0
        exist_unsorted_pair = True
        unsorted_top = sort_target.head.next

        while exist_unsorted_pair:
            exist_unsorted_pair = False
            target = sort_target.tail.prev
            while target is not unsorted_top:
                if comp_func(target.prev.value, target.value):
                    # 未ソート部の先頭が上書きされないようにする
                    unsorted_top_prev = unsorted_top.prev

                    # a(tmp_prev) - b(tmp_next) - c(target) - d  を
                    # a           - c           - b         - d  に入れ替える
                    # 改善点: swap関数としてまとめたほうが良いかも．
                    tmp_prev = target.prev.prev
                    tmp_next = target.prev
                    target.prev.prev.next = target
                    target.prev.prev = target
                    target.prev.next = target.next
                    target.next.prev = target.prev
                    target.prev = tmp_prev
                    target.next = tmp_next

                    unsorted_top = unsorted_top_prev.next

                    exist_unsorted_pair = True
                    # replace_count += 1
                else:
                    target = target.prev
            unsorted_top = unsorted_top.next
    # return replace_count


def selection_sort(sort_target, comp_func):
    """
    >>> sort_target_list = [5, 2, 4, 6, 1, 3]

    >>> ascending_target_list   = sort_target_list.copy()
    >>> descending_target_list  = sort_target_list.copy()
    >>> odd_even_list           = sort_target_list.copy()

    >>> selection_sort(ascending_target_list, comp_func = lambda x, y: x > y)
    selection sort
    >>> print(ascending_target_list)
    [1, 2, 3, 4, 5, 6]

    >>> selection_sort(descending_target_list, comp_func = lambda x, y: x < y)
    selection sort
    >>> print(descending_target_list)
    [6, 5, 4, 3, 2, 1]

    >>> # 前の値(x)が大きい かつ 奇数<偶数が成り立っていない時
    >>> # または 偶数<奇数のときTrueを返して入れ替える
    >>> selection_sort(odd_even_list, comp_func = lambda x, y: True if x > y and not(x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1) else False)
    selection sort
    >>> print(odd_even_list)
    [1, 3, 5, 2, 4, 6]


    >>> ascending_target_dll    = insert_list_to_dll(sort_target_list)
    >>> descending_target_dll   = insert_list_to_dll(sort_target_list)
    >>> odd_even_dll            = insert_list_to_dll(sort_target_list)

    >>> selection_sort(ascending_target_dll, comp_func = lambda x, y: x > y)
    selection sort
    >>> ascending_target_dll.show()
    1 2 3 4 5 6

    >>> selection_sort(descending_target_dll, comp_func = lambda x, y: x < y)
    selection sort
    >>> descending_target_dll.show()
    6 5 4 3 2 1

    >>> # 前の値(x)が大きい かつ 奇数<偶数が成り立っていない時
    >>> # または 偶数<奇数のときTrueを返して入れ替える
    >>> selection_sort(odd_even_dll, comp_func = lambda x, y: True if x > y and not(x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1) else False)
    selection sort
    >>> odd_even_dll.show()
    1 3 5 2 4 6
    """
    print("selection sort")
    if type(sort_target) is list:
        # replace_count = 0
        has_picture = type(sort_target[0]) is str
        for unsorted_top_position in range(len(sort_target)):
            # count_flag = False
            tmp_min = unsorted_top_position
            for i in range(unsorted_top_position, len(sort_target)):
                if (
                    has_picture and comp_func(
                        sort_target[tmp_min][1], sort_target[i][1])
                ) or (
                    not has_picture and comp_func(
                        sort_target[tmp_min], sort_target[i])
                ):
                    tmp_min = i
                    # count_flag = True

            tmp = sort_target[unsorted_top_position]
            sort_target[unsorted_top_position] = sort_target[tmp_min]
            sort_target[tmp_min] = tmp

            # if count_flag:
            # replace_count += 1
    else:
        # replace_count = 0
        unsorted_top = sort_target.head.next
        while unsorted_top is not sort_target.tail:
            # count_flag = False
            min = unsorted_top
            target = unsorted_top.next
            while target is not sort_target.tail:
                if comp_func(min.value, target.value):
                    min = target
                    # count_flag = True
                target = target.next

            # a(unsorted_top) - b - c(tmp_prev) - d(min) - e(tmp_next)  を
            # d(unsorted_top) - b - c           - a      - e            にする
            # 改善点: swap関数としてまとめたほうが良いかも．
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

            # minとunsorted_topが隣り合っていたときの対策
            # min.nextがmin自身，unsorted_top.prevも自身を指している．
            if min.next is min:
                min.next = unsorted_top
                unsorted_top.prev = min

            unsorted_top = min.next
            # if count_flag:
            # replace_count += 1
            # return replace_count


def stable_sort(sort_target):
    """
    >>> # データの準備 listはミュータブルでソート関数を通すと上書きされる．
    >>> # 先にdllにも同じリストをコピーしておく．
    >>> sort_target_list = ['H4', 'C9', 'S4', 'D2', 'C3']
    >>> sort_target_dll = insert_list_to_dll(sort_target_list, has_pic=True)
    >>> stable_sort(sort_target_list)
    stable sort
    bubble sort
    ['D2', 'C3', 'H4', 'S4', 'C9']
    Stable
    selection sort
    ['D2', 'C3', 'S4', 'H4', 'C9']
    Not stable
    >>> stable_sort(sort_target_dll)
    stable sort
    bubble sort
    D2 C3 H4 S4 C9
    Stable
    selection sort
    D2 C3 S4 H4 C9
    Not stable
    """
    print("stable sort")
    is_dddll = type(sort_target) is dll.DoubleDataDoublyLinkedList

    bubble_sort_target = sort_target.copy()
    bubble_sort(bubble_sort_target, comp_func=lambda x, y: x > y)
    if is_dddll:
        bubble_sort_target.show()
    else:
        print(bubble_sort_target)

    print("Stable")  # Bubble sort is always stable

    selection_sort_target = sort_target.copy()
    selection_sort(selection_sort_target, comp_func=lambda x, y: x > y)

    if is_dddll:
        selection_sort_target.show()
    else:
        print(selection_sort_target)

    if is_dddll:
        # bubble sort と selection sortの結果をheadから順に比較
        bubble_item = bubble_sort_target.head.next
        selection_item = selection_sort_target.head.next
        while bubble_item is not bubble_sort_target.tail:
            if (
                bubble_item.value != selection_item.value
                or
                bubble_item.picture != selection_item.picture
            ):
                print("Not stable")
                return
            bubble_item = bubble_item.next
            selection_item = selection_item.next
        print("Stable")
    elif bubble_sort_target == selection_sort_target:
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
