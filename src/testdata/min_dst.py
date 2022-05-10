import math

def dst(x1, y1, x2, y2) -> float:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

class MinDistance:
    def __init__(self, min_dst):
        self.min_dst = min_dst
        self.ps = []

    def add_point(self, x, y) -> bool:
        for p in self.ps:
            if dst(p[0], p[1], x, y) < self.min_dst:
                return False
        self.ps.append([x, y])
        return True

    def clear(self):
        self.ps.clear()
