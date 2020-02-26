from src.rangefilter import RangeFilter
from utils.extendedtestcase import ExtendedTestCase
from utils.errormessages import ErrorMessages as Em
import unittest


class FilterTestSuite(ExtendedTestCase):
    """Range Filter test cases."""

    def test_invalid_range(self):
        self.assertRaisesWithMessage(Em.RangeValueError, RangeFilter, 'hi', 0.2)
        self.assertRaisesWithMessage(Em.MaxMinConstraint, RangeFilter, 0.3, 0.2)

    def test_invalid_scans(self):
        invalid_scan = [['a', 0.2, 10, 12, 15], 1]
        range_filter = RangeFilter(0, 10)

        self.assertRaisesWithMessage(Em.inputError, range_filter.update, invalid_scan[0])
        self.assertRaisesWithMessage(Em.scanError, range_filter.update, invalid_scan[1])
        self.assertRaisesWithMessage(Em.inputError, range_filter.update, invalid_scan)

    def test_valid_scans(self):
        range_filter = RangeFilter(0, 10)
        valid_scans = [[-1., 51., 77., 45., -30.], [0., 1., 2., 1., 3.]]

        self.assertEqual([0., 1., 2., 1., 3.], range_filter.update(valid_scans[1]))
        self.assertEqual([0., 10., 10., 10., 0.], range_filter.update(valid_scans[0]))


if __name__ == '__main__':
    unittest.main()
