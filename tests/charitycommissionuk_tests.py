import unittest
import validators
from charitycommissionEW import CharityCommissionEW

class CharityCommissionTestCase(unittest.TestCase):

    def setUp(self):
        self.ccuk = CharityCommissionEW()

    def test_entity_exisits_good(self):

        self.assertTrue(self.ccuk._entity_exists('charity'))

        self.assertFalse(self.ccuk._entity_exists('ytirahc'))

        self.assertTrue(self.ccuk._entity_exists('ChArItY'))

    def test_gen_url(self):

        self.assertTrue(validators.url(self.ccuk._gen_url(entity='charity', json=True)))

    def test_dict_output(self):
        result = self.ccuk.to_dict(entity='charity')
        self.assertNotEqual(len(result), 0)
    
if __name__ == '__main__':
    unittest.main()