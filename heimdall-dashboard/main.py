from PyQt5 import QtWidgets
import sys

class HeimdallOS(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heimdall OS - Guardian Dashboard")
        self.setGeometry(250, 150, 900, 600)
        
        label = QtWidgets.QLabel("Welcome to Heimdall OS (Blue Team Console)", self)
        label.move(260, 50)
        label.resize(500, 50)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = HeimdallOS()
    win.show()
    sys.exit(app.exec_())
