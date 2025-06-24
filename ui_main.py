from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
from keylogger import KeyLogger

class KeyInsightUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KeyPulse Pro")
        self.setGeometry(400, 150, 740, 520)
        self.setStyleSheet("background-color: #1e1e2f; color: #eeeeee;")

        layout = QVBoxLayout()
        layout.setSpacing(18)

        # Title
        self.title_label = QLabel("🕵️  KeyPulse Pro – Smart Educational Logger")
        self.title_label.setFont(QFont("Segoe UI", 22, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.title_label)

        # Compact Status Badge
        self.status_label = QLabel("● Stopped")
        self.status_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #2c2c3d;
                color: #ff4444;
                border: 1px solid #ff8888;
                padding: 6px 12px;
                border-radius: 20px;
                max-width: 120px;
                margin: auto;
            }
        """)
        layout.addWidget(self.status_label)

        # Centered Button
        button_layout = QHBoxLayout()
        self.toggle_button = QPushButton("Start Logging")
        self.toggle_button.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.toggle_button.setFixedWidth(160)
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #2979ff;
                color: white;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #5393ff;
            }
        """)
        self.toggle_button.clicked.connect(self.toggle_logging)
        button_layout.addStretch()
        button_layout.addWidget(self.toggle_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        # Log Display Area (Styled Box)
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setFont(QFont("Courier New", 10))
        self.log_display.setStyleSheet("""
            QTextEdit {
                background-color: #141421;
                color: #00ffc3;
                border: 1px solid #444;
                border-radius: 10px;
                padding: 12px;
            }
        """)
        layout.addWidget(self.log_display)

        self.setLayout(layout)

        # Logger
        self.logger = KeyLogger()
        self.listener = None
        self.is_running = False
        self.log_file = "key_log.txt"

    def toggle_logging(self):
        if not self.is_running:
            self.listener = self.logger.start()
            self.is_running = True
            self.status_label.setText("● Logging")
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #233d2e;
                    color: #44ff88;
                    border: 1px solid #66ffbb;
                    padding: 6px 12px;
                    border-radius: 20px;
                    max-width: 120px;
                    margin: auto;
                }
            """)
            self.toggle_button.setText("Stop Logging")
            self.log_display.setPlainText("")
        else:
            self.listener.stop()
            self.is_running = False
            self.status_label.setText("● Stopped")
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #2c2c3d;
                    color: #ff4444;
                    border: 1px solid #ff8888;
                    padding: 6px 12px;
                    border-radius: 20px;
                    max-width: 120px;
                    margin: auto;
                }
            """)
            self.toggle_button.setText("Start Logging")
            self.show_logs()

    def show_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as f:
                logs = f.read()
                self.log_display.setPlainText(logs)
