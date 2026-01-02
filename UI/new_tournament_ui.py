# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_tournament.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QFrame, QLabel, QLayout, QPushButton,
                               QRadioButton, QSizePolicy, QVBoxLayout)


class Ui_NewTournament(object):
    def setupUi(self, NewTournament):
        if not NewTournament.objectName():
            NewTournament.setObjectName(u"NewTournament")
        NewTournament.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewTournament.resize(261, 159)
        NewTournament.setMinimumSize(QSize(0, 0))
        NewTournament.setMaximumSize(QSize(261, 159))
        self.verticalLayout = QVBoxLayout(NewTournament)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.InfoLabel = QLabel(NewTournament)
        self.InfoLabel.setObjectName(u"InfoLabel")

        self.verticalLayout.addWidget(self.InfoLabel)

        self.FolderButton = QPushButton(NewTournament)
        self.FolderButton.setObjectName(u"FolderButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FolderButton.sizePolicy().hasHeightForWidth())
        self.FolderButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/svg/file_save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FolderButton.setIcon(icon)

        self.verticalLayout.addWidget(self.FolderButton)

        self.line = QFrame(NewTournament)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.FolderChoice = QLabel(NewTournament)
        self.FolderChoice.setObjectName(u"FolderChoice")
        self.FolderChoice.setTextFormat(Qt.TextFormat.PlainText)

        self.verticalLayout.addWidget(self.FolderChoice)

        self.line_2 = QFrame(NewTournament)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.RadioButton60_20 = QRadioButton(NewTournament)
        self.RadioButton60_20.setObjectName(u"RadioButton60_20")

        self.verticalLayout.addWidget(self.RadioButton60_20)

        self.RadioButton75_24 = QRadioButton(NewTournament)
        self.RadioButton75_24.setObjectName(u"RadioButton75_24")
        self.RadioButton75_24.setChecked(True)

        self.verticalLayout.addWidget(self.RadioButton75_24)

        self.RadioButton80_16 = QRadioButton(NewTournament)
        self.RadioButton80_16.setObjectName(u"RadioButton80_16")

        self.verticalLayout.addWidget(self.RadioButton80_16)

        self.RadioButton75_25 = QRadioButton(NewTournament)
        self.RadioButton75_25.setObjectName(u"RadioButton75_25")

        self.verticalLayout.addWidget(self.RadioButton75_25)

        self.RadioButton90_15 = QRadioButton(NewTournament)
        self.RadioButton90_15.setObjectName(u"RadioButton90_15")

        self.verticalLayout.addWidget(self.RadioButton90_15)

        self.RadioButton100_25 = QRadioButton(NewTournament)
        self.RadioButton100_25.setObjectName(u"RadioButton100_25")

        self.verticalLayout.addWidget(self.RadioButton100_25)

        self.buttonBox = QDialogButtonBox(NewTournament)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewTournament)

        QMetaObject.connectSlotsByName(NewTournament)

    # setupUi

    def retranslateUi(self, NewTournament):
        NewTournament.setWindowTitle(QCoreApplication.translate("NewTournament", u"New Tournament", None))
        self.InfoLabel.setText(
            QCoreApplication.translate("NewTournament", u"Enter the file name of the new bingo tournament.\n"
                                                        "Saving tournament is automatic.", None))
        self.FolderButton.setText(QCoreApplication.translate("NewTournament", u"Browse", None))
        self.FolderChoice.setText("")
        self.RadioButton60_20.setText(
            QCoreApplication.translate("NewTournament", u"60 Numbers (20 numbers per card)", None))
        self.RadioButton75_24.setText(
            QCoreApplication.translate("NewTournament", u"75 Numbers (24 numbers per card)", None))
        self.RadioButton80_16.setText(
            QCoreApplication.translate("NewTournament", u"80 Numbers (16 numbers per card)", None))
        self.RadioButton75_25.setText(
            QCoreApplication.translate("NewTournament", u"75 Numbers (25 numbers per card)", None))
        self.RadioButton90_15.setText(
            QCoreApplication.translate("NewTournament", u"90 Numbers (15 numbers per card)", None))
        self.RadioButton100_25.setText(
            QCoreApplication.translate("NewTournament", u"100 Numbers (25 numbers per card)", None))
    # retranslateUi
