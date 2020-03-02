import unittest
from ConfigurationParse import ConfigurationParser

class TestParse(unittest.TestCase):

    # def test_parse_suct_name(self):
    #     cp = ConfigurationParser()
    #     expected_name = ['CUSTOMER_A', 'CUSTOMER_B']
    #     parse_names = cp.parseCustomerName()
    #     self.assertAlmostEqual(list, type(parse_names))
    #     self.assertAlmostEqual(expected_name, parse_names)

    def test_parse_cust_vlan(self):
        cp = ConfigurationParser()
        customer_name = "CUSTOMER_A"
        expected_vlan = 100
        parsed_vlan = cp.parseCustomerVlan(customer_name)
        self.assertEqual(expected_vlan, parsed_vlan)