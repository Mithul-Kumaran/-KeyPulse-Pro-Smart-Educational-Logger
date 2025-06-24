from PyQt5.QtWidgets import QApplication
from ui_main import KeyInsightUI

app = QApplication([])
window = KeyInsightUI()
window.show()
app.exec_()
