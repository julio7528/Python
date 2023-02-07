from mimetypes import init
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    
    def go_home(self):
        self.browser.setUrl(QUrl('https://www.ciccopn.pt/'))
    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self, url):
        self.url_bar.setText(url.toString())    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://firefox.com')
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #barra de navegação
        navbar = QToolBar ()
        self.addToolBar(navbar)

        #botao voltar 
        voltar_btn = QAction('<-', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn)

        #botao Actualizar
        actualizar_btn = QAction('actualizar', self)
        actualizar_btn.triggered.connect(self.browser.reload)
        navbar.addAction(actualizar_btn)
       
        # botao Home
        home_btn = QAction ('Home', self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

        #botao Avançar
        Avançar_btn = QAction('->', self)
        Avançar_btn.triggered.connect(self.browser.forward)
        navbar.addAction(Avançar_btn)


        #barra de endereco
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


app = QApplication(sys.argv)
QApplication.setApplicationName('Meu Browser')
windows = MainWindow() 
app.exec()       