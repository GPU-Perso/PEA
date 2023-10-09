import unittest
from data.connectdb import Database
import stock
from stock import Stock

stock.database = Database(host="localhost", database="test", user="postgres", password="postgres")

class TestStock(unittest.TestCase):
    def test_basics(self):
        s = Stock("FR0000051732")
        s.load()
        self.assertEqual(s.nb, 80)
        gap = abs((s.buy_price - s.last_price) / s.last_price)
        self.assertAlmostEqual(gap, abs(s.buy_price_gap))
        gap = abs((s.sell_price - s.last_price) / s.last_price)
        self.assertAlmostEqual(gap, abs(s.sell_price_gap))

        s.last_price = 10
        self.assertEqual(s.total_price, 800)

    def test_store(self):
        s = Stock("FR0000051732")
        s.load()
        s.nb = 1
        s.store()

        s2 = Stock("FR0000051732")
        s2.load()
        self.assertEqual(s2.nb, 1)
        s2.nb = 80
        s2.store()

if __name__ == '__main__':
    unittest.main()