"""
DROP TABLE public.stocks;

CREATE TABLE public.stocks (
	code varchar NOT NULL,
	"name" varchar NULL,
	last_price float4 NULL DEFAULT 0.0,
	nb int2 NULL DEFAULT 0,
	sell_price float4 NULL DEFAULT 0.0,
	buy_price float4 NULL DEFAULT 0.0,
	currency varchar NULL,
	exchange varchar NULL,
	"timestamp" timestamp NULL DEFAULT now(),
	active bool NOT NULL DEFAULT true,
	id serial4 NOT NULL,
	CONSTRAINT stocks_pk PRIMARY KEY (id)
);

INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0010220475', 'ALSTOM', 13.06, 53, 18.08, 10.42, 'EUR', 'PAR', '2023-10-09 10:19:40.898', true, 39);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0013412012', 'AMUNDI ETF PEA MSCI EMERGING ASIA UCITS ETF - EUR', 21.078, 27, 23.74, 19.35, 'EUR', 'PAR', '2023-10-09 10:19:33.110', true, 40);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0013412269', 'AMUNDI ETF PEA NASDAQ-100 UCITS ETF - EUR', 41.641, 11, 43.69, 36.9, 'EUR', 'PAR', '2023-10-09 10:19:31.494', true, 41);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0014003U94', 'ARAMIS GROUP', 3.915, 159, 4.53, 3.07, 'EUR', 'PAR', '2023-10-09 10:19:38.264', true, 42);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000074148', 'ASSYSTEM', 38.0, 9, 51.29, 37.17, 'EUR', 'PAR', '2023-10-09 10:19:30.034', true, 43);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000051732', 'ATOS', 5.122, 80, 9.63, 4.6, 'EUR', 'PAR', '2023-10-09 10:19:34.143', true, 3);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000035164', 'BENETEAU', 11.68, 24, 14.76, 10.21, 'EUR', 'PAR', '2023-10-09 10:19:36.055', true, 6);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0010425595', 'CELLECTIS', 1.3, 509, 1.87, 1.07, 'EUR', 'PAR', '2023-10-09 10:19:39.727', true, 44);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0013426004', 'CLARANOVA', 1.466, 1026, 1.8, NULL, 'EUR', 'PAR', '2023-10-09 10:19:42.323', true, 5);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0010386334', 'ClARIANE', 5.105, 92, 6.83, 4.48, 'EUR', 'PAR', '2023-10-09 10:19:35.356', true, 46);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000053381', 'DERICHEBOURG', 4.396, 90, 5.93, 3.83, 'EUR', 'PAR', '2023-10-09 10:19:36.875', true, 47);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0011950732', 'ELIOR GROUP', 1.65, 285, 2.55, 1.41, 'EUR', 'PAR', '2023-10-09 10:19:37.573', true, 48);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000035818', 'ESKER', 122.0, 3, 166.46, 102.59, 'EUR', 'PAR', '2023-10-09 10:19:38.621', true, 49);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0004163111', 'GENFIT', 3.115, 135, 4.81, 2.41, 'EUR', 'PAR', '2023-10-09 10:19:42.846', true, 50);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0004024222', 'INTERPARFUMS', 50.2, 3, 69.08, 44.04, 'EUR', 'PAR', '2023-10-09 10:19:35.752', true, 51);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('IE00B53L3W79', 'ISHR ESTX50 B A', 147.58, 5, 170.07, 143.6, 'EUR', 'EBS', '2023-10-09 10:19:30.766', true, 52);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0011440478', 'LYXOR MSCI EMERGING MARKETS C-EUR', 14.573, 42, 16.54, 13.48, 'EUR', 'PAR', '2023-10-09 10:19:32.435', true, 53);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0011871128', 'LYXOR SP500 PEA', 34.784, 30, 38.59, 32.53, 'EUR', 'PAR', '2023-10-09 10:19:31.814', true, 54);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('IT0004965148', 'MONCLER N', 54.78, 5, 77.76, 42.9, 'EUR', 'MIL', '2023-10-09 10:19:41.828', true, 55);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0010112524', 'NEXITY', 13.1, 40, 19.41, 12.68, 'EUR', 'PAR', '2023-10-09 10:19:31.151', true, 56);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0014005HJ9', 'OVHCLOUD', 7.445, 50, 10.17, 6.49, 'EUR', 'PAR', '2023-10-09 10:19:36.400', true, 57);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR001400AEJ2', 'PEA PROFILE DYNAMIQUE C', 101.9, 27, 108.73, 93.02, 'EUR', 'FRA', '2023-10-09 10:19:32.077', true, 70);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0013154002', 'SARTORIUS STEDIM BIOTECH', 227.0, 2, 330.91, 203.45, 'EUR', 'PAR', '2023-10-09 10:19:34.562', true, 58);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0010282822', 'SES IMAGOTAG', 113.0, 3, 181.79, 102.72, 'EUR', 'PAR', '2023-10-09 10:19:33.808', true, 59);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000130809', 'SOCIETE GENERALE', 22.375, 5, 27.48, 20.64, 'EUR', 'PAR', '2023-10-09 10:19:32.795', true, 60);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0013227113', 'SOITEC', 154.5, 4, 203.82, 134.52, 'EUR', 'PAR', '2023-10-09 10:19:37.247', true, 61);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000051807', 'TELEPERFORMANCE', 117.35, 3, 189.16, 96.85, 'EUR', 'PAR', '2023-10-09 10:19:39.386', true, 62);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000033003', 'TOUAX', 4.18, 72, 7.19, 3.8, 'EUR', 'PAR', '2023-10-09 10:19:33.495', true, 63);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0005691656', 'TRIGANO', 129.7, 3, 156.89, 105.05, 'EUR', 'PAR', '2023-10-09 10:19:40.124', true, 64);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000054470', 'UBISOFT ENTERTAIN.', 28.68, 8, 32.88, 15.62, 'EUR', 'PAR', '2023-10-09 10:19:37.896', true, 65);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0013506730', 'VALLOUREC', 10.74, 38, 14.87, 8.69, 'EUR', 'PAR', '2023-10-09 10:19:40.509', true, 66);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000031577', 'VIRBAC', 259.0, 1, 350.0, 206.04, 'EUR', 'PAR', '2023-10-09 10:19:41.352', true, 67);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0000127771', 'VIVENDI SE', 8.292, 22, 11.03, 7.31, 'EUR', 'PAR', '2023-10-09 10:19:35.011', true, 68);
INSERT INTO public.stocks
(code, "name", last_price, nb, sell_price, buy_price, currency, exchange, "timestamp", active, id)
VALUES('FR0011981968', 'WORLDLINE', 24.49, 21, 38.53, 20.29, 'EUR', 'PAR', '2023-10-09 10:19:38.944', true, 69); 
"""

import unittest
from connectdb import Database

class TestDatabase(unittest.TestCase):
    def test_connection(self):
        database = Database(host="localhost", database="test", user="postgres", password="postgres")
        cursor = database.conn.cursor()
        self.assertIsNotNone(cursor)
        cursor.execute("select * from stocks limit 1")
        data = cursor.fetchall()
        self.assertEqual(len(data), 1)
        cursor.close()

    def test_content(self):
        database = Database(host="localhost", database="test", user="postgres", password="postgres")
        cursor = database.conn.cursor()
        self.assertIsNotNone(cursor)
        cursor.execute("select count(*) from stocks")
        data = cursor.fetchall()
        self.assertEqual(data[0][0], 34)

        cursor.execute("select * from stocks limit 1")
        data = cursor.fetchall()
        self.assertEqual(len(data[0]), 11)
        cursor.close()

if __name__ == '__main__':
    unittest.main()