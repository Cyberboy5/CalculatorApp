from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QLineEdit, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator


class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(330, 370)
        self.display = ""
        self.edit = QLineEdit()
        self.style_edit(self.edit)
        self.setStyleSheet("background-color: #36454f;")
        self.edit.setAlignment(Qt.AlignRight)

        validator = QIntValidator()
        self.edit.setValidator(validator)

        self.v_box = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.addition_box = QHBoxLayout()
        self.second_additional_box = QHBoxLayout()


        # Creating buttons and adding them to the layout
        for i in range(1, 4):
            btn = QPushButton(str(i), self)
            self.style_button(btn)
            self.h_box1.addWidget(btn)
            btn.clicked.connect(self.press)

        btn_plus = QPushButton('+', self)
        self.style_button(btn_plus, background_color="#FF9500")
        self.h_box1.addWidget(btn_plus)
        btn_plus.clicked.connect(self.press)

        for i in range(4, 7):
            btn = QPushButton(str(i), self)
            self.style_button(btn)
            self.h_box2.addWidget(btn)
            btn.clicked.connect(self.press)

        btn_minus = QPushButton('-', self)
        self.style_button(btn_minus, background_color="#FF9500")
        self.h_box2.addWidget(btn_minus)
        btn_minus.clicked.connect(self.press)

        for i in range(7, 10):
            btn = QPushButton(str(i), self)
            self.style_button(btn)
            self.h_box3.addWidget(btn)
            btn.clicked.connect(self.press)

        btn_multiply = QPushButton('*', self)
        self.style_button(btn_multiply, background_color="#FF9500")
        self.h_box3.addWidget(btn_multiply)
        btn_multiply.clicked.connect(self.press)


        # Adding additional buttons
        for char in 'C()/':
            btn = QPushButton(char, self)
            if char == 'C':
                btn.clicked.connect(self.clear_display)
                self.style_button(btn,background_color='#A5A5A5')

            elif char == '/':
                self.style_button(btn,background_color='#FF9500')
                
            else:
                btn.clicked.connect(self.press)
                self.style_button(btn,background_color='#A5A5A5')
            self.addition_box.addWidget(btn)

        for char in "<0.=":
            btn = QPushButton(char, self)
            if char == '=':
                self.style_button(btn, background_color="#FF9500")
                btn.clicked.connect(self.get_result)
            elif char == '<':
                self.style_button(btn, background_color="#A5A5A5")
                btn.clicked.connect(self.delete_last)
            else:
                self.style_button(btn)
                btn.clicked.connect(self.press)
            self.second_additional_box.addWidget(btn)

        self.v_box.addWidget(self.edit)
        self.v_box.addLayout(self.addition_box)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.second_additional_box)

        self.setLayout(self.v_box)

    def style_button(self, button, background_color="#333333"):
        button.setStyleSheet(f"""
            QPushButton {{
                border: none;
                border-radius: 30px;
                background-color: {background_color};
                font-size: 18px;
                color: white;
            }}
            QPushButton:pressed {{
                background-color: #555555;
            }}
        """)
        button.setFixedSize(60, 60)

    def style_edit(self, edit):
        edit.setStyleSheet("""
            QLineEdit {
                border: none;
                border-radius: 15px;
                background-color: #333333;
                font-size: 18px;
                color: white;
                padding: 10px;
                text-align: left;
            }
        """)
        edit.setFixedHeight(40)


    def press(self):
        btn = self.sender()
        self.display += btn.text()
        self.edit.setText(self.display)

    def get_result(self):
        if not self.display:
            self.edit.setText("Error")
        else:
            try:
                self.edit.setText(str(eval(self.display)))
                self.display = ""
            except Exception as e:
                self.edit.setText("Error")
                self.display = ""


    def delete_last(self):
        self.display = self.display[:-1]
        self.edit.setText(self.display)
    
    def clear_display(self):
        self.display = ''
        self.edit.setText(self.display)

    def keyPressEvent(self, event):
        key = event.key()
        if key in [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4,
                   Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9,
                   Qt.Key_Plus, Qt.Key_Minus, Qt.Key_Asterisk,Qt.Key_Slash,Qt.Key_Equal]:
            self.display += event.text()
            self.edit.setText(self.display)
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            self.get_result()
        elif key == Qt.Key_Backspace:
            self.delete_last()
        elif key == Qt.Key_C:
            self.clear_display()


app = QApplication([])
win = Win()
win.show()
app.exec_()
