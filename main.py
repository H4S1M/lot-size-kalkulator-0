from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

# Fungsi kelas utama yang QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lot Size Calc")
        self.setGeometry(100, 250, 240, 225)
        self.setFixedSize(240, 225)

        # Tambahkan widget utama ke jendela utama
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Tambahkan label dan line edit untuk Stop Loss
        stop_loss_label = QLabel("Stop Loss")
        self.stop_loss_edit = QLineEdit()
        self.stop_loss_edit.setPlaceholderText("Masukkan Stop Loss (USD)")

        # Tambahkan label dan line edit untuk jarak dari Entry ke Stop Loss dalam poin
        sl_distance_label = QLabel("Jarak N3 ke Stop Loss + spredd")
        self.sl_distance_edit = QLineEdit()
        self.sl_distance_edit.setPlaceholderText("Masukan jarak N3 ke Stop Loss (Points)")

        # Tambahkan label dan line edit untuk nilai Tick
        tick_value_label = QLabel("Tick Value")
        self.tick_value_edit = QLineEdit()
        self.tick_value_edit.setPlaceholderText("Masukkan Tick Value (USD)")

        # Tambahkan tombol untuk menghitung ukuran lot
        calculate_button = QPushButton("Hitung Lot")
        calculate_button.clicked.connect(self.calculate_lot_size)

        # Tambahkan tombol reset
        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_fields)

        # Tambahkan label untuk menampilkan hasil perhitungan
        self.lot_size_label = QLabel("Ukuran lot : ")

        # Tambahkan layout vertikal dan tambahkan widget-widget ke dalamnya
        vbox = QVBoxLayout()
        vbox.addWidget(stop_loss_label)
        vbox.addWidget(self.stop_loss_edit)
        vbox.addWidget(sl_distance_label)
        vbox.addWidget(self.sl_distance_edit)
        vbox.addWidget(tick_value_label)
        vbox.addWidget(self.tick_value_edit)
        vbox.addWidget(calculate_button)
        vbox.addWidget(reset_button)
        vbox.addWidget(self.lot_size_label)
        vbox.addStretch()

        # Tetapkan layout vertikal ke widget utama
        main_widget.setLayout(vbox)

    # Fungsi metode untuk menghitung ukuran lot
    def calculate_lot_size(self):
        if self.stop_loss_edit.text() == "" or self.sl_distance_edit.text() == "" or self.tick_value_edit.text() == "":
           self.lot_size_label.setText("MAU NGITUNG ANGIN ???")
        else:
             #conver data input dari string ke float untuk kalkulasi
             stop_loss = float(self.stop_loss_edit.text())
             sl_distance_in_points = float(self.sl_distance_edit.text())
             tick_value = float(self.tick_value_edit.text())

             # Hitung ukuran lot dengan rumus 
             dollar_risk = stop_loss
             lot_size = dollar_risk / (sl_distance_in_points * tick_value)

             # Bulatkan hasil perhitungan lot menjadi 2 digit di belakang koma
             lot_size = round(lot_size, 2)

             # Tampilkan hasil perhitungan di label
             self.lot_size_label.setText("Ukuran Lot : " + str(lot_size) + " " + "lot")

    # Fungsi metode untuk mereset input jarak ke Stop Loss dan nilai Tick
    def reset_fields(self):
        self.sl_distance_edit.clear()
        self.tick_value_edit.clear()

# Buat aplikasi dan jalankan jendela utama
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())