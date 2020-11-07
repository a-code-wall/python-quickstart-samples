import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		first_name = 'blue'
		last_name = 'sky'
		salary = 1000
		self.employee = Employee(first_name, last_name, salary)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(1000, self.employee.salary)

	def test_give_custom_raise(self):
		self.employee.give_raise(5000)
		self.assertEqual(6000, self.employee.salary)

unittest.main()