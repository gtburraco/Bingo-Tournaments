# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_choice.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QDialogButtonBox, QLineEdit, QVBoxLayout)


class Ui_GenerateChoice(object):
    def setupUi(self, GenerateChoice):
        if not GenerateChoice.objectName():
            GenerateChoice.setObjectName(u"GenerateChoice")
        GenerateChoice.setWindowModality(Qt.WindowModality.ApplicationModal)
        GenerateChoice.resize(174, 117)
        GenerateChoice.setMaximumSize(QSize(174, 117))
        self.verticalLayout = QVBoxLayout(GenerateChoice)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(GenerateChoice)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit)

        self.SamepositioncheckBox = QCheckBox(GenerateChoice)
        self.SamepositioncheckBox.setObjectName(u"SamepositioncheckBox")

        self.verticalLayout.addWidget(self.SamepositioncheckBox)

        self.DifferentpositioncheckBox = QCheckBox(GenerateChoice)
        self.DifferentpositioncheckBox.setObjectName(u"DifferentpositioncheckBox")

        self.verticalLayout.addWidget(self.DifferentpositioncheckBox)

        self.buttonBox = QDialogButtonBox(GenerateChoice)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GenerateChoice)

        QMetaObject.connectSlotsByName(GenerateChoice)

    # setupUi

    def retranslateUi(self, GenerateChoice):
        GenerateChoice.setWindowTitle(QCoreApplication.translate("GenerateChoice", u"Input", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("GenerateChoice", u"9999", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("GenerateChoice", u"Cards to generate", None))
        self.SamepositioncheckBox.setText(
            QCoreApplication.translate("GenerateChoice", u"Prevent identical cards (same numbers, same positions)",
                                       None))
        self.DifferentpositioncheckBox.setText(QCoreApplication.translate("GenerateChoice",
                                                                          u"Prevent cards with the same set of numbers, regardless of position",
                                                                          None))
    # retranslateUi
