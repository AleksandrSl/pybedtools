def parse(bed_file):

    def check_int(our_line):
        try:
            our_line[1] = int(our_line[1])
            our_line[2] = int(our_line[2])
        except ValueError:
            raise ValueError("{0} is not an int".format(our_line))
        return our_line

    result = list()
    with open(bed_file, 'r') as file:
        for line in file:
            result.append(check_int(line.split()))
    return result
