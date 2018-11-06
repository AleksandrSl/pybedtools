def parsing_bed(bed_file):
    def check_int(line):
        try:
            line[1], line[2] = int(line[1]), int(line[2])
        except ValueError:
            raise ValueError("Program expects starting and "
                             "ending positions to be valid "
                             "numbers (integer). Check line: {} "
                             .format(' '.join(line)))
        return line

    def check_len(line):
        try:
            line[2]
        except IndexError:
            raise IndexError("Program expects each line to "
                             "have chromosome name, starting "
                             "and ending position. Check line: {} "
                             .format(' '.join(line)))
        return line

    parsed_data = list()
    with open(bed_file) as input_handle:
        for line in input_handle:
            line_elements = line.split()
            # Ignore annotation lines.
            if any(el in line_elements for el in ("#", "browser", "track")):
                continue
            check_len(line_elements)
            check_int(line_elements)
            parsed_data.append(tuple(line_elements[0:5]))
        return parsed_data
