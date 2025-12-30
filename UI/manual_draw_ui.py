# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manual_draw.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QLineEdit, QVBoxLayout)


class Ui_ManualDraw(object):
    def setupUi(self, ManualDraw):
        if not ManualDraw.objectName():
            ManualDraw.setObjectName(u"ManualDraw")
        ManualDraw.setWindowModality(Qt.WindowModality.ApplicationModal)
        ManualDraw.resize(174, 117)
        ManualDraw.setMaximumSize(QSize(174, 117))
        self.verticalLayout = QVBoxLayout(ManualDraw)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(ManualDraw)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit)

        self.buttonBox = QDialogButtonBox(ManualDraw)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ManualDraw)

        QMetaObject.connectSlotsByName(ManualDraw)

    # setupUi

    def retranslateUi(self, ManualDraw):
        ManualDraw.setWindowTitle(QCoreApplication.translate("ManualDraw", u"Input", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("ManualDraw", u"999", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ManualDraw", u"Number to draw", None))
    # retranslateUi
