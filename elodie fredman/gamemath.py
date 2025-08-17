import math

def circle_overlap( x1, y1, r1, x2, y2, r2) -> bool:
    distance: float = math.hypot(x1 - x2, y1 - y2)
    overlap : bool = distance < r1 + r2
    return overlap
