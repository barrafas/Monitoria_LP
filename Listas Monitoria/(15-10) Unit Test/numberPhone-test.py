import unittest
from numbers_phone import number_phone_br

class MyTestCase(unittest.TestCase):
	def test_number_DDD(self):
		self.number = 21998765432
		expected = 21998765432
		#Act
		actual = number_phone_br(self.number)
        # Assert
		self.assertAlmostEqual(expected, actual)

	def test_string_DDD(self):
		self.number = "21998765432"
		expected = 21998765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)
	
	def test_string_symbols_DDD(self):
		self.number = "(21) 99876-5432"
		expected = 21998765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)

	def test_string_symbols(self):
		self.number = "99876-5432"
		expected = 21998765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)

	def test_string_international_symbols(self):
		self.number = "+55 (21) 99876-5432"
		expected = 21998765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)

	def test_number_no_cellphone(self):
		self.number = 2198765432
		expected = 2198765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)

	def test_no_cellphone(self):
		self.number = "(21) 9876-5432"
		expected = 2198765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)

	def test_no_cellphone_international_DDD(self):
		self.number = "+55 (21) 9876-5432"
		expected = 2198765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)
	
	def test_no_cellphone_international_DDD(self):
		self.number = "+55 2198765432"
		expected = 2198765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)

	def test_international_DDD_space(self):
		self.number = "+55 21 99876 5432"
		expected = 21998765432
		# Act
		actual = number_phone_br(self.number)
		# Assert
		self.assertAlmostEqual(expected, actual)
	
	