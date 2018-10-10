def parsing(bed_file):
    def int_error(our_int: str):
        if our_int.isdigit() is False:
            raise ValueError("{0} is not a integer".format(our_int))
    def str_error(our_str: str):
        if isinstance(our_str, str) is False:
            raise ValueError("{0} is not a integer".format(our_str))
    def checking(our_line: list):
        str_error(our_line[0])
        int_error(our_line[1])
        int_error(our_line[2])
        try:
            str_error(our_line[3])
        except IndexError:
            pass
    result = list(tuple())
    with open(bed_file, 'r') as file:
        for line in file:
            if 'description' not in line:
                checking(line.split()[0:-1])
                result.append(line.split()[0:-1])
    return result