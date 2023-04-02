from random import randint, shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,
QMessageBox, QRadioButton, QButtonGroup)
app = QApplication([])
main_win = QWidget()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Давай некст!')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Не уверен, но пусть будет так')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Не уверен, но пусть будет так' == btn_OK.text():
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Красавчик!!! Горжусь!!!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-На сколько вопросов вы угадали ответ: ', main_win.score)
        print('Процентики вашего ума: ', (main_win.score / main_win.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Ну нееее, подумай получше')
            print('Процентики вашего ума: ', (main_win.score / main_win.total * 100), '%')

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    main_win.cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[main_win.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Хочу вот эта':
        check_answer()
    else:
        next_question()

questions_list=[]
questions_list.append(Question('Какая страна самая большая?', 'Россия', 'Обь',
 'Владислав', 'Не Россия'))
questions_list.append(Question('Сколько месяцев в году?', '12', 'Владислав',
'Январь', 'Мудрый дуб'))
questions_list.append(Question('Самая лучшая буква русского алфавита?',
'Ё', 'Ъ', 'Ы', 'Ь'))

main_win.setWindowTitle('Memory Card')
btn_OK = QPushButton('Не уверен, но пусть будет так')
lb_Question = QLabel('Самая лучшая буква русского алфавита?')
RadioGroupBox = QGroupBox('Чего Ваше Высочество пожелает ответить?')
rbtn_1 = QRadioButton('Ъ')
rbtn_2 = QRadioButton('Ё')
rbtn_3 = QRadioButton('Ь')
rbtn_4 = QRadioButton('Ы')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ буит тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question,
alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.score = 0
main_win.total = 0
main_win.cur_question = -1
q = Question('Самая лучшая буква русского алфавита?', 'Ё', 'Ъ', 'Ь', 'Ы')
ask(q)
btn_OK.clicked.connect(click_OK)

next_question()

main_win.setLayout(layout_card)
main_win.show()
app.exec_()