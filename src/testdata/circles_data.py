import math
from typing import Tuple, List

import numpy as np

from src.testdata.test_data import TestData


class CirclesData(TestData):
    def __init__(self,
                 start_layer=0, end_layer=10, step_layer=3, layer_size=0.07,
                 start_hangle=0, end_hangle=720, step_hangle=30):
        self.start_layer = start_layer
        self.end_layer = end_layer
        self.step_layer = step_layer
        self.layer_size = layer_size
        self.start_hangle = start_hangle
        self.end_hangle = end_hangle
        self.step_hangle = step_hangle

    def xy_data(self) -> Tuple[List[float], List[float]]:
        xs, ys = [], []

        for layer in np.arange(self.start_layer, self.end_layer, self.step_layer):
            for phi in range(self.start_hangle, self.end_hangle, self.step_hangle):
                r = self.layer_size * layer

                x = r * math.cos(math.radians(phi / 2))
                y = r * math.sin(math.radians(phi / 2))

                xs.append(x)
                ys.append(y)

        return xs, ys
