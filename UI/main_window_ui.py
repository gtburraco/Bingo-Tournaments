# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QAbstractItemView, QFrame, QHBoxLayout,
                               QLCDNumber, QLineEdit, QListView,
                               QListWidget, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QStatusBar, QTableView, QToolButton, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.ActionNewT = QAction(MainWindow)
        self.ActionNewT.setObjectName(u"ActionNewT")
        self.ActionLoadT = QAction(MainWindow)
        self.ActionLoadT.setObjectName(u"ActionLoadT")
        self.ActionGenerate = QAction(MainWindow)
        self.ActionGenerate.setObjectName(u"ActionGenerate")
        self.ActionGenerate.setEnabled(True)
        self.ActionDeleteExtracetd = QAction(MainWindow)
        self.ActionDeleteExtracetd.setObjectName(u"ActionDeleteExtracetd")
        self.ActionExportCSV = QAction(MainWindow)
        self.ActionExportCSV.setObjectName(u"ActionExportCSV")
        self.ActionExportHtml = QAction(MainWindow)
        self.ActionExportHtml.setObjectName(u"ActionExportHtml")
        self.ActionAbout = QAction(MainWindow)
        self.ActionAbout.setObjectName(u"ActionAbout")
        self.ActionExit = QAction(MainWindow)
        self.ActionExit.setObjectName(u"ActionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AutomaticDraw = QPushButton(self.centralwidget)
        self.AutomaticDraw.setObjectName(u"AutomaticDraw")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutomaticDraw.sizePolicy().hasHeightForWidth())
        self.AutomaticDraw.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.AutomaticDraw)

        self.ManualDraw = QPushButton(self.centralwidget)
        self.ManualDraw.setObjectName(u"ManualDraw")

        self.horizontalLayout.addWidget(self.ManualDraw)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.UndoDraw = QPushButton(self.centralwidget)
        self.UndoDraw.setObjectName(u"UndoDraw")

        self.horizontalLayout.addWidget(self.UndoDraw)

        self.SearchCards = QLineEdit(self.centralwidget)
        self.SearchCards.setObjectName(u"SearchCards")
        self.SearchCards.setMaximumSize(QSize(80, 16777215))
        self.SearchCards.setMaxLength(7)

        self.horizontalLayout.addWidget(self.SearchCards)

        self.SearchCardToolButton = QToolButton(self.centralwidget)
        self.SearchCardToolButton.setObjectName(u"SearchCardToolButton")

        self.horizontalLayout.addWidget(self.SearchCardToolButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ShowBoard = QPushButton(self.centralwidget)
        self.ShowBoard.setObjectName(u"ShowBoard")

        self.horizontalLayout.addWidget(self.ShowBoard)

        self.LcdNumber = QLCDNumber(self.centralwidget)
        self.LcdNumber.setObjectName(u"LcdNumber")
        self.LcdNumber.setDigitCount(3)
        self.LcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.LcdNumber)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.TableCardsView = QTableView(self.centralwidget)
        self.TableCardsView.setObjectName(u"TableCardsView")
        self.TableCardsView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TableCardsView.setAlternatingRowColors(True)
        self.TableCardsView.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.TableCardsView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.TableCardsView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ViewCardToolButton = QToolButton(self.centralwidget)
        self.ViewCardToolButton.setObjectName(u"ViewCardToolButton")
        self.ViewCardToolButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.ViewCardToolButton)

        self.InvalidateCardToolButton = QToolButton(self.centralwidget)
        self.InvalidateCardToolButton.setObjectName(u"InvalidateCardToolButton")
        self.InvalidateCardToolButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.InvalidateCardToolButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.ListNumberDraw = QListWidget(self.centralwidget)
        self.ListNumberDraw.setObjectName(u"ListNumberDraw")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ListNumberDraw.sizePolicy().hasHeightForWidth())
        self.ListNumberDraw.setSizePolicy(sizePolicy1)
        self.ListNumberDraw.setMinimumSize(QSize(0, 100))
        self.ListNumberDraw.setMaximumSize(QSize(16777215, 100))
        self.ListNumberDraw.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.ListNumberDraw.setResizeMode(QListView.ResizeMode.Adjust)
        self.ListNumberDraw.setSpacing(5)
        self.ListNumberDraw.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout.addWidget(self.ListNumberDraw)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuTournament = QMenu(self.menubar)
        self.menuTournament.setObjectName(u"menuTournament")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        self.menuInfo.setTitle(u"?")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTournament.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuTournament.addAction(self.ActionNewT)
        self.menuTournament.addAction(self.ActionLoadT)
        self.menuTournament.addSeparator()
        self.menuTournament.addAction(self.ActionGenerate)
        self.menuTournament.addAction(self.ActionDeleteExtracetd)
        self.menuTournament.addSeparator()
        self.menuTournament.addAction(self.ActionExportCSV)
        self.menuTournament.addAction(self.ActionExportHtml)
        self.menuTournament.addSeparator()
        self.menuTournament.addAction(self.ActionExit)
        self.menuInfo.addAction(self.ActionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bingo Tournaments", None))
        self.ActionNewT.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.ActionLoadT.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.ActionGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate Cards", None))
        self.ActionDeleteExtracetd.setText(
            QCoreApplication.translate("MainWindow", u"Delete all the drawn numbers", None))
        self.ActionExportCSV.setText(QCoreApplication.translate("MainWindow", u"Export Cards to CSV", None))
        self.ActionExportHtml.setText(QCoreApplication.translate("MainWindow", u"Export Carts to HTML and print", None))
        self.ActionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.ActionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.AutomaticDraw.setText(QCoreApplication.translate("MainWindow", u"Automatic\n"
                                                                            "Draw", None))
        self.ManualDraw.setText(QCoreApplication.translate("MainWindow", u"Manual\n"
                                                                         "Draw", None))
        self.UndoDraw.setText(QCoreApplication.translate("MainWindow", u"Undo Last\n"
                                                                       "Draw", None))
        self.SearchCards.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search card", None))
        self.SearchCardToolButton.setText("")
        self.ShowBoard.setText(QCoreApplication.translate("MainWindow", u"Board", None))
        # if QT_CONFIG(tooltip)
        self.LcdNumber.setToolTip(QCoreApplication.translate("MainWindow", u"The last number drawn", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.ViewCardToolButton.setToolTip(QCoreApplication.translate("MainWindow",
                                                                      u"Use double click or button to view card. Multi-select is available.",
                                                                      None))
        # endif // QT_CONFIG(tooltip)
        self.ViewCardToolButton.setText("")
        # if QT_CONFIG(tooltip)
        self.InvalidateCardToolButton.setToolTip(QCoreApplication.translate("MainWindow", u"Invalidate Cards", None))
        # endif // QT_CONFIG(tooltip)
        self.InvalidateCardToolButton.setText("")
        self.menuTournament.setTitle(QCoreApplication.translate("MainWindow", u"Tournament", None))
    # retranslateUi
