import unittest
from city_functions import city_country

class TestCitycountry(unittest.TestCase):

    def test_city_country(self):
        result = city_country("London", "England")
        self.assertEqual(result, "London, England")

if __name__ == "__main__":
    unittest.main()