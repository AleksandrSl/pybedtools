import sys


def parsing_bed(bed_file):
    parsed_data = list()
    with open(bed_file) as input_handle:
        for line in input_handle:
            line_elements = line.split()
            # Ignore annotation lines.
            if any(i in line_elements for i in ("#", "browser", "track")):
                continue
            # Check if a non-annotation line if valid.
            elif len(line_elements) < 3:
                sys.exit("Program expects a valid BED file with at least 3 columns (chromosome, start and end).\n"
                         "Problem in line: %s" % line)
            elif not (line_elements[1].isdigit() and line_elements[2].isdigit()):
                sys.exit("Program expects starting and ending positions to be valid numbers (integer).\n"
                         "Problem in line: %s" % line)
            # End of check
            else:
                # Give "None" name if file is BED3 or doesn't contain name option for other BED types.
                if len(line_elements) == 3 or line_elements[3].isdigit():
                    line_elements.insert(3, "None")
                # Covert start and end parameters to int.
                for i in [1, 2]:
                    line_elements[i] = int(line_elements[i])
                parsed_data.append(tuple(line_elements[0:5]))
        return parsed_data
