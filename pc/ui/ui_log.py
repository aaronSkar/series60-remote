# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/src/log.ui'
#
# Created: Wed Nov 17 12:05:58 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(673, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/text-plain"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Log.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Log)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setMargin(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtGui.QTabWidget(Log)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setMargin(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logEdit = QtGui.QPlainTextEdit(self.tab)
        self.logEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.logEdit.setReadOnly(True)
        self.logEdit.setObjectName("logEdit")
        self.verticalLayout_2.addWidget(self.logEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formatBox = QtGui.QCheckBox(self.tab)
        self.formatBox.setChecked(True)
        self.formatBox.setObjectName("formatBox")
        self.horizontalLayout.addWidget(self.formatBox)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.levelBox = QtGui.QComboBox(self.tab)
        self.levelBox.setMinimumSize(QtCore.QSize(170, 0))
        self.levelBox.setEditable(False)
        self.levelBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.levelBox.setObjectName("levelBox")
        self.levelBox.addItem("")
        self.levelBox.addItem("")
        self.levelBox.addItem("")
        self.levelBox.addItem("")
        self.levelBox.addItem("")
        self.levelBox.addItem("")
        self.horizontalLayout.addWidget(self.levelBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setMargin(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputEdit = QtGui.QTextEdit(self.tab_2)
        self.outputEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.outputEdit.setReadOnly(True)
        self.outputEdit.setObjectName("outputEdit")
        self.verticalLayout.addWidget(self.outputEdit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonBox = QtGui.QDialogButtonBox(Log)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Log)
        self.tabWidget.setCurrentIndex(0)
        self.levelBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Log.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Log.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.logEdit.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.outputEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        Log.setWindowTitle(QtGui.QApplication.translate("Log", "Log messages", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Log", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.formatBox.setText(QtGui.QApplication.translate("Log", "Long format", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Log", "Log level:", None, QtGui.QApplication.UnicodeUTF8))
        self.levelBox.setItemText(0, QtGui.QApplication.translate("Log", "Debug (with SQL)", None, QtGui.QApplication.UnicodeUTF8))
        self.levelBox.setItemText(1, QtGui.QApplication.translate("Log", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.levelBox.setItemText(2, QtGui.QApplication.translate("Log", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.levelBox.setItemText(3, QtGui.QApplication.translate("Log", "Warning", None, QtGui.QApplication.UnicodeUTF8))
        self.levelBox.setItemText(4, QtGui.QApplication.translate("Log", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.levelBox.setItemText(5, QtGui.QApplication.translate("Log", "Critical", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Log", "Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Log", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Log", "Output", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
