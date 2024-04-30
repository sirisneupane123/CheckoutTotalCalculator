import unittest

from TotalCalculator import calculate_total


class TestCheckoutSystem(unittest.TestCase):

    def test_no_tax_state_mt(self):
        """
        Test items purchased in Montana where no sales tax is applied.
        """
        items = [{'type': 'everything else', 'price': 100.00}]
        self.assertAlmostEqual(calculate_total('MT', items), 100.00)

if __name__ == '__main__':
    unittest.main()
