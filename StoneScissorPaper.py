# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\projects\project\style.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color:white;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"margin-bottom:20px;\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    border-radius:20px;\n"
"    background-color:#FFFACD;\n"
"    border-color:black;    \n"
"    border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#FFFAAA;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FFE4B5;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    border-radius:20px;\n"
"    background-color:#FFFACD;\n"
"    border-color:black;    \n"
"    border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#FFFAAA;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FFE4B5;\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    border-radius:20px;\n"
"    background-color:#FFFACD;\n"
"    border-color:black;    \n"
"    border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#FFFAAA;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FFE4B5;\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    border-radius:20px;\n"
"    background-color:#FFFACD;\n"
"    border-color:black;    \n"
"    border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#FFFAAA;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FFE4B5;\n"
"}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignLeft)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setMinimumSize(QtCore.QSize(20, 0))
        self.label_3.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"margin-top:20px;\n"
"margin-bottom:20px")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    border-radius:20px;\n"
"    background-color:#FFFACD;\n"
"    border-color:black;    \n"
"    border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#FFFAAA;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FFE4B5;\n"
"}\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    border-radius:20px;\n"
"    background-color:#FFFACD;\n"
"    border-color:black;    \n"
"    border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#FFFAAA;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FFE4B5;\n"
"}\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Камень/ножницы/бумага by Dmitr.Pod"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Приветствуем вас в игре &quot;Камень, ножницы, бумага!&quot;</p><p align=\"center\">Чтобы начать игру нажмите на кнопку &quot;Начать&quot;</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Начать"))
        self.label_2.setText(_translate("MainWindow", "Выберите: камень, ножницы или бумагу!"))
        self.pushButton_2.setText(_translate("MainWindow", "Камень"))
        self.pushButton_3.setText(_translate("MainWindow", "Ножницы"))
        self.pushButton_4.setText(_translate("MainWindow", "Бумага"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Ок"))
        self.pushButton_6.setText(_translate("MainWindow", "Назад"))


        def ClickNext():
            self.stackedWidget.setCurrentWidget(ui.page_2)
            self.label_2.setText("Выберите: камень, ножницы или бумагу!!")
            self.label_3.setText("")
            self.pushButton_5.setText("Ок")

            global Player_Choice
            Player_Choice = 0

        def ClickStart():
            self.stackedWidget.setCurrentWidget(ui.page)

        def scissors():
            global Player_Choice
            Player_Choice = 2
        def stone():
            global Player_Choice
            Player_Choice = 1
        def paper():
            global Player_Choice
            Player_Choice = 3

        def Choice(number):
            if number == 1:
                a = "камень"
                return a
            elif number == 2:
                a = "ножницы"
                return a
            elif number == 3:
                a = "бумагу"
                return a
        
        def ReturnPlay():
            self.pushButton_5.setText("Начать заново!")
            global Player_Choice
            Player_Choice = 4

        def GoPlay():
            global Player_Choice
            if Player_Choice == 4:
                ClickNext()
            else:
                Computer_Choice = random.randint(1,3)
                if Player_Choice > 0:
                        if Computer_Choice == Player_Choice:
                                self.label_2.setText("Ничья!")
                                Computer_Choice_Text = Choice(Computer_Choice)
                                self.label_3.setText(f"Компьютер выбрал {Computer_Choice_Text}!")
                                ReturnPlay()
                        elif Computer_Choice + 1 == Player_Choice or Computer_Choice - 2 == Player_Choice:
                                self.label_2.setText("К сожалению, вы проиграли!")
                                Computer_Choice_Text = Choice(Computer_Choice)
                                self.label_3.setText(f"Компьютер выбрал {Computer_Choice_Text}!")
                                ReturnPlay()
                        else:
                                self.label_2.setText("Поздравляю, вы выиграли!")
                                Computer_Choice_Text = Choice(Computer_Choice)
                                self.label_3.setText(f"Компьютер выбрал {Computer_Choice_Text}!")
                                ReturnPlay()
                else:
                        self.label_3.setText("Выберите элемент!")

                
        
        self.pushButton_5.clicked.connect(GoPlay)

        self.pushButton_2.clicked.connect(stone)
        self.pushButton_3.clicked.connect(scissors)
        self.pushButton_4.clicked.connect(paper)

        self.pushButton.clicked.connect(ClickNext)
        self.pushButton_6.clicked.connect(ClickStart)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
