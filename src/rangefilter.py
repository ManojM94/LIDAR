#######################################
# LIDAR Range Filtering
# Authored by: Manoj Madabhushi
#######################################

from utils.errormessages import ErrorMessages as Em


def is_valid_scan(scan):
    if not isinstance(scan, list):
        raise Exception(Em.scanError)


def is_valid_input(inp):
    if not isinstance(inp, (int, float)):
        raise Exception(Em.inputError)


class RangeFilter():
    def __init__(self, range_min=0.03, range_max=50):

        # Validating input range min and max values
        if not (isinstance(range_max, (int, float)) and isinstance(range_min, (int, float))):
            raise Exception(Em.RangeValueError)
        if range_min > range_max:
            raise Exception(Em.MaxMinConstraint)

        self.range_max = range_max
        self.range_min = range_min

    def update(self, scan):
        is_valid_scan(scan)
        result = [None]*len(scan)
        for i in range(len(scan)):
            is_valid_input(scan[i])

            if scan[i] > self.range_max:
                result[i] = self.range_max
            elif scan[i] < self.range_min:
                result[i] = self.range_min
            else:
                result[i] = scan[i]
        return result
