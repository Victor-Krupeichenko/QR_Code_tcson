# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QR_tcson.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import loev_tcson

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 450)
        Dialog.setMinimumSize(QSize(650, 450))
        Dialog.setMaximumSize(QSize(650, 450))
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setKerning(False)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/tcson.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Dialog.setStyleSheet(u"background-image: url(:/newPrefix/background.jpg);\n"
"\n"
"\n"
"")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 631, 121))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setKerning(True)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"#textEdit {\n"
"    color: #FFFFFF;\n"
"    font-weight: normal;\n"
"	outline: none;\n"
"    background-color: rgba(57, 30, 241, 0.1);\n"
"    border: none;\n"
"    font-weight: normal;\n"
"    font-style: italic;\n"
"	color: rgb(0, 0, 0);\n"
"    background: transparent;\n"
"}\n"
"")
        self.btn = QPushButton(Dialog)
        self.btn.setObjectName(u"btn")
        self.btn.setGeometry(QRect(260, 400, 151, 41))
        font2 = QFont()
        font2.setFamilies([u"Monotype Corsiva"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setKerning(True)
        self.btn.setFont(font2)
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setStyleSheet(u"#btn {\n"
"	padding: 0 0 0 0;\n"
"    border-radius: 10px;\n"
"    color: rgb(174, 29, 228);\n"
"    font: 14pt \"Monotype Corsiva\";\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"}\n"
"\n"
"#btn:hover {\n"
"    color: rgb(46, 139, 87);	\n"
"}")
        self.labelMyName = QLabel(Dialog)
        self.labelMyName.setObjectName(u"labelMyName")
        self.labelMyName.setGeometry(QRect(20, 410, 161, 21))
        self.labelMyName.setStyleSheet(u"QLabel {\n"
"    font: 14pt \"Mistral\";\n"
"    color: rgb(255, 255, 255);\n"
"    font-style: italic;\n"
"    /* \u041f\u041e\u041b\u041d\u041e\u0421\u0422\u042c\u042e \u0423\u0411\u0418\u0420\u0410\u0415\u0422 \u0424\u041e\u041d (\u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0433\u043e \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u043c) */\n"
"    background: transparent;\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0435\u0432\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u0440\u0438\u0442\u043e\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0446\u0435\u043d\u0442\u0440 \u2013 \u0441\u043e\u0437\u0434\u0430\u0442\u044c QR-\u043a\u043e\u0434", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u044e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442...", None))
        self.btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c QR-\u041a\u041e\u0414", None))
        self.labelMyName.setText(QCoreApplication.translate("Dialog", u"Victor Krupeichenko", None))
    # retranslateUi

