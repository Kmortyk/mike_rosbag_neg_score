from unittest import TestCase
import numpy as np


class Test(TestCase):
    def test_point_reward(self):
        print(100 * np.log(1 - 0.1/np.sqrt(0.09)))
