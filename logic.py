from PyQt6.QtWidgets import *
from vote_menu import Ui_MainWindow
from candidate_menu import Ui_Form1
from final_menu import Ui_Form2


class VoteMenu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.john_votes = 0
        self.jane_votes = 0
        self.vote_button.clicked.connect(self.show_candidate_menu)
        self.exit_button.clicked.connect(self.show_final_menu)

    def show_candidate_menu(self):
        candidate_menu = CandidateMenu(self)
        candidate_menu.show()
        self.hide()

    def show_final_menu(self):
        self.final_menu = FinalMenu(self.john_votes, self.jane_votes)
        self.final_menu.show()
        self.hide()

    def vote_for_candidate(self, candidate):
        if candidate == 'John':
            self.john_votes += 1
        elif candidate == 'Jane':
            self.jane_votes += 1


class CandidateMenu(QWidget, Ui_Form1):
    def __init__(self, parent):
        super().__init__()

        self.setupUi(self)
        self.john_button.clicked.connect(lambda: self.cast_vote('John'))
        self.jane_button.clicked.connect(lambda: self.cast_vote('Jane'))
        self.parent = parent

    def cast_vote(self, candidate):
        self.parent.vote_for_candidate(candidate)
        self.parent.show()
        self.hide()


class FinalMenu(QWidget, Ui_Form2):
    def __init__(self, john_votes, jane_votes):
        super().__init__()

        self.setupUi(self)
        self.john_final.setText(f'John: {john_votes} votes')
        self.jane_final.setText(f'Jane: {jane_votes} votes')
        total_votes = john_votes + jane_votes
        self.total_final.setText(f'Total: {total_votes} votes')
