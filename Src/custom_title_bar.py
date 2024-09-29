# custom_title_bar.py
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setStyleSheet("background-color: #2c3e50;")

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0)

        self.title_label = QLabel("Authentihash")  # Updated title
        self.title_label.setStyleSheet("""
            color: gold;  # Changed text color to gold
            font-size: 24px;
            font-weight: 600;
            padding: 10px;
        """)
        layout.addWidget(self.title_label)

        # Add buttons (minimize, close)
        self.minimize_button = QPushButton("-")
        self.minimize_button.setFixedSize(40, 30)
        self.minimize_button.setStyleSheet("background-color: darkred; color: white; border: none;")
        self.minimize_button.clicked.connect(self.minimize_window)
        layout.addWidget(self.minimize_button)

        self.close_button = QPushButton("x")
        self.close_button.setFixedSize(40, 30)
        self.close_button.setStyleSheet("background-color: darkred; color: white; border: none;")
        self.close_button.clicked.connect(self.close_window)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def minimize_window(self):
        self.window().showMinimized()

    def close_window(self):
        self.window().close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.window().move(event.globalPos() - self.drag_position)
            event.accept()
