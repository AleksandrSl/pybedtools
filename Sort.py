ort(bed_file):
    def check(our_line):
        try:
            our_line[1] = int(our_line[1])
            our_line[2] = int(our_line[2])
        except ValueError:
            raise ValueError("{0} is not an int".format(our_line))
        return our_line
    
    def divide(sorted_file, chr_names):
        list_chr_names = list(chr_names)
        result = []
        for i in list_chr_names:
            name = i
            i = list()
            for j in range(len(sorted_file)):
                if sorted_file[j][0] == name:
                    i.append(sorted_file[j])
            result.append(i)
        return result
    
    def sort_by_chr(our_list):
        our_list.sort(key=lambda x: x[0])
        return our_list
    
    def sort_by_start(sorted_file):
        sorted_file.sort(key=lambda x: x[1])
        return sorted_file
    
    result = list()
    chr_names = set()
    with open(bed_file, 'r') as file:
        for line in file:
            result.append(check(line.split()))
            chr_names.add(line.split()[0])
    result = divide(result, chr_names)
    sorted_by_start = []
    concatenated_list = []
    for i in result:
        sorted_by_start.append(sort_by_start(i))
    for i in sorted_by_start:
        concatenated_list += i
    chr_and_pos_sorted = sort_by_chr(concatenated_list)
    return chr_and_pos_sorted
