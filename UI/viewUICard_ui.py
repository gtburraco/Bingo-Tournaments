# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewUICard.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QSizePolicy,
                               QTableWidget, QVBoxLayout)


class Ui_ViewUICard(object):
    def setupUi(self, ViewUICard):
        if not ViewUICard.objectName():
            ViewUICard.setObjectName(u"ViewUICard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewUICard.sizePolicy().hasHeightForWidth())
        ViewUICard.setSizePolicy(sizePolicy)
        ViewUICard.setMinimumSize(QSize(200, 200))
        self.verticalLayout = QVBoxLayout(ViewUICard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CardWidget = QTableWidget(ViewUICard)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.CardWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CardWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CardWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.CardWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.CardWidget.horizontalHeader().setVisible(False)
        self.CardWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.CardWidget)

        self.retranslateUi(ViewUICard)

        QMetaObject.connectSlotsByName(ViewUICard)

    # setupUi

    def retranslateUi(self, ViewUICard):
        pass
    # retranslateUi
