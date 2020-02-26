from src.medianfilter import MedianFilter
from utils.extendedtestcase import ExtendedTestCase
from utils.errormessages import ErrorMessages as Em
import unittest


class FilterTestSuite(ExtendedTestCase):
    """Median Filter test cases."""

    def test_d_values(self):
        self.assertRaisesWithMessage(Em.DValueError, MedianFilter, 0)
        self.assertRaisesWithMessage(Em.DValueError, MedianFilter, 'hi')
        self.assertRaisesWithMessage(Em.DValueError, MedianFilter, 0.1)

    def test_invalid_scans(self):
        invalid_scan = ['a', 0.2, 10, 12, 15]
        invalid_scans = [['a', 0.2, 10, 12, 15], [3., 3., 3., 1., 3.]]
        median_filter = MedianFilter(3)

        self.assertRaisesWithMessage(Em.scanError, MedianFilter, 1, invalid_scan)
        self.assertRaisesWithMessage(Em.inputError, MedianFilter, 1, invalid_scans)
        self.assertRaisesWithMessage(Em.scanError, median_filter.update, invalid_scan[1])

    def test_valid_scans_without_history(self):
        valid_scans = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.],
                       [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
                       [10., 2., 4., 0., 0.]]
        median_filter = MedianFilter(3)

        self.assertEqual([0., 1., 2., 1., 3.], median_filter.update(valid_scans[0]))
        self.assertEqual([0.5, 3., 4.5, 1., 3.], median_filter.update(valid_scans[1]))
        self.assertEqual([1., 3., 4., 1., 3.], median_filter.update(valid_scans[2]))
        self.assertEqual([1.5, 3., 3.5, 1., 3.], median_filter.update(valid_scans[3]))
        self.assertEqual([2.5, 3., 4., 1., 1.5], median_filter.update(valid_scans[4]))

    def test_valid_scans_with_history(self):
        valid_scans = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.],
                       [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
                       [10., 2., 4., 0., 0.]]
        median_filter = MedianFilter(3, valid_scans[0:3])
        self.assertEqual([1.5, 3., 3.5, 1., 3.], median_filter.update(valid_scans[3]))
        self.assertEqual([2.5, 3., 4., 1., 1.5], median_filter.update(valid_scans[4]))


if __name__ == '__main__':
    unittest.main()
