def parse(bed_file):
    def int_error(our_int: str):
        if our_int.isdigit() is False:
            raise ValueError("{0} is not an int".format(our_int))
    def str_error(our_str: str):
        if isinstance(our_str, str) is False:
            raise ValueError("{0} is not a str".format(our_str))
    def check(our_line: list):
        str_error(our_line[0])
        int_error(our_line[1])
        int_error(our_line[2])
        if len(our_line) == 4:
            str_error(our_line[3])
        return our_line
    def convert(our_line: list):
        our_line[1] = int(our_line[1])
        our_line[2] = int(our_line[2])
        return our_line
    result = list(tuple())
    with open(bed_file, 'r') as file:
        for line in file:
            if 'description' not in line:
                result.append(convert(check(line.split()[0:-1])))
    return result