# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/src/import_settingsPage.ui'
#
# Created: Wed Nov 17 12:05:59 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_settingsPage(object):
    def setupUi(self, settingsPage):
        settingsPage.setObjectName("settingsPage")
        settingsPage.resize(500, 430)
        self.verticalLayout_2 = QtGui.QVBoxLayout(settingsPage)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(settingsPage)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(settingsPage)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.settingsStack = QtGui.QStackedWidget(settingsPage)
        self.settingsStack.setObjectName("settingsStack")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.databaseBox = QtGui.QComboBox(self.groupBox)
        self.databaseBox.setObjectName("databaseBox")
        self.verticalLayout_3.addWidget(self.databaseBox)
        self.databaseStack = QtGui.QStackedWidget(self.groupBox)
        self.databaseStack.setObjectName("databaseStack")
        self.sqlitePage = QtGui.QWidget()
        self.sqlitePage.setObjectName("sqlitePage")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.sqlitePage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtGui.QGroupBox(self.sqlitePage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setMargin(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.sqlite_fileLine = QtGui.QLineEdit(self.groupBox_2)
        self.sqlite_fileLine.setObjectName("sqlite_fileLine")
        self.horizontalLayout.addWidget(self.sqlite_fileLine)
        self.openFileButton = QtGui.QToolButton(self.groupBox_2)
        self.openFileButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/document-open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFileButton.setIcon(icon)
        self.openFileButton.setObjectName("openFileButton")
        self.horizontalLayout.addWidget(self.openFileButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 148, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.databaseStack.addWidget(self.sqlitePage)
        self.mysqlPage = QtGui.QWidget()
        self.mysqlPage.setObjectName("mysqlPage")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.mysqlPage)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_3 = QtGui.QGroupBox(self.mysqlPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setMargin(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mysql_userLine = QtGui.QLineEdit(self.groupBox_3)
        self.mysql_userLine.setObjectName("mysql_userLine")
        self.gridLayout_3.addWidget(self.mysql_userLine, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 3, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 3, 1, 1)
        self.mysql_portBox = QtGui.QSpinBox(self.groupBox_3)
        self.mysql_portBox.setMaximum(65535)
        self.mysql_portBox.setProperty("value", 3306)
        self.mysql_portBox.setObjectName("mysql_portBox")
        self.gridLayout_3.addWidget(self.mysql_portBox, 0, 4, 1, 1)
        self.mysql_databaseLine = QtGui.QLineEdit(self.groupBox_3)
        self.mysql_databaseLine.setObjectName("mysql_databaseLine")
        self.gridLayout_3.addWidget(self.mysql_databaseLine, 2, 1, 1, 1)
        self.mysql_passLine = QtGui.QLineEdit(self.groupBox_3)
        self.mysql_passLine.setEchoMode(QtGui.QLineEdit.Password)
        self.mysql_passLine.setObjectName("mysql_passLine")
        self.gridLayout_3.addWidget(self.mysql_passLine, 1, 4, 1, 1)
        self.mysql_hostLine = QtGui.QLineEdit(self.groupBox_3)
        self.mysql_hostLine.setObjectName("mysql_hostLine")
        self.gridLayout_3.addWidget(self.mysql_hostLine, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.databaseStack.addWidget(self.mysqlPage)
        self.verticalLayout_3.addWidget(self.databaseStack)
        self.verticalLayout.addWidget(self.groupBox)
        self.settingsStack.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.settingsStack.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.settingsStack)
        self.label_4.setBuddy(self.sqlite_fileLine)
        self.label_8.setBuddy(self.mysql_userLine)
        self.label_7.setBuddy(self.mysql_portBox)
        self.label_10.setBuddy(self.mysql_databaseLine)
        self.label_9.setBuddy(self.mysql_passLine)
        self.label_6.setBuddy(self.mysql_hostLine)

        self.retranslateUi(settingsPage)
        self.settingsStack.setCurrentIndex(0)
        self.databaseStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settingsPage)
        settingsPage.setTabOrder(self.databaseBox, self.mysql_hostLine)
        settingsPage.setTabOrder(self.mysql_hostLine, self.mysql_portBox)
        settingsPage.setTabOrder(self.mysql_portBox, self.mysql_userLine)
        settingsPage.setTabOrder(self.mysql_userLine, self.mysql_passLine)
        settingsPage.setTabOrder(self.mysql_passLine, self.mysql_databaseLine)
        settingsPage.setTabOrder(self.mysql_databaseLine, self.sqlite_fileLine)

    def retranslateUi(self, settingsPage):
        self.label.setText(QtGui.QApplication.translate("settingsPage", "Step 3: Select application settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsPage", "Please select the settings for your requested application:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("settingsPage", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settingsPage", "Select the database you want to import from:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("settingsPage", "Configure SQLite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("settingsPage", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("settingsPage", "Configure MySQL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("settingsPage", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("settingsPage", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("settingsPage", "Database:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("settingsPage", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.mysql_hostLine.setText(QtGui.QApplication.translate("settingsPage", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("settingsPage", "Host:", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
