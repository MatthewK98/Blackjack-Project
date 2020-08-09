import unittest

from Blackjack import score


class TestScore(unittest.TestCase):
	def test_below_21(self):
		hand = ["8", "3", "2"]
		total = score(hand)

		self.assertEqual(total, 13)

	def test_above_21(self):
		hand = ["8", "10", "4"]
		total = score(hand)

		self.assertEqual(total, 22)

	def test_ace_below_21(self):
		hand = ["Ace", "2", "2"]
		total = score(hand)

		self.assertEqual(total, 15)

	def test_ace_is_one(self):
		hand = ["Ace", "10", "2"]
		total = score(hand)

		self.assertEqual(total, 13)

	def test_two_ace(self):
		hand = ["Ace", "Ace"]
		total = score(hand)

		self.assertEqual(total, 12)

	def test_two_ace_countasone(self):
		hand = ["Ace", "Ace","10"]
		total = score(hand)

		self.assertEqual(total, 12)

	def test_ace_and_bust(self):
		hand = ["Ace", "Ace","Ace","King","Queen"]
		total = score(hand)

		self.assertEqual(total, 23)

if __name__ == '__main__':
	unittest.main()