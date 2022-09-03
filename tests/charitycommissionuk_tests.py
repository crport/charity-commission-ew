import unittest
import validators
from charitycommissionew import CharityCommissionEW

class CharityCommissionTestCase(unittest.TestCase):

    def setUp(self):
        self.ccew = CharityCommissionEW()

    def test_entity_exisits_good(self):

        self.assertTrue(self.ccew._entity_exists('charity'))

        self.assertFalse(self.ccew._entity_exists('ytirahc'))

    def test_gen_url(self):

        self.assertTrue(validators.url(self.ccew._gen_url(entity='charity', json=True)))

    def test_dict_output(self):
        result = self.ccew.to_dict(entity='charity')
        self.assertNotEqual(len(result), 0)
    
if __name__ == '__main__':
    unittest.main()