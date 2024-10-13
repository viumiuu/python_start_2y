from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

from main_window import *

question = "Apple"

answer = "apple"

wrong_answer1 = "orenge"
wrong_answer2 = "orenge"
wrong_answer3 = "orenge"

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
shuffle(radio_buttons)

# підставляємо питання та відповідді до радіо перемикачів
def new_question():
    lb_question.setText(question)
    lb_right_answer.setText(answer)
 
    radio_buttons[0].setText(answer)
    radio_buttons[1].setText(wrong_answer1)
    radio_buttons[2].setText(wrong_answer2)
    radio_buttons[3].setText(wrong_answer3)
 
# запускаємо функцію
new_question()
 
# Перевірка правильної відповідді
def check():
    RadioGroup.setExclusive(False)
    # проходимось по всім радіо перемикачам
    for answer in radio_buttons:
        #  перевіряємо які перемикачі обрані користувачем
        if answer.isChecked():
            # прибираємо "галочку" біля відповідді
            answer.setChecked(False)
 
            # перевіряємо текст перемикача з правильною відповіддю
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Вірно!')
                break
 
    # Конструкція else після циклу працює лише тоді, коли цикл закінчився без переривання
    #  (тобто коли цикл не був зупинений за допомогою break).
    else:
        # якщо в циклі немає істини (true), обрана не вірна відповідь
        lb_result.setText('Не вірно!')