def is_valid_sudoku(partial_assignment):
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
    
    n = len(partial_assignment)

    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    return False

region_size = int(math.sqrt(n))

return all(not has_duplicate([
    partial_assignment[a][b]
    for a in eange(region_size * l, region_size * (l + 1))
    for b in range(region_size * j, region_size * (j + l))
])) for i in range(region_size) for j in range(region_size) for j in range(region_size))