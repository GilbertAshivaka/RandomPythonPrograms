import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt 

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Madlipz')
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        form = QFormLayout()

        noun1 = form.addRow('First Noun: ', QLineEdit().text())
        p_noun = form.addRow('Plural Noun :', QLineEdit().text())
        noun2 = form.addRow('Second Noun: ', QLineEdit().text())
        place = form.addRow('Place:', QLineEdit().text())
        adjective = form.addRow('Adjective : ', QLineEdit().text())
        noun3 = form.addRow('Third Noun: ', QLineEdit().text())

        label = QLabel(self)

        label.setText(
            f'Be kind to your {noun1}-footed {p_noun}\n',
            f'For a duck might be someone\'s {noun2}',
            f'For I will tell you about {p_noun} in {place}',
            f'Where the weather is alway {adjective}',
            f'You might think that this is {noun3}.',
            f'Well it is!!'
        )

        layout.addLayout(form)
        layout.addWidget(label)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())










'''noun = input("Choose a noun:  ")
p_noun = input("Choose a plural noun:  ")
noun2 = input("Choose another noun:  ")
place = input("Choose a place:  ")
adjective = input("Choose an adjective (A word describing  noun):  ")
noun3 = input("Choose a third noun:  ")

print("-----------------------------------------------------------")

print("Be kind to your ",noun,"-footed ",p_noun, sep="")
print("For a duck might be somebody's" ,noun2,",")
print("For I will tell you about ",p_noun,"in ", place)
print("Where the weather is always ",adjective,".\n")
print("You might think that this is a ", noun3,",")
print("Well, it is.")
print("-----------------------------------------------------------")
'''
