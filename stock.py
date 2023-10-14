from data.connectdb import Database
import yfinance as yf
from termcolor import colored

import threading
import concurrent.futures
import time

MULTITHREADS = False

database = Database(host="localhost", database="pea_tomtom", user="postgres", password="postgres")

class Stock:
    def __init__(self, code = "") -> None:
        self.code = code
        self.name = ""
        self.currency = ""
        self.exchange = ""
        self.last_price = 0.01
        self.timestamp = None
        self.active = True
        self.nb = 0
        self.sell_price = 0.0
        self.buy_price = 0.0
        self.id = 0
    
    @property
    def total_price(self):
        return self.last_price*self.nb
    @property
    def buy_price_gap(self):
        if not self.buy_price:
            return -.999
        if self.last_price > 0:
            return self.buy_price / self.last_price -1
    @property
    def sell_price_gap(self):
        if not self.sell_price:
            return .999
        if self.last_price > 0:
            return self.sell_price / self.last_price - 1

    def __str__(self) -> str:
        return f"""{self.name:<20.20s} | {self.buy_price or 0:>7.2f} ({abs(self.buy_price_gap*100):>4.1f}%) | {self.last_price:>10.2f} | {self.sell_price or 0:>7.2f} ({abs(self.sell_price_gap*100):>4.1f}%) | {self.nb:>4} | {self.total_price:>7.2f}"""
        return f"""{self.code} | {self.name} | {self.currency} | {self.exchange} | {self.last_price} | {self.timestamp} | {self.active} | {self.nb} | {self.sell_price} | {self.buy_price} | {self.id}\n
            Total : {self.total_price} | Buy gap : {self.buy_price_gap} | Sell gap : {self.sell_price_gap}"""

    def load(self, data = None):
        tic = time.perf_counter()
        if data is None:
            cursor = database.conn.cursor()
            cursor.execute(f"""
                select code, name, currency, exchange, last_price, timestamp, active, nb, sell_price, buy_price, id 
                from stocks where code='{self.code}' and active=true
                """)
            s = cursor.fetchone()
            cursor.close()
        else:
            s = data
        
        if s is not None:
            self.code = s[0]
            self.name = s[1]
            self.currency = s[2]
            self.exchange = s[3]
            self.last_price = s[4]
            self.timestamp = s[5]
            self.active = s[6]
            self.nb = s[7]
            self.sell_price = s[8]
            self.buy_price = s[9]
            self.id = s[10]

        infos = yf.Ticker(self.code)
        self.currency = infos.basic_info.currency
        self.exchange = infos.basic_info.exchange
        self.last_price = infos.basic_info.last_price

        toc = time.perf_counter()
        print(f"{self.name} load time: {toc - tic:0.4f} seconds")

    def store(self):
        query = f"select count(*) from stocks where id={self.id}"
        cursor = database.conn.cursor()
        cursor.execute(query)
        if cursor.fetchone()[0] > 0:
            cursor.execute(f"""
                update stocks
                set 
                    code = '{self.code}',
                    name = '{self.name}',
                    currency = '{self.currency}',
                    exchange = '{self.exchange}',
                    last_price = {self.last_price},
                    timestamp = now(),
                    active = {self.active},
                    nb = {self.nb},
                    sell_price = {self.sell_price or "Null"},
                    buy_price = {self.buy_price or "Null"}
                where id={self.id}""")
        else:
            cursor.execute(f"""
                insert into stocks (code, name, currency, exchange, last_price, timestamp, active, nb, sell_price, buy_price)
                    VALUES ('{self.code}', '{self.name}', '{self.currency}', '{self.exchange}', {self.last_price},
                        now(), {self.active}, {self.nb}, {self.sell_price}, {self.buy_price})
            """)
        database.conn.commit()
        cursor.close()

def load_stocks(limit = None) -> list:
    stocks = []
    if not limit:
        query = """
                select code, name, currency, exchange, last_price, timestamp, active, nb, sell_price, buy_price, id, least(abs(buy_price / last_price -1), abs(sell_price / last_price - 1)) as gap
                from stocks where active=true and last_price > 0
                union
                select code, name, currency, exchange, last_price, timestamp, active, nb, sell_price, buy_price, id, 1 as gap
                from stocks where active=true and last_price is null or last_price = 0
                order by gap asc
            """
    else:
        query = f"""
                select code, name, currency, exchange, last_price, timestamp, active, nb, sell_price, buy_price, id, least(abs(buy_price / last_price -1), abs(sell_price / last_price - 1)) as gap, random() as rank
                from stocks where active=true and last_price > 0
                union
                select code, name, currency, exchange, last_price, timestamp, active, nb, sell_price, buy_price, id, 1 as gap, random() as rank
                from stocks where active=true and last_price is null or last_price = 0
                order by rank asc limit {limit}
            """

    cursor = database.conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    tic = time.perf_counter()

    if MULTITHREADS:
        threads = []
        for row in rows:
            s = Stock()
            t = threading.Thread(target=s.load, args=(row,))
            t.name =row[1]
            threads.append(t)
            t.start()
            stocks.append(s)

        for t in threads:
            t.join()
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for row in rows:
                s = Stock()
                stocks.append(s)
                futures.append(
                    executor.submit(s.load, row)
                )
    
    for s in stocks:
        s.store()

    toc = time.perf_counter()
    print(f"Total time: {toc - tic:0.4f} seconds")

    return stocks

def init():
    s = ["FR0010220475","FR0013412012","FR0013412269","FR0014003U94","FR0000074148","FR0010425595","FR0013426004","FR0010386334","FR0000053381","FR0011950732","FR0000035818","FR0004163111","FR0004024222","IE00B53L3W79","FR0011440478","FR0011871128","IT0004965148","FR0010112524","FR0014005HJ9","FR0013154002","FR0010282822","FR0000130809","FR0013227113","FR0000051807","FR0000033003","FR0005691656","FR0000054470","FR0013506730","FR0000031577","FR0000127771","FR0011981968","FR001400AEJ2"]
    for _ in s:
        stock = Stock(_)
        stock.load()
        print(stock)
        stock.store()


if __name__ == "__main__":
#    init()
    # stock = Stock("FR0000051732")
    # stock.load()
    # print(stock)
    # stock.store()

    stocks = load_stocks()
    print(f"""{"Name":<20.20s} | buy_price       | Last_price | sell_price      | nb   | total_price""")
    print("-" * 100)
    for s in stocks:
        if s.buy_price_gap and s.buy_price_gap > -0.05:
            print(colored(s, "red"))
        elif s.sell_price_gap and s.sell_price_gap < 0.05:
            print(colored(s, "green"))
        else:
            print(s)