# 城市和国家
import unittest
from city_functions import city_country

# class cityCountryTestCase(unittest.TestCase):
# 	def test_city_country(self):
# 		full_name = city_country('santiago', 'chile')
# 		self.assertEqual(full_name, 'Santiago, Chile')

# unittest.main()

# 人口数量
class cityCountryTestCase(unittest.TestCase):
	def test_city_country(self):
		full_name = city_country('santiago', 'chile')
		self.assertEqual(full_name, 'Santiago, Chile')
		full_name = city_country('santiago', 'chile', 50000)
		self.assertEqual(full_name, 'Santiago, Chile - Population 50000')

	def test_city_country_population(self):
		full_name = city_country('santiago', 'chile', 5000000)
		self.assertEqual(full_name, 'Santiago, Chile - Population 5000000')

unittest.main()
