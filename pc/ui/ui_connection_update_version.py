# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/src/connection_update_version.ui'
#
# Created: Wed Nov 17 12:05:54 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConnectionUpdateVersionDialog(object):
    def setupUi(self, ConnectionUpdateVersionDialog):
        ConnectionUpdateVersionDialog.setObjectName("ConnectionUpdateVersionDialog")
        ConnectionUpdateVersionDialog.resize(698, 453)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/phone"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConnectionUpdateVersionDialog.setWindowIcon(icon)
        self.verticalLayout_6 = QtGui.QVBoxLayout(ConnectionUpdateVersionDialog)
        self.verticalLayout_6.setMargin(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtGui.QLabel(ConnectionUpdateVersionDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtGui.QLabel(ConnectionUpdateVersionDialog)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.py20Box = QtGui.QCheckBox(ConnectionUpdateVersionDialog)
        self.py20Box.setObjectName("py20Box")
        self.horizontalLayout.addWidget(self.py20Box)
        self.helpLabel = HelpLabel(ConnectionUpdateVersionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpLabel.sizePolicy().hasHeightForWidth())
        self.helpLabel.setSizePolicy(sizePolicy)
        self.helpLabel.setText("<a href=\"#\">[Help]</a>")
        self.helpLabel.setObjectName("helpLabel")
        self.horizontalLayout.addWidget(self.helpLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.obexStack = QtGui.QStackedWidget(ConnectionUpdateVersionDialog)
        self.obexStack.setObjectName("obexStack")
        self.obexFoundWidget = QtGui.QWidget()
        self.obexFoundWidget.setObjectName("obexFoundWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.obexFoundWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtGui.QLabel(self.obexFoundWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(20, -1, -1, -1)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.sendPythonButton = QtGui.QCommandLinkButton(self.obexFoundWidget)
        self.sendPythonButton.setObjectName("sendPythonButton")
        self.gridLayout.addWidget(self.sendPythonButton, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.obexFoundWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_8 = QtGui.QLabel(self.obexFoundWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sendApplicationButton = QtGui.QCommandLinkButton(self.obexFoundWidget)
        self.sendApplicationButton.setMinimumSize(QtCore.QSize(0, 30))
        self.sendApplicationButton.setObjectName("sendApplicationButton")
        self.gridLayout_2.addWidget(self.sendApplicationButton, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.obexFoundWidget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.obexStack.addWidget(self.obexFoundWidget)
        self.obexNotFoundWidget = QtGui.QWidget()
        self.obexNotFoundWidget.setObjectName("obexNotFoundWidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.obexNotFoundWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtGui.QLabel(self.obexNotFoundWidget)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.operatingSystemStack = QtGui.QStackedWidget(self.obexNotFoundWidget)
        self.operatingSystemStack.setObjectName("operatingSystemStack")
        self.linuxWidget = QtGui.QWidget()
        self.linuxWidget.setObjectName("linuxWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.linuxWidget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(self.linuxWidget)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.operatingSystemStack.addWidget(self.linuxWidget)
        self.windowsWidget = QtGui.QWidget()
        self.windowsWidget.setObjectName("windowsWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.windowsWidget)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtGui.QLabel(self.windowsWidget)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.operatingSystemStack.addWidget(self.windowsWidget)
        self.verticalLayout_5.addWidget(self.operatingSystemStack)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.openFolderButton = QtGui.QCommandLinkButton(self.obexNotFoundWidget)
        self.openFolderButton.setObjectName("openFolderButton")
        self.horizontalLayout_2.addWidget(self.openFolderButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(565, 120, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.obexStack.addWidget(self.obexNotFoundWidget)
        self.verticalLayout_6.addWidget(self.obexStack)
        spacerItem4 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.buttonBox = QtGui.QDialogButtonBox(ConnectionUpdateVersionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_6.addWidget(self.buttonBox)

        self.retranslateUi(ConnectionUpdateVersionDialog)
        self.obexStack.setCurrentIndex(0)
        self.operatingSystemStack.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConnectionUpdateVersionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConnectionUpdateVersionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionUpdateVersionDialog)

    def retranslateUi(self, ConnectionUpdateVersionDialog):
        ConnectionUpdateVersionDialog.setWindowTitle(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Install/Update S60 Remote service", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Install or update the <i>S60 Remote service</i> on your mobile phone.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "<i>Series 60-Remote</i> requires <i>Python for S60</i> (PyS60), so please install this package first, if you haven\'t already.", None, QtGui.QApplication.UnicodeUTF8))
        self.py20Box.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "I want to use PyS60 2.0.0.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Step 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.sendPythonButton.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Send PyS60 package to mobile phone... ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Please continue the installation on your mobile phone!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Step 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.sendApplicationButton.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Send Series60-Remote package to mobile phone... ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Please continue the installation on your mobile phone!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Unfortunately, the following error appeared:<br />\n"
"- The python binding for <i>obexftp</i> isn\'t installed.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Either you install the required package (for instance on Fedora: <i>yum install python-obexftp</i>)<br />\n"
"or you transfer the files <i>PythonForS60_1_4_5_3rdEd.sis</i> and <i>series60-remote.sis</i> in the directory <i>mobile</i> manually to your device (you could use the application <i>kbluetooth</i>)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "You have to transfer the files <i>PythonForS60_1_4_5_3rdEd.sis</i> and <i>series60-remote.sis</i> in the directory <i>mobile</i> manually to your device.\n"
"Please use <i>Nokia PC Suite</i>.", None, QtGui.QApplication.UnicodeUTF8))
        self.openFolderButton.setText(QtGui.QApplication.translate("ConnectionUpdateVersionDialog", "Open Folder", None, QtGui.QApplication.UnicodeUTF8))

from widget.HelpLabel import HelpLabel
import resource_rc
