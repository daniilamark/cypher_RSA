import random
from PyQt6 import QtWidgets, QtCore, QtGui
import sys

from PyQt6.QtWidgets import QFileDialog

from rsa.rsa import generate_keys, decrypt_message, encrypt_message
from ui.rsa_win import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('private_key.ico'))

        # tab_generate_keys
        self.btn_random_prime_nums.clicked.connect(self.insertGenerateRandomPrimeNum)
        self.btn_generate_keys.clicked.connect(self.generateKeys)
        self.btn_clear_all_gen_key.clicked.connect(self.clearAllGenKey)

        # tab_encrypt
        self.btn_paste_key_encrypt.clicked.connect(self.pasteKeysEncrypt)
        self.btn_encrypt.clicked.connect(self.encryptMessage)
        self.btn_clear_all_encrypt.clicked.connect(self.clearAllEncrypt)
        self.btn_download_encrypt.clicked.connect(self.downloadEncrypt)
        self.btn_save_encrypt.clicked.connect(self.saveEncrypt)

        # tab_decrypt
        self.btn_paste_key_decrypt.clicked.connect(self.pasteKeysDecrypt)
        self.btn_decrypt.clicked.connect(self.decryptMessage)
        self.btn_clear_all_decrypt.clicked.connect(self.clearAllDecrypt)
        self.btn_download_decrypt.clicked.connect(self.downloadDecrypt)
        self.btn_save_decrypt.clicked.connect(self.saveDencrypt)
    # tab_generate_keys

    def insertGenerateRandomPrimeNum(self):
        try:
            max_prime_num = int(self.sb_max_prime_num.text())
            self.btn_random_prime_nums.setEnabled(0)
            first = str(generateRandomPrimeNum(0, max_prime_num))
            self.le_first_prime_num.setText(str(first))

            second = str(generateRandomPrimeNum(0, max_prime_num))
            self.le_second_prime_num.setText(second)

            self.statusbar.showMessage("Числа сгенерированы успешно")
            self.btn_random_prime_nums.setEnabled(1)
        except:
            print("Ошибка при генерации ключей\n")
            self.statusbar.showMessage("Ошибка при генерации ключей")

    def generateKeys(self):
        try:
            # Generate values for encryption / decryption
            n, e, d = generate_keys(int(self.le_first_prime_num.text()), int(self.le_second_prime_num.text()))

            # Show keys
            print(f"Открытый ключ:\nN: {n}\ne: {e}\n")
            print(f"Закрытый ключ:\nN: {n}\nd: {d}\n")
            self.te_generated_keys.setText(f"Открытый ключ:\nN: {n}\ne: {e}\n" + f"Закрытый ключ:\nN: {n}\nd: {d}\n")
            #self.statusbar.showMessage("Ключи сгенерированы успешно")
            self.statusbar.showMessage("")

        except:
            print("Error: Invalid Primes\n")
            self.statusbar.showMessage("Введите значения простых чисел")

    def clearAllGenKey(self):
        self.le_first_prime_num.setText("")
        self.le_second_prime_num.setText("")
        self.te_generated_keys.setText("")
        self.statusbar.showMessage("")

    # tab_encrypt

    def pasteKeysEncrypt(self):
        try:
            n, e, d = generate_keys(int(self.le_first_prime_num.text()), int(self.le_second_prime_num.text()))
            self.le_public_key_n.setText(str(n))
            self.le_public_key_e.setText(str(e))
        except:
            print("Error: Invalid Primes\n")
            self.statusbar.showMessage("")

    def encryptMessage(self):
        try:
            res = encrypt_message(self.te_message_encrypt.toPlainText(),
                                  int(self.le_public_key_n.text()),
                                  int(self.le_public_key_e.text()))
            self.te_message_encrypt_result.setText(res)
        except:
            print("ошибка шифрования\n")
            self.statusbar.showMessage("")

    def clearAllEncrypt(self):
        self.le_public_key_n.setText("")
        self.le_public_key_e.setText("")
        self.te_message_encrypt.setText("")
        self.te_message_encrypt_result.setText("")
        self.statusbar.showMessage("")

    def downloadEncrypt(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.te_message_encrypt.setText(data)

    def saveEncrypt(self):
        filename = QFileDialog.getSaveFileName(self, 'Сохранить файл')

        if filename[0]:
            f = open(filename[0]+".txt", 'w')

            with f:
                f.write(str(self.te_message_encrypt_result.toPlainText()))

    # tab_decrypt
    def pasteKeysDecrypt(self):
        try:
            n, e, d = generate_keys(int(self.le_first_prime_num.text()), int(self.le_second_prime_num.text()))
            self.le_private_key_n.setText(str(n))
            self.le_private_key_d.setText(str(d))
        except:
            print("Error: Invalid Primes\n")
            self.statusbar.showMessage("Ошибка с ключами")

    def decryptMessage(self):
        try:
            res = decrypt_message(self.te_message_decrypt.toPlainText(),
                                  int(self.le_private_key_n.text()),
                                  int(self.le_private_key_d.text()))
            self.te_message_decrypt_result.setText(res)
        except:
            print("ошибка дешифрования\n")
            self.statusbar.showMessage("")

    def clearAllDecrypt(self):
        self.le_private_key_n.setText("")
        self.le_private_key_d.setText("")
        self.te_message_decrypt.setText("")
        self.te_message_decrypt_result.setText("")
        self.statusbar.showMessage("")

    def downloadDecrypt(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.te_message_decrypt.setText(data)

    def saveDencrypt(self):
        filename = QFileDialog.getSaveFileName(self, 'Сохранить файл')

        if filename[0]:
            f = open(filename[0]+".txt", 'w')

            with f:
                f.write(str(self.te_message_decrypt_result.toPlainText()))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


def generateRandomPrimeNum(min_prime, max_prime):
    cached_primes = [i for i in range(min_prime, max_prime) if isPrime(i)]
    random_prime_num = random.choice(cached_primes)

    return random_prime_num


def isPrime(x):
    count = 0
    for i in range(int(x / 2)):
        if x % (i + 1) == 0:
            count = count + 1
    return count == 1


if __name__ == '__main__':
    main()
