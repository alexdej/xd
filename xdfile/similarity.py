#!/usr/bin/env python3


def grid_similarity(a, b):
    if len(a.grid) != len(b.grid) or len(a.grid[0]) != len(b.grid[0]):
        return 0

    r = 0
    tot = 0
    for row1, row2 in zip(a.grid, b.grid):
        for i in range(len(row1)):
            if row1[i] != '#':
                tot += 1
                if row1[i] == row2[i]:
                    r += 1

    astr = a.to_unicode()
    bstr = b.to_unicode()
    if astr == bstr:
        return 100

    return int(r * 100 / float(tot)) if tot else 0