from typing import List


class LayeredList:
    def __init__(self, inner_size=720):
        self.lists = []
        self.size = 0
        self.inner_size = inner_size

    def __add_list(self):
        self.lists.append([0.]*self.inner_size)
        self.size += 1

    def __setitem__(self, key, value):
        if self.size == 0:
            self.__add_list()
            self.lists[0][key] = value

        layer = 0

        while True:
            if self.lists[layer][key] == 0:
                self.lists[layer][key] = value
                return

            if layer == self.size - 1:
                self.__add_list()

            layer += 1

    def get_lists(self) -> List[List[float]]:
        return self.lists
