import sys

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Note that these conversions are all in seconds.
# These conversions are the ones which will be used in adding the QComboBox
# contents as well as the values which will be used in the conversion calculations
Conversions = (
    ('Second', 1),
    ('Millisecond', .001),
    ('Microsecond', .000001),
    ('Nanosecond', .000000001),
    ('Picosecond', .000000000001),
    ('Minute', 60),
    ('Hour', 3600),
    ('Day', 86400),
    ('Week', 604800),
    ('Month', 2629800),
    ('Year(calendar)', 31536000),
    ('Year(tropical)', 31556930),
    ('Year(sidereal)', 31558150)
)


class Window(QWidget):
    def __init__(self):  # This is the main function of the class Window
        super().__init__()

        self.title = "Unit Converter"  # The title which will appear in the main window
        self.left = 500
        self.top = 500
        self.width = 300
        self.height = 400
        self.iconName = "time.png"  # Added a png file for the icon picture of my Window

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))  # A method to display the icon picture in the Window
        self.setGeometry(self.left, self.top, self.width, self.height)  # Sets Geometry of application
        self.setStyleSheet("background-color: rgb(44, 50, 86);")  # Sets background color of application
        self.move(500, 150)

        self.initUI()  # Calls the function initUI
        self.show()  # Shows the application on screen when run

        # for method which uses the Conversions array content to be added to both
        # the QComboBoxes combo and combo2
        for label, multi in Conversions:
            self.combo.addItem(label, multi)
            self.combo2.addItem(label, multi)

        # Calls the functions convertTo and convertFrom whenever a text is edited inside both QLineEdits e1 and e2
        self.e1.textEdited.connect(self.convertTo)
        self.e2.textEdited.connect(self.convertFrom)
        # Calls function comboChanged whenever both combo or combo2 current index is changed
        self.combo.currentIndexChanged.connect(self.comboChanged)
        self.combo2.currentIndexChanged.connect(self.comboChanged)

        self.lastEdited = self.e1

    # This is a function which adds attributes for the application
    # It is where all the attributes are defined as well
    # It is where the UI are added as well to the application
    def initUI(self):

        gbox = QGridLayout()  # variable for layout of the application
        self.setLayout(gbox)   # Sets the layout of the application

        self.combo = QComboBox()    # QComboBox called combo which will store all the units of time
        self.combo.setStyleSheet("QComboBox {\n"
                                 "\n"
                                 "    background-color: rgb(44, 50, 86);\n"
                                 "    color: rgb(79, 199, 255);\n"
                                 "    border: none;\n"
                                 "    border-radius: 9px;\n"
                                 "    text -align: center;\n"
                                 "}\n"
                                 "")

        self.combo2 = QComboBox()  # QComboBox called combo2 which will store all the units of time
        self.combo2.setStyleSheet("QComboBox {\n"
                                  "\n"
                                  "    background-color: rgb(44, 50, 86);\n"
                                  "    color: rgb(79, 199, 255);\n"
                                  "    border: none;\n"
                                  "    border-radius: 9px;\n"
                                  "    text -align: center;\n"
                                  "}\n"
                                  "")

        self.e1 = QLineEdit()   # QLineEdit e1 is where the values will be entered
        self.e1.setPlaceholderText("Enter Value")   # Provided a place holder for better understanding
        self.e1.setMinimumWidth(200)    # Sets the minimum width of the QLineEdit
        self.e1.setValidator(QDoubleValidator())    # Sets the values acceptable to input as floating points
        self.e1.setAlignment(Qt.AlignCenter)    # Aligns text at center when typed
        self.e1.setFont(QtGui.QFont("Arial", 10))   # Sets font and font size of text
        self.e1.setStyleSheet("QLineEdit {\n"   # Provides edits to how the QLineEdit will look
                              "background-color: rgb(115, 199, 255);\n"
                              "border: none;\n"
                              "border-radius: 9px;\n"
                              "}")

        self.e2 = QLineEdit()
        self.e2.setMinimumWidth(200)
        self.e2.setValidator(QDoubleValidator())
        self.e2.setAlignment(Qt.AlignCenter)
        self.e2.setFont(QtGui.QFont("Arial", 10))
        self.e2.setStyleSheet("QLineEdit {\n"
                              "background-color: rgb(115, 199, 255);\n"
                              "border: none;\n"
                              "border-radius: 9px;\n"
                              "}")

        self.label = QLabel("My UNIT CONVERTER")    # QLabel label to act as a title of the application
        myFont = QtGui.QFont()
        myFont.setBold(True)
        self.label.setFont(myFont)
        self.label.setFont(QtGui.QFont("Segoe UI", 15))
        self.label.setStyleSheet("color: rgb(247, 19, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.l1 = QLabel("From: ")      # QLabel l1 to act as an indicator for the From conversion
        self.l1.setFont(QtGui.QFont("Segoe UI", 10))
        self.l1.setStyleSheet("color: rgb(247, 19, 255);")
        self.l1.setAlignment(Qt.AlignCenter)

        self.l2 = QLabel("To: ")    # QLabel l2 to act as an indicator for the To conversion
        self.l2.setFont(QtGui.QFont("Segoe UI", 10))
        self.l2.setStyleSheet("color: rgb(247, 19, 255);")
        self.l2.setAlignment(Qt.AlignCenter)

        self.l3 = QLabel("UNIT OF TIME")    # QLabel l3 to provide understanding what unit the application converts
        self.l3.setFont(QtGui.QFont("Segoe UI", 10))
        self.l3.setStyleSheet("color: rgb(247, 19, 255);")
        self.l3.setAlignment(Qt.AlignCenter)

        # Below shows the added widgets which will appear in the application
        # all the added widgets are already created and customized above
        # the numbers shown at the end sets their location in the application
        # since we are using QGridLayout, this method is applicable
        gbox.addWidget(self.label, 0, 0, 1, 4)
        gbox.addWidget(self.l1, 1, 0, 1, 3)
        gbox.addWidget(self.combo, 2, 0, 1, 2)
        gbox.addWidget(self.e1, 2, 3)
        gbox.addWidget(self.l2, 3, 0, 1, 2)
        gbox.addWidget(self.combo2, 4, 0, 1, 2)
        gbox.addWidget(self.e2, 4, 3)
        gbox.addWidget(self.l3, 6, 0, 1, 4)

    # Below are the functions which will be used to set the calculation
    # of the conversion process when the program is run

    # A function for the e1 QLineEdit which acts whenever a float is typed
    # It works for the "To" conversions
    # Makes calculations for e1 and displays result in e2 using combo and combo2 current data
    def convertTo(self):
        try:
            value = float(self.e1.text())
        except ValueError:
            return
        self.lastEdited = self.e1
        seconds = value * self.combo.currentData()
        result = str(seconds / self.combo2.currentData())
        self.e2.setText(result.rstrip('0').rstrip('.'))

    # A function for the e2 QLineEdit which acts whenever a float is typed
    # It works for the "From" conversions
    # It makes the calculations for e2 using combo and combo2 currentData and display result in e1
    def convertFrom(self):
        try:
            value = float(self.e2.text())
        except ValueError:
            return
        self.lastEdited = self.e2
        seconds = value * self.combo2.currentData()
        result = str(seconds / self.combo.currentData())
        self.e1.setText(result.rstrip('0').rstrip('.'))

    # This is a function for both the QLineEdits indicating whenever
    # a value is entered or edited, it will call the above functions to work
    def comboChanged(self):
        if self.lastEdited == self.e1:
            self.convertTo()
        else:
            self.convertFrom()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    App.setStyle(QStyleFactory.create('Fusion'))   # This just sets the style of the application when run
    sys.exit(App.exec())
