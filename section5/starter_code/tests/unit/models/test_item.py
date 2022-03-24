from models.item import ItemModel
from unittest import TestCase

class TestItem(TestCase):

    def setUp(self):
        self.itemmodel = ItemModel('Farinha', 4.55)
    
    def test_ItemModel_json_method(self):
        expected_json_dict = {
            'name': 'Farinha',
            'price': 4.55
        }
        self.assertDictEqual(expected_json_dict, self.itemmodel.json())

    def test__create_ItemModel_correctly(self):
        expected_ItemModel_name = 'Farinha'
        expected_ItemModel_price = 4.55

        self.assertEqual(expected_ItemModel_name, self.itemmodel.name)
        self.assertEqual(expected_ItemModel_price, self.itemmodel.price)