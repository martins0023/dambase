import os
from itertools import zip_longest, chain
from time import time
def cross_product(v1, v2):
    return [w1 + w2 for w1 in v1  for w2 in v2]

def chunk(iterable, n, fillvalue=None):
    args = (iter(iterable)) * n 
    return zip_longest(*args, fillvalue=fillvalue)

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross_product(rows, cols)
all_units = (
    [cross_product(rows, c) for c in cols]
    + [cross_product(r, cols) for r in rows]
    + [cross_product(rs, cs)
       for rs in chunk(rows, 3) for cs in chunk(cols, 3)]
)
units = dict(
    (square, [unit for unit in all_units if square in unit])
    for square in squares
)
peers = dict(
    (square, set(chain(*units[square])) - set([square]))
    for square in squares
)

def parse_puzzle(puzzles):
    assert set(puzzle) <= set ('.0123456789')
    assert len(puzzle) == 81
    
    grid = dict((square, digits) for square in squares)
    for square, digit in zip(squares, puzzle):
        if digit in digits and not place(grid, square, digit):
            return False
        return grid
    
def solve(puzzle):
    grid = parse_puzzle(puzzle)
    return search(grid)

def search(grid):
    if not grid:
        return False
    if all(len(grid[square]) == 1 for square in squares):
        return grid
    values, square = min(
        (len(grid[square]), square) for square in squares
        if len(grid[square]) > 1
    )
    for digit in grid[square]:
        result = search(place(grid.copy(), square, digit))
        if result:
            return result
        
def place(grid, square, digit):
    """Eliminate all the other values (except digit) from
    grid[square] and propagate.
    Return grid, or Flase if a contradiction is detected.
    """
    other_vals = grid[square].replace(digit, '')
    if all(eliminate(grid, square, val) for val in other_vals):
        return grid
    return False
def eliminate(grid, square, digit):
    """Eliminate digit from grid[square]. Propagate when candidates
    are <= 2.
    Return grid, or False if a contradiction is detected.
    """
    if digit not in grid[square]:
        return grid # already eliminated
    grid[square] = grid[square].replace(digit, '')
    
    ## (1) If a square is reduced to one value, eliminate value
    ## from peers.
    
    if len(grid[square]) == 0:
        return False # nothing left to place here, wrong solution
    elif len(grid[square]) == 1:
        value = grid[square]
        
        if not all(
            eliminate(grid, peer, value) for peer in peers[square]
            ):
            
            return False
        ## (2) If a unit is reduced to only one place for a value,
        ## then put it there.
        
        for unit in units[square]:
            places = [sqr for sqr in unit if digit in grid[sqr]]
            
            if len(places) == 0:
                return False # No place for this value
            elif len(places) == 1:
                # digit can only be in one place in unit,
                # assign it there
                if not place(grid, places[0], digit):
                    return False
                return grid