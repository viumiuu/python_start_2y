from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])
 
from main_window import *
 
 
class Question ():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True 
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1

q1 = Question("З яким кельтським святом пов’язане походження Хелловіну?", "Самайн", "Імболк", "Лугнасад", "Бельтайн")
q2 = Question("Яке ім’я має ліхтар з гарбуза, що є символом Хелловіну?", "Джек-ліхтар", "Темний Том", "Сяючий Сем", "Гарбузовий Джо")
q3 = Question("Чому чорні коти асоціюються з Хелловіном?", "Їх вважали супутниками відьом", "Вони можуть бачити духів", "Вони були священними для кельтів", "Вони символізують невезіння")
q4 = Question("Яке з цих створінь вважається традиційним символом Хелловіну?", "Вампір", "Грифон", "Єдиноріг", "Кентавр")
q5 = Question("В яких країнах найпопулярніше святкування Хелловіну?", "Ірландія та США", "Франція та Канад", "Іспанія та Мексикa", "Бразилія та Португалія")
q6 = Question("Як називається традиція ходити від дверей до дверей, збираючи солодощі на Хелловін?", "«Trick or treat»", " «Викрутка або цукерка»", "«Солодке частування»", "«Цукерки або вихід»")
q7 = Question("Яке дерево часто використовується для створення магічних жезлів, популярних на Хелловін?", "Глід", "Горіх", "В’яз", "Дуб")
q8 = Question("Чому люди одягали костюми на Самайн (попередник Хелловіну)?", "Щоб заплутати злих духів та уникнути їхнього вплив", "Щоб святкувати зміну пір року", "Щоб отримати більше їжі від сусідів", "Щоб справити враження на духів")
q9 = Question(" Який відомий роман Готичної літератури пов’язують із Хелловіном?", "“Дракула”", "“Війна світів”", "“Граф Монте-Крісто”", "“Франкенштейн”")
q10 = Question("Який фрукт часто використовується в хелловінських іграх, коли гравці повинні ловити його ротом у воді?", "Яблуко", "Груша", "Слива", "Апельсин")

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
 
# Помістили радіо перемикачі в список
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
# перемішали список рандомно

 
# підставляємо питання та відповідді до радіо перемикачів
def new_question():
    global current_question
    current_question = choice(questions)

    lb_question.setText(current_question.question)
    lb_right_answer.setText(current_question.answer)

    shuffle(radio_buttons)

    radio_buttons[0].setText(current_question.answer)
    radio_buttons[1].setText(current_question.wrong_answer1)
    radio_buttons[2].setText(current_question.wrong_answer2)
    radio_buttons[3].setText(current_question.wrong_answer3)
 
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
                current_question.got_right()
                lb_result.setText('Вірно!')
                break
 
    # Конструкція else після циклу працює лише тоді, коли цикл закінчився без переривання
    #  (тобто коли цикл не був зупинений за допомогою break).
    else:
        # якщо в циклі немає істини (true), обрана не вірна відповідь
        lb_result.setText('Не вірно!')
        current_question.got_wrong
 
    RadioGroup.setExclusive(True)
 
# Клік на кнопку "Відповісти" або "Наступне запитання"
def click_ok():
 
    # Якщо користувач натиснув на кнопку "Відповісти"
    # викликаємо функцію check, щоб перевірити правильну відповідь
    # та приховуємо группу з питаннями
    # показуємо групу з відповіддями
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
 
        # Змінюємо текст кнопки "Відповісти" на "Наступне запитання"
        btn_next.setText('Наступне запитання')
    else:
        # Натиснута кнопка "Наступне запитання" то запитуємо нове запитання
        # приховуємо відповідді 
        # показуємо групу з питаннями
        new_question()
        gb_question.show()
        gb_answer.hide()
 
        # Змінюємо текст кнопки "Наступне запитання" на "Відповісти" 
        btn_next.setText('Відповісти')
 
# Під'єднуємо кнопку до обробника функції click_ok()
btn_next.clicked.connect(click_ok)
 
 
# показати вікно
window.show()
# запустити додаток
app.exec_()
