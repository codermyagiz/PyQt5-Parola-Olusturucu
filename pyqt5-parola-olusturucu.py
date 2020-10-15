import os
import sys
import random
import string
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(400, 300) #Bu değerin dışında boyutta herhangi bir değişiklik yapılamaz.
        self.setWindowTitle("Parola Oluşturucu") #Pencere Başlığı

        self.isimText = QLabel(self)
        self.isimText.setText('İsim:')
        self.isim = QLineEdit(self)

        self.soyadText = QLabel(self)
        self.soyadText.setText("Soyad: ")
        self.soyad = QLineEdit(self)

        self.tarihNum = QLabel(self)
        self.tarihNum.setText("D. Yılınız: ")
        self.tarih = QLineEdit(self)

        #Başlangıç: Boyutlandırma İşlemleri
        self.isim.move(80, 20)
        self.isim.resize(200, 32)
        self.isimText.move(20, 20)

        self.soyad.move(80, 60)
        self.soyad.resize(200,32)
        self.soyadText.move(20, 60)

        self.tarih.move(80, 100)
        self.tarih.resize(200, 32)
        self.tarihNum.move(20, 100)

        self.parola_sabit = QtWidgets.QLabel(self)
        self.parola_sabit.setGeometry(QtCore.QRect(80, 160, 201, 111))

        self.parola_sabit.setText("Size Önerebileceğimiz Parola:")

        self.parola_text = QtWidgets.QLabel(self)
        self.parola_text.setGeometry(QtCore.QRect(80, 180, 201, 111))

        self.parola_text.setText("")

        #Buton Tanım Başlangıç
        pybutton = QPushButton('Oluştur', self)
        pybutton.clicked.connect(self.parola_olustur) #parola_olustur fonksiyonuna bağlandı.
        pybutton.resize(200,32)
        pybutton.move(80, 140)


        copy_clipboard = QPushButton("Kopyala", self)
        copy_clipboard.clicked.connect(self.copy_pw) #copy_pw fonksiyonuna bağlandı
        copy_clipboard.resize(60,32)
        copy_clipboard.move(230, 220)

        #Buton Tanımlama Bitiş
        #Bitiş: Boyutlandırma İşlemleri

    #Parola Oluşturma fonksiyonu
    def parola_olustur(self):
        alfabe = string.ascii_letters
        sayilar = string.digits

        uzunluk_parola = 15

        def convertTuple(tup):
            str =  ''.join(tup)
            return str

        def split(word):
            return [char for char in word]

        yasakli_küme = ()
        sifre_kume = ()
        en_yeni_küme = ()

        yasak_ad = split(self.isim.text()) #Heceleniyor
        yasak_soyad = split(self.soyad.text()) #Heceleniyor
        yasak_tarih = split(self.tarih.text()) #Heceleniyor

        p =  "".join(random.sample(sayilar+alfabe,uzunluk_parola ))
        x = split(p) #Heceleniyor
        yasakli_küme = set(yasak_ad+yasak_soyad+yasak_tarih) #yasakli_küme set ediliyor.
        sifre_küme = set(x) #sifre_küme set ediliyor.
        en_yeni_küme = (sifre_küme - yasakli_küme) #Kümelerin farkı alınıp ad,soyad,tarih karakterleri hariç tutuluyor.
        global en_yeni_kume_string
        en_yeni_kume_string = convertTuple(en_yeni_küme)
        self.parola_text.setText(en_yeni_kume_string) #Parola ekrana yazdırılıyor.
    def copy_pw(self):
        clipb = QApplication.clipboard()
        clipb.clear(mode=clipb.Clipboard)
        clipb.setText(en_yeni_kume_string, mode=clipb.Clipboard)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
