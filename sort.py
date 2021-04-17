import DoublyLinkedList as dll


class AbstractSort:
    def sort(self, sort_target, comp_func):
        raise NotImplementedError


def get_sort_instance(algorithm_name):
    return eval(algorithm_name+'Sort')()


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
                # 改善点: swap関数としてまとめたほうが良いかも．
                ct.prev.next = ct.next
                ct.next.prev = ct.prev
                ct.next = sorted.next
                ct.prev = sorted
                sorted.next.prev = ct
                sorted.next = ct

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
