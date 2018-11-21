def sort(bed_entries: list):
    return sorted(bed_entries, key=lambda x: (x[0], x[1]))
