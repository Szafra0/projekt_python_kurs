import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class NameInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Name")

        self.name_label = QLabel("Enter your name:")
        self.name_input = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_name(self):
        return self.name_input.text()


class SurnameInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Surname")

        self.surname_label = QLabel("Enter your surname:")
        self.surname_input = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_surname(self):
        return self.surname_input.text()


class AgeInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Age")

        self.age_label = QLabel("Enter your age:")
        self.age_input = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_age(self):
        return int(self.age_input.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Pierwsze okno modalne - wprowadzenie imienia
    dialog1 = NameInputDialog()
    if dialog1.exec_() == QDialog.Accepted:
        name = dialog1.get_name()

        # Drugie okno modalne - wprowadzenie nazwiska
        dialog2 = SurnameInputDialog()
        if dialog2.exec_() == QDialog.Accepted:
            surname = dialog2.get_surname()

            # Trzecie okno modalne - wprowadzenie wieku
            dialog3 = AgeInputDialog()
            if dialog3.exec_() == QDialog.Accepted:
                age = dialog3.get_age()

                print(f"Name: {name}")
                print(f"Surname: {surname}")
                print(f"Age: {age}")
            else:
                print("Cancelled age input")
        else:
            print("Cancelled surname input")
    else:
        print("Cancelled name input")

    sys.exit(app.exec_())