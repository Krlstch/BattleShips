from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import Qt
from src.special.game_states import GameState


class StartScreen:
    def __init__(self, application, hidden: bool = True):
        self.app = application
        self.setup_ui()

        if hidden:
            self.hide()
        else:
            self.show()

    def setup_ui(self):
        self.start_button = QPushButton(self.app.window)
        self.start_button.setGeometry(250, 300, 300, 100)
        self.start_button.setText("Start")
        self.start_button.clicked.connect(self.__on_start_button_pressed)

        self.exit_button = QPushButton(self.app.window)
        self.exit_button.setGeometry(250, 600, 300, 100)
        self.exit_button.setText("Exit")
        self.exit_button.clicked.connect(self.__on_exit_button_pressed)

        self.title_label = QLabel(self.app.window)
        self.title_label.setGeometry(100, 50, 600, 200)
        self.title_label.setText("Battle Ships")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial Font", 80))

    def show(self):
        self.start_button.show()
        self.exit_button.show()
        self.title_label.show()

    def hide(self):
        self.start_button.hide()
        self.exit_button.hide()
        self.title_label.hide()

    def __on_start_button_pressed(self):
        self.hide()
        self.app.setup_screen.show(GameState.PLAYER1_PREPARING)

    def __on_exit_button_pressed(self):
        self.app.window.close()

