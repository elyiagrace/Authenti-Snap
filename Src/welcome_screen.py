# welcome_screen.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont, QFontDatabase, QBrush, QPixmap, QPalette
from PyQt5.QtCore import Qt
from snipping_tool import SnippingTool
import os

class WelcomeScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(300, 200, 500, 400)

        # Set background image
        self.setAutoFillBackground(True)
        palette = QPalette()

        # Ensure the image path is correct
        image_path = os.path.join(os.path.dirname(__file__), "art-deco.jpg")  # Adjust path as needed
        background_brush = QBrush(QPixmap(image_path))

        palette.setBrush(QPalette.Window, background_brush)  # Use the QBrush
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.apply_modern_font()

        # Create a horizontal layout for minimize and exit buttons
        top_button_layout = QHBoxLayout()
        top_button_layout.setAlignment(Qt.AlignRight)  # Align buttons to the right

        # Add minimize and exit buttons
        minimize_button = QPushButton("-")
        exit_button = QPushButton("x")
        minimize_button.setFixedSize(40, 30)
        exit_button.setFixedSize(40, 30)

        minimize_button.setStyleSheet("background-color: rgba(30, 30, 30, 180); color: white; border: none;")
        exit_button.setStyleSheet("background-color: rgba(30, 30, 30, 180); color: white; border: none;")

        # Connect minimize and exit buttons
        minimize_button.clicked.connect(self.minimize_window)
        exit_button.clicked.connect(self.close)

        # Add minimize and exit buttons to the top button layout
        top_button_layout.addWidget(minimize_button)
        top_button_layout.addWidget(exit_button)

        layout.addLayout(top_button_layout)

        # Welcome message label
        welcome_message = QLabel("AUTHENTISNAP")
        welcome_message.setAlignment(Qt.AlignCenter)
        welcome_message.setStyleSheet("""
            background-color: rgba(100, 100, 100, 120);  /* Charcoal gray */
            color: white;  /* White text for visibility */
            border-radius: 15px;  /* Rounded edges */
            padding: 10px 15px;  /* More padding for improved appearance */
            margin: 20px;  /* Add margin for spacing */
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);  /* Subtle shadow effect */
        """)
        welcome_message.setFont(QFont("Roboto", 22, QFont.Bold))
        welcome_message.setWordWrap(True)

        # Set size policy to fixed to prevent expansion
        welcome_message.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        welcome_message.adjustSize()

        # Add a spacer above the welcome message to move it down
        layout.addSpacing(80)  # Adjust this value to move the message down as needed
        layout.addWidget(welcome_message, alignment=Qt.AlignCenter)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)  # Center the buttons

        # Add buttons for About and Snip
        about_button = QPushButton("About")
        snip_button = QPushButton("Snip")

        # Style for buttons (lighter gold)
        button_style = """
            QPushButton {
                background-color: #E3CBA0;  /* Softer shade of gold */
                color: black;  /* Black text */
                border: none;  /* No border */
                border-radius: 15px;  /* More rounded corners */
                padding: 12px 25px;  /* Increased padding */
                font-size: 16px;  /* Font size */
                font-weight: bold;  /* Bold font */
            }
            QPushButton:hover {
                background-color: #D1B38D;  /* Darker shade on hover */
                color: white;  /* Change text color on hover */
            }
        """

        about_button.setStyleSheet(button_style)
        snip_button.setStyleSheet(button_style)

        # Add buttons to the horizontal layout
        button_layout.addWidget(about_button)
        button_layout.addSpacing(20) 
        button_layout.addWidget(snip_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        # Add a spacer below the button layout to push the buttons upwards
        layout.addSpacing(80)  # Adjust this value to move the buttons further up

        # Connect button signals
        about_button.clicked.connect(self.show_about)
        snip_button.clicked.connect(self.start_snipping)


        # Add the main layout to the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def apply_modern_font(self):
        QFontDatabase.addApplicationFont("font/Montserrat-Regular.ttf")  # Ensure the font is available

    def show_about(self):
        # Show about information (implement your logic here)
        print("About clicked")  # Placeholder for actual implementation

    def start_snipping(self):
        self.close()
        self.snipping_tool = SnippingTool()
        self.snipping_tool.show()

    def minimize_window(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
