# snipping_tool.py

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPen, QColor
from screenshot_processor import ScreenshotProcessor

class SnippingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snipping Tool Clone')
        self.showFullScreen()  # Fullscreen for capturing
        self.setWindowOpacity(0.4)  # Make the window slightly transparent
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.is_drawing = False
        self.processor = ScreenshotProcessor()

        # Prepare a canvas to draw the selection rectangle
        self.setStyleSheet("background-color: black;")

    def mousePressEvent(self, event):
        """Capture the initial mouse position when the user starts drawing the snip area."""
        if event.button() == 1:  # Left-click
            self.start_x = event.x()
            self.start_y = event.y()
            self.is_drawing = True

    def mouseMoveEvent(self, event):
        """Update the snip area while the user is dragging."""
        if self.is_drawing:
            self.end_x = event.x()
            self.end_y = event.y()
            self.update()  # Triggers paintEvent to draw the rectangle

    def mouseReleaseEvent(self, event):
        """Once the user releases the mouse, capture the screenshot."""
        if event.button() == 1:  # Left-click
            self.is_drawing = False
            self.capture_screenshot()

    def paintEvent(self, event):
        """Draw the rectangle on the screen to indicate the snip area."""
        if self.is_drawing and self.start_x and self.start_y and self.end_x and self.end_y:
            qp = QPainter(self)
            pen = QPen(QColor(255, 0, 0), 2, 1)  # Red border for snipping
            qp.setPen(pen)
            rect = QRect(min(self.start_x, self.end_x), min(self.start_y, self.end_y),
                         abs(self.start_x - self.end_x), abs(self.start_y - self.end_y))
            qp.drawRect(rect)

    def capture_screenshot(self):
        """Handle the screenshot capture, hashing, and IPFS upload."""
        if self.start_x and self.start_y and self.end_x and self.end_y:
            x = min(self.start_x, self.end_x)
            y = min(self.start_y, self.end_y)
            width = abs(self.start_x - self.end_x)
            height = abs(self.start_y - self.end_y)

            # Save screenshot using the processor
            self.processor.save_screenshot((x, y, x + width, y + height))

            # Hash the screenshot and store to IPFS via Pinata API
            self.processor.hash_screenshot()
            self.processor.store_to_ipfs()

            # Close the application after the snip is complete
            self.close()

