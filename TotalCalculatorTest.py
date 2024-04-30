import unittest

from TotalCalculator import calculate_total


class TestCheckoutSystem(unittest.TestCase):

    def test_no_tax_state_mt(self):
        """
        Test items purchased in Montana where no sales tax is applied.
        """
        items = [{'type': 'everything else', 'price': 100.00}]
        self.assertAlmostEqual(calculate_total('MT', items), 100.00)

    def test_normal_tax_id(self):
        """
        Test items purchased in Idaho with the standard tax rate applied.
        """
        items = [{'type': 'everything else', 'price': 100.00}]
        self.assertAlmostEqual(calculate_total('ID', items), 106.00)

    def test_tax_exempt_software_id(self):
        """
        Test purchasing software in Idaho, which is exempt from sales tax.
        """
        items = [{'type': 'Software', 'price': 200.00}]
        self.assertAlmostEqual(calculate_total('ID', items), 200.00)

    def test_high_tax_state_wa(self):
        """
        Test items purchased in Washington state with a high tax rate.
        """
        items = [{'type': 'everything else', 'price': 100.00}]
        self.assertAlmostEqual(calculate_total('WA', items), 109.38)


if __name__ == '__main__':
    unittest.main()
