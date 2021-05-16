from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton

from src.special.game_states import GameState


class EndScreen:
    def __init__(self, application, hidden=True):
        self.app = application

        self.setup_ui()
        if hidden:
            self.hide()
        else:
            self.show()


    def setup_ui(self):
        self.exit_button = QPushButton(self.app.window)
        self.exit_button.setGeometry(250, 600, 300, 100)
        self.exit_button.setText("Back to main menu")
        self.exit_button.clicked.connect(self.__on_exit_button_pressed)

        self.title_label = QLabel(self.app.window)
        self.title_label.setGeometry(100, 50, 600, 200)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial Font", 80))

    def show(self, state=GameState.PLAYER1_PLAYING):
        self.title_label.setText(f"Player {GameState.get_player(state)+1} won")

        self.exit_button.show()
        self.title_label.show()

    def hide(self):
        self.title_label.hide()
        self.exit_button.hide()

    def __on_exit_button_pressed(self):
        self.hide()
        self.app.reset_vars()
        self.app.start_screen.show()
