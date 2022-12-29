# Form implementation generated from reading ui file 'rsa_win.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RsaWindow(object):
    def setupUi(self, RsaWindow):
        RsaWindow.setObjectName("RsaWindow")
        RsaWindow.resize(600, 400)
        RsaWindow.setMinimumSize(QtCore.QSize(600, 400))
        RsaWindow.setMaximumSize(QtCore.QSize(600, 400))
        RsaWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(RsaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_generate_keys = QtWidgets.QWidget()
        self.tab_generate_keys.setObjectName("tab_generate_keys")
        self.btn_random_prime_nums = QtWidgets.QPushButton(self.tab_generate_keys)
        self.btn_random_prime_nums.setGeometry(QtCore.QRect(240, 200, 131, 23))
        self.btn_random_prime_nums.setObjectName("btn_random_prime_nums")
        self.te_generated_keys = QtWidgets.QTextEdit(self.tab_generate_keys)
        self.te_generated_keys.setGeometry(QtCore.QRect(240, 10, 341, 111))
        self.te_generated_keys.setObjectName("te_generated_keys")
        self.le_second_prime_num = QtWidgets.QLineEdit(self.tab_generate_keys)
        self.le_second_prime_num.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.le_second_prime_num.setInputMask("")
        self.le_second_prime_num.setText("")
        self.le_second_prime_num.setObjectName("le_second_prime_num")
        self.le_first_prime_num = QtWidgets.QLineEdit(self.tab_generate_keys)
        self.le_first_prime_num.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.le_first_prime_num.setInputMask("")
        self.le_first_prime_num.setText("")
        self.le_first_prime_num.setObjectName("le_first_prime_num")
        self.btn_generate_keys = QtWidgets.QPushButton(self.tab_generate_keys)
        self.btn_generate_keys.setGeometry(QtCore.QRect(10, 70, 211, 23))
        self.btn_generate_keys.setObjectName("btn_generate_keys")
        self.btn_clear_all_gen_key = QtWidgets.QPushButton(self.tab_generate_keys)
        self.btn_clear_all_gen_key.setGeometry(QtCore.QRect(10, 100, 211, 23))
        self.btn_clear_all_gen_key.setObjectName("btn_clear_all_gen_key")
        self.label = QtWidgets.QLabel(self.tab_generate_keys)
        self.label.setGeometry(QtCore.QRect(10, 200, 131, 21))
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.tab_generate_keys)
        self.line_3.setGeometry(QtCore.QRect(10, 180, 571, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.sb_max_prime_num = QtWidgets.QSpinBox(self.tab_generate_keys)
        self.sb_max_prime_num.setGeometry(QtCore.QRect(130, 200, 91, 22))
        self.sb_max_prime_num.setMaximum(10000)
        self.sb_max_prime_num.setProperty("value", 1000)
        self.sb_max_prime_num.setObjectName("sb_max_prime_num")
        self.label_2 = QtWidgets.QLabel(self.tab_generate_keys)
        self.label_2.setGeometry(QtCore.QRect(240, 170, 151, 21))
        self.label_2.setObjectName("label_2")
        self.btn_save_generated_keys = QtWidgets.QPushButton(self.tab_generate_keys)
        self.btn_save_generated_keys.setGeometry(QtCore.QRect(440, 130, 141, 23))
        self.btn_save_generated_keys.setObjectName("btn_save_generated_keys")
        self.btn_exit_in_main = QtWidgets.QPushButton(self.tab_generate_keys)
        self.btn_exit_in_main.setGeometry(QtCore.QRect(450, 320, 131, 23))
        self.btn_exit_in_main.setObjectName("btn_exit_in_main")
        self.tabWidget.addTab(self.tab_generate_keys, "")
        self.tab_encrypt = QtWidgets.QWidget()
        self.tab_encrypt.setObjectName("tab_encrypt")
        self.le_public_key_n = QtWidgets.QLineEdit(self.tab_encrypt)
        self.le_public_key_n.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.le_public_key_n.setInputMask("")
        self.le_public_key_n.setText("")
        self.le_public_key_n.setObjectName("le_public_key_n")
        self.le_public_key_e = QtWidgets.QLineEdit(self.tab_encrypt)
        self.le_public_key_e.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.le_public_key_e.setInputMask("")
        self.le_public_key_e.setText("")
        self.le_public_key_e.setObjectName("le_public_key_e")
        self.te_message_encrypt = QtWidgets.QTextEdit(self.tab_encrypt)
        self.te_message_encrypt.setGeometry(QtCore.QRect(240, 10, 341, 111))
        self.te_message_encrypt.setObjectName("te_message_encrypt")
        self.btn_encrypt = QtWidgets.QPushButton(self.tab_encrypt)
        self.btn_encrypt.setGeometry(QtCore.QRect(10, 100, 211, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_download_encrypt = QtWidgets.QPushButton(self.tab_encrypt)
        self.btn_download_encrypt.setGeometry(QtCore.QRect(440, 130, 141, 23))
        self.btn_download_encrypt.setObjectName("btn_download_encrypt")
        self.btn_save_encrypt = QtWidgets.QPushButton(self.tab_encrypt)
        self.btn_save_encrypt.setGeometry(QtCore.QRect(10, 320, 141, 23))
        self.btn_save_encrypt.setObjectName("btn_save_encrypt")
        self.btn_clear_all_encrypt = QtWidgets.QPushButton(self.tab_encrypt)
        self.btn_clear_all_encrypt.setGeometry(QtCore.QRect(10, 130, 211, 23))
        self.btn_clear_all_encrypt.setObjectName("btn_clear_all_encrypt")
        self.btn_paste_key_encrypt = QtWidgets.QPushButton(self.tab_encrypt)
        self.btn_paste_key_encrypt.setGeometry(QtCore.QRect(10, 70, 211, 23))
        self.btn_paste_key_encrypt.setObjectName("btn_paste_key_encrypt")
        self.te_message_encrypt_result = QtWidgets.QTextEdit(self.tab_encrypt)
        self.te_message_encrypt_result.setGeometry(QtCore.QRect(10, 190, 571, 111))
        self.te_message_encrypt_result.setObjectName("te_message_encrypt_result")
        self.line = QtWidgets.QFrame(self.tab_encrypt)
        self.line.setGeometry(QtCore.QRect(10, 170, 571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.btn_exit_in_main_2 = QtWidgets.QPushButton(self.tab_encrypt)
        self.btn_exit_in_main_2.setGeometry(QtCore.QRect(450, 320, 131, 23))
        self.btn_exit_in_main_2.setObjectName("btn_exit_in_main_2")
        self.tabWidget.addTab(self.tab_encrypt, "")
        self.tab_decrypt = QtWidgets.QWidget()
        self.tab_decrypt.setObjectName("tab_decrypt")
        self.te_message_decrypt = QtWidgets.QTextEdit(self.tab_decrypt)
        self.te_message_decrypt.setGeometry(QtCore.QRect(240, 10, 341, 111))
        self.te_message_decrypt.setObjectName("te_message_decrypt")
        self.le_private_key_d = QtWidgets.QLineEdit(self.tab_decrypt)
        self.le_private_key_d.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.le_private_key_d.setInputMask("")
        self.le_private_key_d.setText("")
        self.le_private_key_d.setObjectName("le_private_key_d")
        self.le_private_key_n = QtWidgets.QLineEdit(self.tab_decrypt)
        self.le_private_key_n.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.le_private_key_n.setInputMask("")
        self.le_private_key_n.setText("")
        self.le_private_key_n.setObjectName("le_private_key_n")
        self.btn_decrypt = QtWidgets.QPushButton(self.tab_decrypt)
        self.btn_decrypt.setGeometry(QtCore.QRect(10, 100, 211, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_save_decrypt = QtWidgets.QPushButton(self.tab_decrypt)
        self.btn_save_decrypt.setGeometry(QtCore.QRect(10, 320, 141, 23))
        self.btn_save_decrypt.setObjectName("btn_save_decrypt")
        self.btn_download_decrypt = QtWidgets.QPushButton(self.tab_decrypt)
        self.btn_download_decrypt.setGeometry(QtCore.QRect(440, 130, 141, 23))
        self.btn_download_decrypt.setObjectName("btn_download_decrypt")
        self.btn_clear_all_decrypt = QtWidgets.QPushButton(self.tab_decrypt)
        self.btn_clear_all_decrypt.setGeometry(QtCore.QRect(10, 130, 211, 23))
        self.btn_clear_all_decrypt.setObjectName("btn_clear_all_decrypt")
        self.btn_paste_key_decrypt = QtWidgets.QPushButton(self.tab_decrypt)
        self.btn_paste_key_decrypt.setGeometry(QtCore.QRect(10, 70, 211, 23))
        self.btn_paste_key_decrypt.setObjectName("btn_paste_key_decrypt")
        self.line_2 = QtWidgets.QFrame(self.tab_decrypt)
        self.line_2.setGeometry(QtCore.QRect(10, 170, 571, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.te_message_decrypt_result = QtWidgets.QTextEdit(self.tab_decrypt)
        self.te_message_decrypt_result.setGeometry(QtCore.QRect(10, 190, 571, 111))
        self.te_message_decrypt_result.setObjectName("te_message_decrypt_result")
        self.btn_exit_in_main_3 = QtWidgets.QPushButton(self.tab_decrypt)
        self.btn_exit_in_main_3.setGeometry(QtCore.QRect(450, 320, 131, 23))
        self.btn_exit_in_main_3.setObjectName("btn_exit_in_main_3")
        self.tabWidget.addTab(self.tab_decrypt, "")
        RsaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RsaWindow)
        self.statusbar.setObjectName("statusbar")
        RsaWindow.setStatusBar(self.statusbar)
        self.action_main = QtGui.QAction(RsaWindow)
        self.action_main.setObjectName("action_main")
        self.action_vigenere = QtGui.QAction(RsaWindow)
        self.action_vigenere.setObjectName("action_vigenere")

        self.retranslateUi(RsaWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RsaWindow)

    def retranslateUi(self, RsaWindow):
        _translate = QtCore.QCoreApplication.translate
        RsaWindow.setWindowTitle(_translate("RsaWindow", "RSA-шифровальщик"))
        self.btn_random_prime_nums.setText(_translate("RsaWindow", "Заполнить случайно"))
        self.te_generated_keys.setPlaceholderText(_translate("RsaWindow", "Сгенерированные ключи"))
        self.le_second_prime_num.setPlaceholderText(_translate("RsaWindow", "Второе простое число"))
        self.le_first_prime_num.setPlaceholderText(_translate("RsaWindow", "Первое простое число"))
        self.btn_generate_keys.setText(_translate("RsaWindow", "Сгенерировать ключи"))
        self.btn_clear_all_gen_key.setText(_translate("RsaWindow", "Очистить всё"))
        self.label.setText(_translate("RsaWindow", "Максимальное число:"))
        self.label_2.setText(_translate("RsaWindow", "Генерация простых чисел"))
        self.btn_save_generated_keys.setText(_translate("RsaWindow", "Сохранить"))
        self.btn_exit_in_main.setText(_translate("RsaWindow", "В меню"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_generate_keys), _translate("RsaWindow", "Генерация ключей"))
        self.le_public_key_n.setPlaceholderText(_translate("RsaWindow", "Открытый ключ n"))
        self.le_public_key_e.setPlaceholderText(_translate("RsaWindow", "Открытый ключ e"))
        self.te_message_encrypt.setPlaceholderText(_translate("RsaWindow", "Сообщение"))
        self.btn_encrypt.setText(_translate("RsaWindow", "Зашифровать сообщение"))
        self.btn_download_encrypt.setText(_translate("RsaWindow", "Загрузить"))
        self.btn_save_encrypt.setText(_translate("RsaWindow", "Сохранить"))
        self.btn_clear_all_encrypt.setText(_translate("RsaWindow", "Очистить всё"))
        self.btn_paste_key_encrypt.setText(_translate("RsaWindow", "Заполнить созданными ключами"))
        self.te_message_encrypt_result.setPlaceholderText(_translate("RsaWindow", "Результат шифрования"))
        self.btn_exit_in_main_2.setText(_translate("RsaWindow", "В меню"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_encrypt), _translate("RsaWindow", "Шифровать"))
        self.te_message_decrypt.setPlaceholderText(_translate("RsaWindow", "Сообщение"))
        self.le_private_key_d.setPlaceholderText(_translate("RsaWindow", "Закрытый ключ d"))
        self.le_private_key_n.setPlaceholderText(_translate("RsaWindow", "Закрытый ключ n"))
        self.btn_decrypt.setText(_translate("RsaWindow", "Дешифровать сообщение"))
        self.btn_save_decrypt.setText(_translate("RsaWindow", "Сохранить"))
        self.btn_download_decrypt.setText(_translate("RsaWindow", "Загрузить"))
        self.btn_clear_all_decrypt.setText(_translate("RsaWindow", "Очистить всё"))
        self.btn_paste_key_decrypt.setText(_translate("RsaWindow", "Заполнить созданными ключами"))
        self.te_message_decrypt_result.setPlaceholderText(_translate("RsaWindow", "Результат дешифрования"))
        self.btn_exit_in_main_3.setText(_translate("RsaWindow", "В меню"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_decrypt), _translate("RsaWindow", "Дешифровать"))
        self.action_main.setText(_translate("RsaWindow", "Главное"))
        self.action_vigenere.setText(_translate("RsaWindow", "Шифр Виженера"))
