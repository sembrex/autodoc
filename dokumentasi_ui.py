# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dokumentasi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.inputFolder = QtGui.QLineEdit(self.centralwidget)
        self.inputFolder.setObjectName(_fromUtf8("inputFolder"))
        self.gridLayout_2.addWidget(self.inputFolder, 0, 1, 1, 1)
        self.btnOutput = QtGui.QToolButton(self.centralwidget)
        self.btnOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOutput.setObjectName(_fromUtf8("btnOutput"))
        self.gridLayout_2.addWidget(self.btnOutput, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.outputFolder = QtGui.QLineEdit(self.centralwidget)
        self.outputFolder.setObjectName(_fromUtf8("outputFolder"))
        self.gridLayout_2.addWidget(self.outputFolder, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnInput = QtGui.QToolButton(self.centralwidget)
        self.btnInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInput.setObjectName(_fromUtf8("btnInput"))
        self.gridLayout_2.addWidget(self.btnInput, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.btnLog = QtGui.QPushButton(self.centralwidget)
        self.btnLog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLog.setObjectName(_fromUtf8("btnLog"))
        self.verticalLayout_2.addWidget(self.btnLog)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.logs = QtGui.QPlainTextEdit(self.widget)
        self.logs.setReadOnly(True)
        self.logs.setObjectName(_fromUtf8("logs"))
        self.verticalLayout_3.addWidget(self.logs)
        self.verticalLayout_2.addWidget(self.widget)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.verticalLayout_2.addWidget(self.btnStart)
        self.btnExit = QtGui.QPushButton(self.centralwidget)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.verticalLayout_2.addWidget(self.btnExit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inputFolder, self.btnInput)
        MainWindow.setTabOrder(self.btnInput, self.outputFolder)
        MainWindow.setTabOrder(self.outputFolder, self.btnOutput)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dokumentasi", None))
        self.btnOutput.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Folder Sumber", None))
        self.label_2.setText(_translate("MainWindow", "File Hasil", None))
        self.btnInput.setText(_translate("MainWindow", "...", None))
        self.btnLog.setText(_translate("MainWindow", "Tampilkan Log", None))
        self.label_3.setText(_translate("MainWindow", "Log", None))
        self.btnStart.setText(_translate("MainWindow", "Mulai", None))
        self.btnExit.setText(_translate("MainWindow", "Keluar", None))

import resources_rc
