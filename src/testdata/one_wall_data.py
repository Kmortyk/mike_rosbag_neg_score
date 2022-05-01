from typing import Tuple, List

from src.testdata.test_data import TestData


class BoxData(TestData):
    def __init__(self,
                 size=1., offset_x=0., offset_y=0,
                 left=True, right=True, top=True, bottom=True):
        self.size = size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def xy_data(self) -> Tuple[List[float], List[float]]:
        xs, ys = [], []
        ox, oy = self.offset_x, self.offset_y
        sz = self.size

        if self.top:
            xs.extend([ox - sz, ox - sz/2, ox, ox + sz/2, ox + sz])
            ys.extend([oy - sz, oy - sz, oy - sz, oy - sz, oy - sz])
        if self.bottom:
            xs.extend([ox - sz, ox - sz/2, ox, ox + sz/2, ox + sz])
            ys.extend([oy + sz, oy + sz, oy + sz, oy + sz, oy + sz])
        if self.left:
            xs.extend([ox - sz, ox - sz, ox - sz, ox - sz, ox - sz])
            ys.extend([oy - sz, oy - sz/2, oy, oy + sz/2, oy + sz])
        if self.right:
            xs.extend([ox + sz, ox + sz, ox + sz, ox + sz, ox + sz])
            ys.extend([oy - sz, oy - sz/2, oy, oy + sz/2, oy + sz])

        return xs, ys
