#######################################
# LIDAR Median Filtering
# Authored by: Manoj Madabhushi
#######################################
import numpy as np
from collections import deque
from collections import defaultdict
from utils.errormessages import ErrorMessages as Em


def is_valid_scan(scan):
    if not isinstance(scan, list):
        raise Exception(Em.scanError)


def is_valid_input(input):
    if not isinstance(input, (int, float)):
        raise Exception(Em.inputError)


class MedianFilter:

    def __init__(self, d, data=None):

        if not (isinstance(d, int)) or d <= 0:
            raise Exception(Em.DValueError)

        self.d = d + 1
        self.dic = defaultdict(deque)
        if data:
            self.__add_data(data)

    # Helper function to add data to the dictionary to apply median on future scans
    def __add_data(self, data):
        is_valid_scan(data)

        # Narrowing down the data needed for this filter instance
        if len(data) > self.d:
            data = data[len(data) - self.d + 1:]

        for dat in data:
            is_valid_scan(dat)
            for i, val in enumerate(dat):
                is_valid_input(val)
                self.dic[i].append(val)

    # Function to apply median filter
    def update(self, scan):
        is_valid_scan(scan)
        if 0 < len(self.dic) != len(scan):
            raise Exception(Em.scanError)
        for i, num in enumerate(scan):
            is_valid_input(num)

            # Sliding values in dictionary of deques if length of deque exceeds D
            if len(self.dic[i]) == self.d:
                self.dic[i].popleft()
            self.dic[i].append(num)
        result = [None] * len(scan)
        # Applying median filter
        for key in self.dic.keys():
            result[key] = np.median(self.dic[key])
        return result
