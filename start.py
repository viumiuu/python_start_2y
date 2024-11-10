from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

# Style: 10
# Чорний + червоний + жовтий
app.setStyleSheet("""
    QApplication {
        background: #0E0E0E;  /* Темний фон для супергеройського стилю */
    }
    QWidget {
        background: #1A1A1A;  /* Темно-сірий фон для вікон */
        color: #FFDD00;  /* Жовтий колір тексту */
    }
    QPushButton {
        background-color: #FF0000;  /* Червоний для кнопок */
        border: 3px solid #000000;  /* Чорний бордер для кнопок */
        border-radius: 5px;  /* Закруглені кути кнопок */
        color: #FFFFFF;  /* Білий текст */
        font-family: 'Impact', sans-serif;  /* Сильний шрифт для супергеройського стилю */
        font-size: 18px;
        padding: 10px 20px;
        margin: 8px 0;
    }
    QPushButton:hover {
        background-color: #FF4500;  /* Світліший червоний при наведенні */
    }
    QPushButton:pressed {
        background-color: #B22222;  /* Темніший червоний при натисканні */
    }
    QGroupBox {
        background: #2F2F2F;  /* Темно-сірий фон для груп */
        border: 3px solid #FFDD00;  /* Жовтий бордер для груп */
        border-radius: 5px;  /* Закруглені кути */
        padding: 10px;
        font-family: 'Impact', sans-serif;
        font-size: 20px;
        color: #FFDD00;  /* Жовтий текст в групах */
    }
    QLabel {
        color: #FFDD00;  /* Жовтий текст */
        font-family: 'Impact', sans-serif;
        font-size: 22px;
        margin: 5px;
    }
""")
 
 
 
 
from main_window import *
from menu_window import *
 
 
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

    try:
        current_question = choice(questions)

        #questions.remove(current_question)

        lb_question.setText(current_question.question)
        lb_right_answer.setText(current_question.answer)

        shuffle(radio_buttons)

        radio_buttons[0].setText(current_question.answer)
        radio_buttons[1].setText(current_question.wrong_answer1)
        radio_buttons[2].setText(current_question.wrong_answer2)
        radio_buttons[3].setText(current_question.wrong_answer3)

    except:
        lb_question.setText("Кінець тесту")
        lb_right_answer.setText("Кінець тесту")

        shuffle(radio_buttons)

        radio_buttons[0].setText("")
        radio_buttons[1].setText("")
        radio_buttons[2].setText("")
        radio_buttons[3].setText("")

 
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
                lb_result.setStyleSheet("color: green;")
                break
 
    # Конструкція else після циклу працює лише тоді, коли цикл закінчився без переривання
    #  (тобто коли цикл не був зупинений за допомогою break).
    else:
        # якщо в циклі немає істини (true), обрана не вірна відповідь
        lb_result.setText('Не вірно!')
        lb_result.setStyleSheet("color: red;")
        current_question.got_wrong()
 
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
 
def rest():
    window.hide()

    n = sp_rest.value() * 60
    sleep(n)

    window.show()

btn_rest.clicked.connect(rest) 

def menu ():

    total_answers = 0
    right_answers = 0
 
    # Перевіряємо всі запитання та рахуємо правильні + загальні відповідді
    for question in questions:
        total_answers += question.count_ask
        right_answers += question.count_right
 
    # формула успішності
    success_rate = (right_answers/(total_answers if total_answers > 0 else 1)) * 100
 
    text = f'Разів відповіли: {total_answers}\n' \
           f'Вірних відповідей: {right_answers}\n' \
           f'Успішність: {round(success_rate, 2)}%'
    # підставити змінну с текстом до порожнього QLabel
    lb_statistic.setText(text)
 
 
    # Показати вікно "Меню"
    menu_win.show()
 
    # Виставити вікно "Меню" по центру екрану ПК
    screen_geometry = app.desktop().screenGeometry()
    x = (screen_geometry.width() - menu_win.width()) // 2
    y = (screen_geometry.height() - menu_win.height()) // 2
    menu_win.move(x, y)
 
    # Приховати вікно "Головне"
    window.hide()

btn_menu.clicked.connect(menu)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
 
btn_clear.clicked.connect(clear)
 
# кнопка додати нове запитання з 4 варіантами відповідді
def add_question():
    if le_question.text().strip() != "":
        new_q = Question(le_question.text(), le_right_ans.text(),
                        le_wrong_ans1.text(), le_wrong_ans2.text(),
                        le_wrong_ans3.text())
 
        questions.append(new_q)
        clear()
 
btn_add_question.clicked.connect(add_question)
 
 


# показати вікно
window.show()
# запустити додаток
app.exec_()
