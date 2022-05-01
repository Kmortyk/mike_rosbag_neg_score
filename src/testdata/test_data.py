import math
from abc import ABC, abstractmethod
from typing import List, Tuple

from src.testdata.layered_list import LayeredList


class TestData(ABC):
    @abstractmethod
    def xy_data(self) -> Tuple[List[float], List[float]]:
        pass

    def laser_scan_data(self) -> List[List[float]]:
        xs, ys = self.xy_data()
        lst = LayeredList()

        for x, y in zip(xs, ys):
            r = math.sqrt(x**2 + y**2)
            phi = int(2*math.degrees(math.atan2(y, x)))

            if phi < 0:
                phi += 360*2

            lst[phi] = r

        return lst.get_lists()
