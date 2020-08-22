import os
import sys
import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

os.system("cls") #Konsolun temizlenmesi için

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(400, 300) #Bu değerin dışında boyutta herhangi bir değişiklik yapılamaz.
        self.setWindowTitle("Parola Oluşturucu") #Pencere Başlığı ayarlanıyor

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
        pybutton.clicked.connect(self.parola_olustur) #parola_olustur fonksiyonu çalıştırılıyor.
        pybutton.resize(200,32)
        pybutton.move(80, 140)
        #Buton Tanımlama Bitiş

        #Bitiş: Boyutlandırma İşlemleri

    #Parola Oluşturma fonksiyonu
    def parola_olustur(self):
        alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z']
        sayilar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        alfa_sayisal_degil=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        uzunluk_parola = 15

        def convertTuple(tup):  #Bu fonksiyon geeksforgeeks'ten alındı. https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            str =  ''.join(tup)
            return str

        def split(word): #Bu fonksiyon geeksforgeeks'tan alındı. https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
            return [char for char in word]

        yasakli_küme = ()
        sifre_kume = ()
        en_yeni_küme = ()

        yasak_ad = split(self.isim.text()) #Heceleniyor
        yasak_soyad = split(self.soyad.text()) #Heceleniyor
        yasak_tarih = split(self.tarih.text()) #Heceleniyor

        p =  "".join(random.sample(sayilar+alfabe+alfa_sayisal_degil,uzunluk_parola ))
        x = split(p) #Heceleniyor
        yasakli_küme = set(yasak_ad+yasak_soyad+yasak_tarih) #yasakli_küme set ediliyor.
        sifre_küme = set(x) #sifre_küme set ediliyor.
        en_yeni_küme = (sifre_küme - yasakli_küme) #Kümelerin farkı alınıp ad,soyad,tarih karakterleri hariç tutuluyor.
        en_yeni_küme_string = convertTuple(en_yeni_küme)
        self.parola_text.setText(en_yeni_küme_string) #Parola ekrana yazdırılıyor.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
