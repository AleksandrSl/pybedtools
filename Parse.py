def parse(bed_file):

    def check(our_line: list):
        try:
            our_line[1] = int(our_line[1])
            our_line[2] = int(our_line[2])
        except ValueError:
            raise ValueError("{0} is not an int".format(our_line))
        return our_line

    result = list(tuple())
    with open(bed_file, 'r') as file:
        for line in file:
            result.append(check(line.split()[0:-1]))
    return result
