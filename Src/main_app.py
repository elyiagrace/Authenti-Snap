# main_app.py

import sys
from PyQt5.QtWidgets import QApplication
from ui import WelcomeScreen

class MainApp:
    def __init__(self):
        """Start the main snipping tool application."""
        self.app = QApplication(sys.argv)
        self.welcome_screen = WelcomeScreen()

    def run(self):
        """Run the application loop."""
        self.welcome_screen.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    # Initialize and run the main application
    main_app = MainApp()
    main_app.run()


