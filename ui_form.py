# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QTreeView, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 310, 80, 21))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(620, 310, 151, 21))
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 350, 781, 241))
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 381, 281))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, -1, 381, 261))
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 381, 261))
        self.tabLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.tabLayout.setObjectName(u"tabLayout")
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.sqlTextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.sqlTextEdit.setObjectName(u"sqlTextEdit")

        self.tabLayout.addWidget(self.sqlTextEdit)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 381, 261))
        self.verticalLayoutWidget_2 = QWidget(self.widget_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 381, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.verticalLayoutWidget_2)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEnabled(True)
        self.treeView.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout.addWidget(self.treeView)

        self.horizontalLayoutWidget = QWidget(self.widget_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 230, 381, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(16777215, 51))

        self.horizontalLayout.addWidget(self.label)

        self.whereTextEdit = QPlainTextEdit(self.horizontalLayoutWidget)
        self.whereTextEdit.setObjectName(u"whereTextEdit")

        self.horizontalLayout.addWidget(self.whereTextEdit)

        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox = QComboBox(Widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(400, 30, 171, 22))
        self.comboBox_2 = QComboBox(Widget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(610, 30, 171, 22))
        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(400, 60, 171, 231))
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget_2 = QListWidget(Widget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(610, 60, 171, 231))
        self.listWidget_2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(410, 310, 151, 20))

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Data Model Translator", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Run Query", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Generate Data Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Conditions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Tab 2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Join columns", None))
    # retranslateUi

