import sys
import utils.ui_utils as ui_utils
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QBoxLayout, QHBoxLayout, QVBoxLayout, QWidget,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QPushButton
)
from PySide2.QtCore import Qt
import stock

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("PEA")
        self.setup_ui()
        self.setup_css()

        self.stocks_layout = {}

        self.show_all_stocks()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        layout = QHBoxLayout()
        self.main_layout.addLayout(layout)
        widget = QWidget()
        widget.setStyleSheet("""font-weight: bold;
        """)
        layout.addWidget(widget)

        self.header = QHBoxLayout()
        widget.setLayout(self.header)
        self.header.addWidget(ui_utils.create_label(text="Name", width=200))
        self.header.addWidget(ui_utils.create_label(text="Buy price", width=80))
        self.header.addWidget(ui_utils.create_label(text="Buy gap", width=80))
        self.header.addWidget(ui_utils.create_label(text="Last price", width=80))
        self.header.addWidget(ui_utils.create_label(text="Sell price", width=80))
        self.header.addWidget(ui_utils.create_label(text="Sell gap", width=80))
        self.header.addWidget(ui_utils.create_label(text="Nb", width=50))
        self.header.addWidget(ui_utils.create_label(text="Total price", width=100))

        self.btn_show_all_stocks = QPushButton("Reload")
        self.btn_show_all_stocks.setFixedWidth(100)
        self.btn_show_all_stocks.clicked.connect(self.show_all_stocks)    
        self.header.addWidget(self.btn_show_all_stocks)

    def setup_css(self):
        self.setStyleSheet("""
        """)

    def show_all_stocks(self):
        self.stocks = stock.load_stocks()

        for s in self.stocks:
            l = self.stocks_layout.get(s.code)
            if l:
                ui_utils.clear_layout(l)
                self.main_layout.removeItem(l)
            
            # line container
            self.stocks_layout[s.code] = stock_line = QHBoxLayout()
            self.main_layout.addLayout(stock_line)

            # create widgets
            # Name | Buy price | Buy price gap | Last price | Sell price | Sell price gap | Nb | Total price | Reload
            self.stocks_layout[s.code+"_label_name"] = ui_utils.create_label(text=s.name, width=200)
            stock_line.addWidget(self.stocks_layout[s.code+"_label_name"])

            self.stocks_layout[s.code+"_label_buy_price"] = ui_utils.create_label(text=s.buy_price, width=80, alignment=Qt.AlignRight, format=":.2f")
            stock_line.addWidget(self.stocks_layout[s.code+"_label_buy_price"])

            self.stocks_layout[s.code+"_label_buy_price_gap"] = ui_utils.create_label(text=f"{s.buy_price_gap*100:.2f}%", width=80, alignment=Qt.AlignRight)
            stock_line.addWidget(self.stocks_layout[s.code+"_label_buy_price_gap"])
            ui_utils.colorize_label(self.stocks_layout[s.code+"_label_buy_price_gap"], value=s.buy_price_gap, max=-0.05, color="red")

            self.stocks_layout[s.code+"_label_last_price"] = ui_utils.create_label(text=str(s.last_price), width=80, alignment=Qt.AlignRight, format=":.2f")
            stock_line.addWidget(self.stocks_layout[s.code+"_label_last_price"])

            self.stocks_layout[s.code+"_label_sell_price"] = ui_utils.create_label(text=str(s.sell_price), width=80, alignment=Qt.AlignRight, format=":.2f")
            stock_line.addWidget(self.stocks_layout[s.code+"_label_sell_price"])

            self.stocks_layout[s.code+"_label_sell_price_gap"] = ui_utils.create_label(text=f"{s.sell_price_gap*100:.2f}%", width=80, alignment=Qt.AlignRight)
            stock_line.addWidget(self.stocks_layout[s.code+"_label_sell_price_gap"])
            ui_utils.colorize_label(self.stocks_layout[s.code+"_label_sell_price_gap"], value=s.sell_price_gap, min=0.05, color="green")

            self.stocks_layout[s.code+"_label_nb"] = ui_utils.create_label(text=str(s.nb), width=50, alignment=Qt.AlignRight)
            stock_line.addWidget(self.stocks_layout[s.code+"_label_nb"])

            self.stocks_layout[s.code+"_label_total_price"] = ui_utils.create_label(text=str(s.total_price), width=100, alignment=Qt.AlignRight, format=":.2f")
            stock_line.addWidget(self.stocks_layout[s.code+"_label_total_price"])

            btn = QPushButton("Reload")
            btn.clicked.connect(lambda *args, s=s: self.reload_stock(s))
            btn.setFixedWidth(100)
            stock_line.addWidget(btn)
            self.stocks_layout[s.code+"_button_reload"] = btn

    def reload_stock(self, s :stock.Stock):
        s.load()
        self.stocks_layout[s.code+"_label_last_price"].setText(f"{s.last_price:.2f}")
        self.stocks_layout[s.code+"_label_buy_price_gap"].setText(f"{s.buy_price_gap*100:.2f}%")
        self.stocks_layout[s.code+"_label_sell_price_gap"].setText(f"{s.sell_price_gap*100:.2f}%")
        self.stocks_layout[s.code+"_label_total_price"].setText(f"{s.total_price:.2f}")
        self.stocks_layout[s.code+"_label_nb"].setText(str(s.nb))
  
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()