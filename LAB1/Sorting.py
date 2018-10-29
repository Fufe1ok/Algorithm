def selection_sort_by_table(table_list):
    for i in range(len(table_list)):
        for j in range(i + 1, len(table_list)):
            if table_list[i].tables < table_list[j].tables:
                table_list[i], table_list[j] = table_list[j], table_list[i]
    return table_list


def merge_sort_by_max_dishes(max_dishes_list):
    if len(max_dishes_list) <= 1:
        return max_dishes_list
    list_mid = int(len(max_dishes_list) / 2)
    left_list = merge_sort_by_max_dishes(max_dishes_list[:list_mid])
    right_list = merge_sort_by_max_dishes(max_dishes_list[list_mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    result_list = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i].max_dishes <= right_list[j].max_dishes:
            result_list.append(left_list[i])
            i += 1
        else:
            result_list.append(right_list[j])
            j += 1
    result_list += left_list[i:]
    result_list += right_list[j:]
    return result_list