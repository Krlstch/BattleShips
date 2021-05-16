from PyQt5.QtWidgets import QPushButton

from src.special.game_states import GameState


class EmptyScreen:
    def __init__(self, application, hidden=True):
        self.app = application
        self.state = None

        self.setup_ui()

        if hidden:
            self.hide()
        else:
            self.show()


    def setup_ui(self):
        self.next_button = QPushButton(self.app.window)
        self.next_button.setGeometry(200, 300, 400, 200)
        self.next_button.setText("Next")
        # self.next_button.setFont(QFont("Arial Font", 20))
        self.next_button.clicked.connect(self.__on_next_button_pressed)

    def show(self, state=GameState.EMPTY_BEFORE_PLAYER2_PLAY):
        self.state = state
        self.next_button.show()

    def hide(self):
        self.next_button.hide()

    def __on_next_button_pressed(self):
        self.hide()
        self.app.game_screen.show(self.state)
