def divide(sort_result, list_chr_names):
    divided_by_chr = []
    for i in list_chr_names:
        name = i
        i = list()
        for j in range(len(sort_result)):
            if sort_result[j][0] == name:
                i.append(sort_result[j])
        divided_by_chr.append(i)
    return divided_by_chr


def merge_by_chr(temp_tuple):
    merged = [temp_tuple[0]]
    for current in temp_tuple:
        previous = merged[-1]
        if current[1] <= previous[2]:
            previous[2] = max(previous[2], current[2])
        else:
            merged.append(current)
    return merged


def merge(bed_entries: list):
    result = list()
    names = set()
    for i in bed_entries:
        names.add(i[0])
    names = sorted(list(names))
    divided_by_chr = divide(bed_entries, names)
    for i in divided_by_chr:
        result.append(merge_by_chr(i))
    return result

