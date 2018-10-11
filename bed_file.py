import sys

def bed_parser(bfile):
    output_data = []
    with open(bfile) as bed_data:
        for line in bed_data.input():
                try:
                   line = bed_data.stdin.readline()
                if not line:
                    break
            return
        for line in bed_data.input():
            if len(bed_data) < 3:
                break
             else:
                continue
        for element in range(len(bed_data)):
            output_data.append(turple(element[0:5]))
    return output_data
