from unittest import TestCase

from ..cross_field_warnings_validator import CrossFieldWarningsValidator

class DrainageTestCase(TestCase):

    def setUp(self):
        self.validator = CrossFieldWarningsValidator()

    def test_equal_areas(self):
        self.assertFalse(self.validator.validate({'drainageArea': '1000', 'contributingDrainageArea': '1000'}, {}))
        self.assertFalse(self.validator.validate({'drainageArea': '1000', 'contributingDrainageArea': '1000'}, {}))


    def test_unequal_areas(self):
        self.assertTrue(self.validator.validate({'drainageArea': '999', 'contributingDrainageArea': '1000'}, {}))
        self.assertTrue(self.validator.validate({'drainageArea': '1000', 'contributingDrainageArea': '999'}, {}))