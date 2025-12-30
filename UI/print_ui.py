# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'print.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_PrintDialog(object):
    def setupUi(self, PrintDialog):
        if not PrintDialog.objectName():
            PrintDialog.setObjectName(u"PrintDialog")
        PrintDialog.resize(193, 151)
        PrintDialog.setMaximumSize(QSize(193, 151))
        self.verticalLayout = QVBoxLayout(PrintDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(PrintDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Col_spinBox = QSpinBox(PrintDialog)
        self.Col_spinBox.setObjectName(u"Col_spinBox")
        self.Col_spinBox.setMinimum(1)
        self.Col_spinBox.setMaximum(10)
        self.Col_spinBox.setValue(2)

        self.horizontalLayout.addWidget(self.Col_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(PrintDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.Row_spinBox = QSpinBox(PrintDialog)
        self.Row_spinBox.setObjectName(u"Row_spinBox")
        self.Row_spinBox.setMinimum(1)
        self.Row_spinBox.setMaximum(20)
        self.Row_spinBox.setValue(3)

        self.horizontalLayout_2.addWidget(self.Row_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(PrintDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.Font_spinBox = QSpinBox(PrintDialog)
        self.Font_spinBox.setObjectName(u"Font_spinBox")
        self.Font_spinBox.setMinimum(2)
        self.Font_spinBox.setMaximum(14)
        self.Font_spinBox.setValue(8)

        self.horizontalLayout_3.addWidget(self.Font_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.RandomcheckBox = QCheckBox(PrintDialog)
        self.RandomcheckBox.setObjectName(u"RandomcheckBox")

        self.verticalLayout.addWidget(self.RandomcheckBox)

        self.buttonBox = QDialogButtonBox(PrintDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PrintDialog)

        QMetaObject.connectSlotsByName(PrintDialog)
    # setupUi

    def retranslateUi(self, PrintDialog):
        PrintDialog.setWindowTitle(QCoreApplication.translate("PrintDialog", u"Print", None))
        self.label_2.setText(QCoreApplication.translate("PrintDialog", u"Cards x row in a page", None))
        self.label_3.setText(QCoreApplication.translate("PrintDialog", u"Number of row in a page", None))
        self.label.setText(QCoreApplication.translate("PrintDialog", u"Font size (2-14)", None))
        self.RandomcheckBox.setText(QCoreApplication.translate("PrintDialog", u"Random", None))
    # retranslateUi

