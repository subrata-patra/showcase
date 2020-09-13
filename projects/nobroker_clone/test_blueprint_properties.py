import unittest
import blueprint_properties as bp


class BlueprintProperties(unittest.TestCase):
    def test_properties_details_create(self):

        with self.assertRaises(TypeError):
            bp.properties_details_create()


if __name__ == '__main__':
    unittest.main()
