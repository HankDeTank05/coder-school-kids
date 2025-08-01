
'''
1. point to compare
2. range min
3. range max
'''

def number_in_range(num: int | float, range_min: int | float, range_max: int | float) -> bool:
    return range_min <= num <= range_max