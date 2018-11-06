def sort(bed_entries: list):


    def divide(parse_result, chr_names):
        list_chr_names = list(chr_names)
        divided_by_chr = []
        for i in list_chr_names:
            name = i
            i = list()
            for j in range(len(parse_result)):
                if parse_result[j][0] == name:
                    i.append(parse_result[j])
                    divided_by_chr.append(i)
        return divided_by_chr

    def sort_by_chr(our_list):
        our_list.sort(key=lambda x: x[0])
        return our_list

    def sort_by_start(sorted_file):
        sorted_file.sort(key=lambda x: x[1])
        return sorted_file

    chr_names = set()
    for i in bed_entries:
        chr_names.add(i[0])
    result = divide(bed_entries, chr_names)
    sorted_by_start = []
    concatenated_list = []
    for i in result:
        sorted_by_start.append(sort_by_start(i))
    for i in sorted_by_start:
        concatenated_list += i
    chr_and_pos_sorted = sort_by_chr(concatenated_list)
    return chr_and_pos_sorted