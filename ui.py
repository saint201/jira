
from PyQt5 import QtCore, QtGui, QtWidgets
import multiprocessing
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from util import *
import os

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))



multiprocessing.freeze_support()
class Ui_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        global historyList 
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(540, 420)
        Dialog.setWindowIcon(QtGui.QIcon('files/icon.png'))
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(77, 77, 77);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 545, 425))
        
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: -1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(58, 58, 58);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #FFFFFF;\n"
"    border-style: dashed;\n"
"    padding: 2px;\n"
"    font: bold 14px;\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    border-color:rgb(131, 131, 131);\n"
"    color: rgb(152, 152, 152);\n"
"}\n"
"QPushButton:focus {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #FFFFFF;\n"
"    border-style: dashed;\n"
"    padding: 2px;\n"
"    font: bold 16px;\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(209, 209, 209);\n"
"    color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.LOGO = QtWidgets.QLabel(self.tab)
        self.LOGO.setGeometry(QtCore.QRect(25, 0, 300, 250))
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap("files/icon.png"))
        self.LOGO.setObjectName("LOGO")
        icon = QtGui.QIcon()
        #icon = QIcon(os.path.join(CURRENT_DIRECTORY+"/files/icon.png"))
        icon.addFile(("files/icon1.png"), QtCore.QSize(16,16))
        icon.addFile(("files/icon1.png"), QtCore.QSize(24,24))
        icon.addFile(("files/icon1.png"), QtCore.QSize(32,32))
        icon.addFile(("files/icon1.png"), QtCore.QSize(48,48))
        icon.addFile(("files/icon1.png"), QtCore.QSize(256,256))
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)
        #self.tray_icon.setIcon(
        #    self.style().standardIcon(QStyle.SP_ComputerIcon))
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(Dialog.show)
        hide_action.triggered.connect(Dialog.hide)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.token = QtWidgets.QLineEdit(self.tab)
        self.token.setGeometry(QtCore.QRect(10, 260, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.token.setFont(font)
        self.token.setMaxLength(200)
        self.token.setEchoMode(QtWidgets.QLineEdit.Password)
        self.token.setObjectName("token")
        self.startWW = QtWidgets.QCheckBox(self.tab)
        self.startWW.setGeometry(QtCore.QRect(310, 50, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startWW.setFont(font)
        if getStartState():
            self.startWW.setCheckState(2)
            self.start_bot(Dialog)
        else:self.startWW.setCheckState(0)
        self.startWW.setObjectName("startWW")
        self.startWW.clicked.connect(lambda: setStartState(self.startWW.isChecked()))

        self.sendToTray = QtWidgets.QPushButton(self.tab)
        self.sendToTray.setGeometry(QtCore.QRect(310, 20, 200, 23))
        self.sendToTray.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendToTray.setObjectName("stopBut")
        self.sendToTray.clicked.connect(lambda: Dialog.hide())

        self.stopBut = QtWidgets.QPushButton(self.tab)
        self.stopBut.setGeometry(QtCore.QRect(160, 310, 75, 23))
        self.stopBut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopBut.setObjectName("stopBut")
        self.stopBut.clicked.connect(lambda: self.stop_bot(Dialog))
        self.runBut = QtWidgets.QPushButton(self.tab)
        self.runBut.setGeometry(QtCore.QRect(60, 310, 75, 23))
        self.runBut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runBut.setObjectName("runBut")
        self.runBut.clicked.connect(lambda: self.start_bot(Dialog))
        self.ruseresonly = QtWidgets.QCheckBox(self.tab)
        self.ruseresonly.setGeometry(QtCore.QRect(310, 90, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ruseresonly.setFont(font)
        self.ruseresonly.setObjectName("ruseresonly")
        self.savehistory = QtWidgets.QCheckBox(self.tab)
        self.savehistory.setGeometry(QtCore.QRect(310, 130, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.savehistory.setFont(font)
        self.savehistory.setChecked(True)
        self.savehistory.setObjectName("savehistory")
        self.notify = QtWidgets.QCheckBox(self.tab)
        self.notify.setGeometry(QtCore.QRect(310, 170, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.notify.setFont(font)
        self.notify.setChecked(True)
        self.notify.setObjectName("notify")
        self.applyBut = QtWidgets.QPushButton(self.tab)
        self.applyBut.setGeometry(QtCore.QRect(250, 260, 51, 31))
        self.applyBut.setObjectName("applyBut")
        self.applyBut.clicked.connect(self.writeToken)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        historyList = QtWidgets.QListWidget(self.tab_3)
        historyList.setGeometry(QtCore.QRect(0, 0, 540, 341))
        historyList.setObjectName("historyList")
        self.filterLine = QtWidgets.QLineEdit(self.tab_3)
        self.filterLine.setGeometry(QtCore.QRect(150, 350, 230, 25))
        self.filterLine.setObjectName("filterLine")
        self.findBut = QtWidgets.QPushButton(self.tab_3)
        self.findBut.setGeometry(QtCore.QRect(380, 350, 150, 25))
        self.findBut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findBut.setObjectName("findBut")
        self.findBut.clicked.connect(self.findHistory)
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.tabBarClicked.connect(self.handle_tabbar_clicked)
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        global historyList 
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jira | status - run"))
        self.token.setText(_translate("Dialog", getToken()))
        self.token.setPlaceholderText(_translate("Dialog", "TOKEN"))
        self.startWW.setText(_translate("Dialog", "start with windows"))
        self.stopBut.setText(_translate("Dialog", "STOP"))
        self.sendToTray.setText(_translate("Dialog", "SEND TO TRAY"))
        self.applyBut.setText(_translate("Dialog", "apply"))
        self.runBut.setText(_translate("Dialog", "RUN"))
        self.ruseresonly.setText(_translate("Dialog", "registered users only"))
        self.savehistory.setText(_translate("Dialog", "save message history"))
        self.notify.setText(_translate("Dialog", "notify registered users "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "setup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "config"))
        self.filterLine.setPlaceholderText(_translate("Dialog", "filter"))
        self.findBut.setText(_translate("Dialog", "FIND / REFRESH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "history"))
        __sortingEnabled = historyList.isSortingEnabled()
        historyList.setSortingEnabled(False)
        historyList.setSortingEnabled(__sortingEnabled)

    def findHistory(self):
        _translate = QtCore.QCoreApplication.translate
        if "" !=self.filterLine.text():
            historyList.clear()
            filtredHistory = []
            for i in readhistory():
                if self.filterLine.text() in i:
                    filtredHistory.append(i)
            self.update_history_list(filtredHistory)
        else:
            historyList.clear()
            self.update_history_list(readhistory())

    def handle_tabbar_clicked(self, index):
        if index == 2:
            historyList.clear()
            self.update_history_list(readhistory())
    def update_history_list(self,list):
        
        _translate = QtCore.QCoreApplication.translate
        for index, i in enumerate(list):
                item = QtWidgets.QListWidgetItem()
                historyList.addItem(item)
                item = historyList.item(index)
                item.setText(_translate("Dialog", i))
    def stop_bot(self, Dialog):
        try:
            if p.is_alive():
                p.terminate()
                p.kill()
        except:pass
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jira | status - stoped"))

    def start_bot(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        global p
        from main import starter

        try:
            if not p.is_alive():
                p = multiprocessing.Process(target=starter,args=(getToken(),))
                p.start()
        except:
            p = multiprocessing.Process(target=starter,args=(getToken(),))
            p.start()
        Dialog.setWindowTitle(_translate("Dialog", "Jira | status - run"))

    
    def writeToken(self):
        setToken(self.token.text())
        
def start_ui():
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    
    sys.exit(app.exec_())
    

    
    

if __name__ == "__main__":
    start_ui()