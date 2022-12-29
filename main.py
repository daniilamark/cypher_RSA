import random
from PyQt6 import QtWidgets, QtCore, QtGui
import sys

from PyQt6.QtWidgets import QFileDialog, QApplication

from rsa.rsa import generate_keys, decrypt_message, encrypt_message
from sha_256.hash_sha_256 import sha_256
from ui.main_win import Ui_MainWindow
from ui.rsa_win import Ui_RsaWindow
from ui.sha_win import Ui_ShaWindow
from ui.vigenere_win import Ui_VigenereWindow
from vigenere.vigenere_algorithm import vigenere_encrypt, vigenere_decrypt


class RsaWindow(QtWidgets.QMainWindow, Ui_RsaWindow):
    def __init__(self):
        super(RsaWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('private_key.ico'))

        # tab_generate_keys
        self.btn_random_prime_nums.clicked.connect(self.insertGenerateRandomPrimeNum)
        self.btn_generate_keys.clicked.connect(self.generateKeys)
        self.btn_clear_all_gen_key.clicked.connect(self.clearAllGenKey)
        self.btn_save_generated_keys.clicked.connect(self.saveGeneratedKeys)

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

        self.btn_exit_in_main.clicked.connect(self.exitInMain)
        self.btn_exit_in_main_2.clicked.connect(self.exitInMain)
        self.btn_exit_in_main_3.clicked.connect(self.exitInMain)

    # tab_generate_keys

    def insertGenerateRandomPrimeNum(self):
        try:
            max_prime_num = int(self.sb_max_prime_num.text())
            first = str(generateRandomPrimeNum(0, max_prime_num))
            self.le_first_prime_num.setText(str(first))
            second = str(generateRandomPrimeNum(0, max_prime_num))
            self.le_second_prime_num.setText(second)

            self.statusbar.showMessage("Числа сгенерированы успешно")
        except:
            self.statusbar.showMessage("Ошибка при генерации ключей. Выберите большее максимальное число")

    def generateKeys(self):
        try:
            first_prime_num = int(self.le_first_prime_num.text())
            second_prime_num = int(self.le_second_prime_num.text())

            first_prime_num_is_prime = isPrime(first_prime_num)
            second_prime_num_is_prime = isPrime(second_prime_num)

            if first_prime_num_is_prime and second_prime_num_is_prime:
                n, e, d = generate_keys(first_prime_num, second_prime_num)

            self.te_generated_keys.setText(f"Открытый ключ:\nN: {n}\ne: {e}\n" + f"Закрытый ключ:\nN: {n}\nd: {d}\n")
            self.statusbar.showMessage("")

        except:
            self.statusbar.showMessage("Введите значения простых чисел или воспользуйтесь генерацией!")

    def clearAllGenKey(self):
        self.le_first_prime_num.setText("")
        self.le_second_prime_num.setText("")
        self.te_generated_keys.setText("")
        self.statusbar.showMessage("")

    def saveGeneratedKeys(self):
        try:
            filename = QFileDialog.getSaveFileName(self, 'Сохранить файл')

            if filename[0]:
                f = open(filename[0] + ".txt", 'w')

                with f:
                    f.write(str(self.te_generated_keys.toPlainText()))
        except:
            self.statusbar.showMessage("Файл не сохранён")

    def exitInMain(self):
        self.hide()

    # tab_encrypt
    def pasteKeysEncrypt(self):
        try:
            n, e, d = generate_keys(int(self.le_first_prime_num.text()), int(self.le_second_prime_num.text()))
            self.le_public_key_n.setText(str(n))
            self.le_public_key_e.setText(str(e))
        except:
            self.statusbar.showMessage("Ключи не вставлены. Введите или сгенерируйте ключи")

    def encryptMessage(self):
        try:
            if self.te_message_encrypt.toPlainText() == "":
                self.statusbar.showMessage("Сообщение не защифровано. Введите сообщение")
            else:
                self.statusbar.showMessage("")
            res = encrypt_message(self.te_message_encrypt.toPlainText(),
                                  int(self.le_public_key_n.text()),
                                  int(self.le_public_key_e.text()))
            self.te_message_encrypt_result.setText(res)

        except:
            self.statusbar.showMessage("Сообщение не защифровано. Введите ключи")

    def clearAllEncrypt(self):
        self.le_public_key_n.setText("")
        self.le_public_key_e.setText("")
        self.te_message_encrypt.setText("")
        self.te_message_encrypt_result.setText("")
        self.statusbar.showMessage("")

    def downloadEncrypt(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Открытие файла')

            if filename[0]:
                f = open(filename[0], 'r')

                with f:
                    data = f.read()
                    self.te_message_encrypt.setText(data)
        except:
            self.statusbar.showMessage("Файл не загружен")

    def saveEncrypt(self):
        try:
            filename = QFileDialog.getSaveFileName(self, 'Сохранение файла')

            if filename[0]:
                f = open(filename[0] + ".txt", 'w')

                with f:
                    f.write(str(self.te_message_encrypt_result.toPlainText()))
        except:
            self.statusbar.showMessage("Файл не сохранён")

    # tab_decrypt
    def pasteKeysDecrypt(self):
        try:
            if self.te_message_decrypt.toPlainText() == "":
                self.statusbar.showMessage("Сообщение не дешифровано. Введите сообщение")
            else:
                self.statusbar.showMessage("")
            n, e, d = generate_keys(int(self.le_first_prime_num.text()), int(self.le_second_prime_num.text()))
            self.le_private_key_n.setText(str(n))
            self.le_private_key_d.setText(str(d))
        except:
            self.statusbar.showMessage("Ключи не вставлены. Введите или сгенерируйте ключи")

    def decryptMessage(self):
        try:
            res = decrypt_message(self.te_message_decrypt.toPlainText(),
                                  int(self.le_private_key_n.text()),
                                  int(self.le_private_key_d.text()))
            self.te_message_decrypt_result.setText(res)
        except:
            self.statusbar.showMessage("Сообщение не дешифровано. Введите ключи")

    def clearAllDecrypt(self):
        self.le_private_key_n.setText("")
        self.le_private_key_d.setText("")
        self.te_message_decrypt.setText("")
        self.te_message_decrypt_result.setText("")
        self.statusbar.showMessage("")

    def downloadDecrypt(self):
        filename = QFileDialog.getOpenFileName(self, 'Открытие файла')

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.te_message_decrypt.setText(data)

    def saveDencrypt(self):
        filename = QFileDialog.getSaveFileName(self, 'Сохранение файла')

        if filename[0]:
            f = open(filename[0] + ".txt", 'w')

            with f:
                f.write(str(self.te_message_decrypt_result.toPlainText()))


class VigenereWindow(QtWidgets.QMainWindow, Ui_VigenereWindow):
    def __init__(self):
        super(VigenereWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('private_key.ico'))

        # tab_encrypt
        self.btn_encrypt.clicked.connect(self.encryptMessage)
        self.btn_clear_all_encrypt.clicked.connect(self.clearAllEncrypt)
        self.btn_download_encrypt.clicked.connect(self.downloadEncrypt)
        self.btn_save_encrypt.clicked.connect(self.saveEncrypt)

        # tab_decrypt
        self.btn_decrypt.clicked.connect(self.decryptMessage)
        self.btn_clear_all_decrypt.clicked.connect(self.clearAllDecrypt)
        self.btn_download_decrypt.clicked.connect(self.downloadDecrypt)
        self.btn_save_decrypt.clicked.connect(self.saveDecrypt)

        self.btn_exit_in_main_1.clicked.connect(self.exitInMain)
        self.btn_exit_in_main_2.clicked.connect(self.exitInMain)

    # tab_encrypt
    def encryptMessage(self):
        try:
            if self.te_message_encrypt.toPlainText() == "":
                self.statusbar.showMessage("Сообщение не защифровано. Введите сообщение")
            else:
                self.statusbar.showMessage("")
            res = vigenere_encrypt(str(self.te_message_encrypt.toPlainText()), str(self.le_key_encrypt.text()))
            print(res)
            self.te_message_encrypt_result.setText(res)

        except:
            self.statusbar.showMessage("Сообщение не защифровано. Введите ключи")

    def clearAllEncrypt(self):
        self.le_key_encrypt.setText("")
        self.te_message_encrypt.setText("")
        self.te_message_encrypt_result.setText("")
        self.statusbar.showMessage("")

    def downloadEncrypt(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Открытие файла')

            if filename[0]:
                f = open(filename[0], 'r')

                with f:
                    data = f.read()
                    self.te_message_encrypt.setText(data)
        except:
            self.statusbar.showMessage("Файл не загружен")

    def saveEncrypt(self):
        try:
            filename = QFileDialog.getSaveFileName(self, 'Сохранение файла')

            if filename[0]:
                f = open(filename[0] + ".txt", 'w')

                with f:
                    f.write(str(self.te_message_encrypt_result.toPlainText()))
        except:
            self.statusbar.showMessage("Файл не сохранён")

    # tab_decrypt

    def decryptMessage(self):
        try:
            res = vigenere_decrypt(str(self.te_message_decrypt.toPlainText()), str(self.le_key_decrypt.text()))
            self.te_message_decrypt_result.setText(res)
        except:
            self.statusbar.showMessage("Сообщение не дешифровано. Введите ключи")

    def clearAllDecrypt(self):
        self.le_key_decrypt.setText("")
        self.te_message_decrypt.setText("")
        self.te_message_decrypt_result.setText("")
        self.statusbar.showMessage("")

    def downloadDecrypt(self):
        filename = QFileDialog.getOpenFileName(self, 'Открытие файла')

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.te_message_decrypt.setText(data)

    def saveDecrypt(self):
        filename = QFileDialog.getSaveFileName(self, 'Сохранение файла')

        if filename[0]:
            f = open(filename[0] + ".txt", 'w')

            with f:
                f.write(str(self.te_message_decrypt_result.toPlainText()))

    def exitInMain(self):
        self.hide()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window_rsa = RsaWindow()
        self.window_vigenere = VigenereWindow()
        self.window_sha = ShaWindow()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('private_key.ico'))

        self.btn_open_rsa.clicked.connect(self.openRsaWindow)
        self.btn_open_vigenere.clicked.connect(self.openVigenereWindow)
        self.btn_open_hash.clicked.connect(self.openShaWindow)

    def openRsaWindow(self):
        if self.window_rsa.isVisible():
            self.window_rsa.hide()
        else:
            self.window_rsa.show()

    def openVigenereWindow(self):
        if self.window_vigenere.isVisible():
            self.window_vigenere.hide()
        else:
            self.window_vigenere.show()

    def openShaWindow(self):
        if self.window_sha.isVisible():
            self.window_sha.hide()
        else:
            self.window_sha.show()

class ShaWindow(QtWidgets.QMainWindow, Ui_ShaWindow):
    def __init__(self):
        super(ShaWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('private_key.ico'))

        self.btn_hash.clicked.connect(self.hash256)
        self.btn_clear_all.clicked.connect(self.clearAll)
        self.btn_download_text.clicked.connect(self.downloadText)
        self.btn_save_output_text.clicked.connect(self.saveText)
        self.btn_exit_in_main.clicked.connect(self.exitInMain)

    def hash256(self):
        try:
            if self.te_text_input.toPlainText() == "":
                self.statusbar.showMessage("Текст не захеширован. Введите текст")
            else:
                self.statusbar.showMessage("")
            res = str(sha_256(self.te_text_input.toPlainText()))
            self.te_text_output.setText(res)

        except:
            self.statusbar.showMessage("Текст не захеширован. Введите текст")

    def clearAll(self):
        self.te_text_input.setText("")
        self.te_text_output.setText("")

    def downloadText(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Открытие файла')

            if filename[0]:
                f = open(filename[0], 'r')

                with f:
                    data = f.read()
                    self.te_text_input.setText(data)
        except:
            self.statusbar.showMessage("Файл не загружен")

    def saveText(self):
        try:
            filename = QFileDialog.getSaveFileName(self, 'Сохранение файла')

            if filename[0]:
                f = open(filename[0] + ".txt", 'w')

                with f:
                    f.write(str(self.te_text_output.toPlainText()))
        except:
            self.statusbar.showMessage("Файл не сохранён")

    def exitInMain(self):
        self.hide()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

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
