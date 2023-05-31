import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QLineEdit
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

class UserListDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("User List")

        # Wczytaj dane z pliku input.xlsx
        self.data = pd.read_excel("input.xlsx")
        
        # Tworzenie listy użytkowników
        self.user_list_widget = QListWidget()
        self.update_user_list()

        # Przyciski dodawania i usuwania użytkownika
        self.add_button = QPushButton("Dodaj użytkownika")
        self.add_button.clicked.connect(self.add_user)
        self.remove_button = QPushButton("Usuń użytkownika")
        self.remove_button.clicked.connect(self.remove_user)

        # Ustawienie layoutu
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Lista użytkowników:"))
        layout.addWidget(self.user_list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def update_user_list(self):
        # Wczytaj imiona i nazwiska użytkowników z danych
        user_names = self.data["Imię i nazwisko"].tolist()

        # Wczytaj wiek użytkowników z danych
        user_ages = self.data["Wiek"].tolist()

        # Wyświetlenie listy użytkowników w widżecie
        self.user_list_widget.clear()
        for name, age in zip(user_names, user_ages):
            self.user_list_widget.addItem(f"{name} (wiek: {age})")

    def add_user(self):
        # Okno modalne do wprowadzenia danych nowego użytkownika
        name, ok = QLineEdit.getText(QLineEdit(), "Dodaj użytkownika", "Wprowadź imię i nazwisko:")
        if ok:
            age, ok = QLineEdit.getInt(QLineEdit(), "Dodaj użytkownika", "Wprowadź wiek:")
            if ok:
                # Dodanie nowego użytkownika do danych
                self.data = self.data.append({"Imię i nazwisko": name, "Wiek": age}, ignore_index=True)

                # Zapis danych do pliku output.xlsx
                self.data.to_excel("output.xlsx", index=False)

                # Zaktualizowanie listy użytkowników
                self.update_user_list()

    def remove_user(self):
        # Sprawdzenie zaznaczonego użytkownika
        selected_item = self.user_list_widget.currentItem()
        if selected_item:
            # Pobranie indeksu zaznaczonego użytkownika
            index = self.user_list_widget.row(selected_item)

            # Usunięcie użytkownika z danych
            self.data = self.data.drop(index, axis=0).reset_index(drop=True)

            # Zapis danych do pliku output.xlsx
            self.data.to_excel("output.xlsx", index=False)

            # Zaktualizowanie listy użytkowników
            self.update_user_list()    


if __name__ == "__main__":
     app = QApplication(sys.argv)

    
 
     dialog = UserListDialog()
     dialog.exec_()

#      dialog1 = NameInputDialog()
#      if dialog1.exec_() == QDialog.Accepted:
#         name = dialog1.get_name()

# #          # Drugie okno modalne - wprowadzenie nazwiska
#      dialog2 = SurnameInputDialog()
#      if dialog2.exec_() == QDialog.Accepted:
#               surname = dialog2.get_surname()

# #              # Trzecie okno modalne - wprowadzenie wieku
#               dialog3 = AgeInputDialog()
#               if dialog3.exec_() == QDialog.Accepted:
#                   age = dialog3.get_age()

#                   print(f"Name: {name}")
#                   print(f"Surname: {surname}")
#                   print(f"Age: {age}")
             

     sys.exit(app.exec_())