from data.connectdb import Database
import stock
from stock import Stock

stock.database = Database(host="localhost", database="test", user="postgres", password="postgres")

def test_basics():
    s = Stock("FR0000051732")
    s.load()
    assert s.nb == 80
    gap = abs((s.buy_price - s.last_price) / s.last_price)
    assert abs(gap - abs(s.buy_price_gap)) < 0.00001
    gap = abs((s.sell_price - s.last_price) / s.last_price)
    assert abs(gap - abs(s.sell_price_gap)) < 0.00001

    s.last_price = 10
    assert s.total_price == 800

def test_load_and_store():
    s1 = Stock("FR0000051732")
    s1.load()
    nb = s1.nb
    s1.nb = nb + 10
    s1.store()

    s2 = Stock("FR0000051732")
    s2.load()
    assert s2.nb == nb + 10
    s2.nb = nb
    s2.store()

    s1.load()
    assert s2.nb == nb
