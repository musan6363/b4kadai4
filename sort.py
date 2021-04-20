import DoublyLinkedList as dll


class AbstractSort:
    def sort(self, sort_target, comp_func):
        raise NotImplementedError


def get_sort_instance(algorithm_name):
    return eval(algorithm_name+'Sort')()


def swap(swap_target, x, y):
    tmp = swap_target[y]
    swap_target[y] = swap_target[x]
    swap_target[x] = tmp


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


class InsertionSort(AbstractSort):
    def sort(self, sort_target, comp_func):
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
            # 交換ではなく，挿入なのでswapメソッドは使えない．
            # a(sorted) - b - c - d(comparison_target) - e を
            # a         - d - b - c                    - d にする
            sort_target.insert_move(sorted, ct)

            ct = new_target


class BubbleSort(AbstractSort):
    def sort(self, sort_target, comp_func):
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
                    # N-1 ~ unsorted_top_position+1
                    tp = len(sort_target) - tp - 1
                    if (
                        has_picture and comp_func(
                            sort_target[tp-1][1], sort_target[tp][1])
                    ) or (
                        not has_picture and comp_func(
                            sort_target[tp-1], sort_target[tp])
                    ):
                        # listはミュータブルなので返り値不要で反映される
                        swap(sort_target, tp-1, tp)
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
                        sort_target.swap(target.prev, target)

                        unsorted_top = unsorted_top_prev.next

                        exist_unsorted_pair = True
                        # replace_count += 1
                    else:
                        target = target.prev
                unsorted_top = unsorted_top.next
        # return replace_count


class SelectionSort(AbstractSort):
    def sort(self, sort_target, comp_func):
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

                # listはミュータブルなので返り値不要で反映される
                swap(sort_target, unsorted_top_position, tmp_min)

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

                # a(unsorted_top) - b - c - d(min) - e を
                # d(unsorted_top) - b - c - a      - e にする
                sort_target.swap(unsorted_top, min)

                unsorted_top = min.next
                # if count_flag:
                # replace_count += 1
                # return replace_count


def test():
    """
    >>> values = [3, 1, 2, 5, 4, 6]
    >>> _c = get_sort_instance('Bubble')
    >>> _c.sort(values, comp_func = lambda x, y: x > y)
    bubble sort
    >>> print(values)
    [1, 2, 3, 4, 5, 6]

    >>> values = [3, 1, 2, 5, 4, 6]
    >>> _c = get_sort_instance('Insertion')
    >>> _c.sort(values, comp_func = lambda x, y: x > y)
    insertion sort
    >>> print(values)
    [1, 2, 3, 4, 5, 6]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
