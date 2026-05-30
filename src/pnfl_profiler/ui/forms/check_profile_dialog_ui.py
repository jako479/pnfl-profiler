# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_profile_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_CheckProfileDialog(object):
    def setupUi(self, CheckProfileDialog):
        if not CheckProfileDialog.objectName():
            CheckProfileDialog.setObjectName(u"CheckProfileDialog")
        CheckProfileDialog.resize(520, 360)
        self.outerLayout = QVBoxLayout(CheckProfileDialog)
        self.outerLayout.setObjectName(u"outerLayout")
        self.headerLabel = QLabel(CheckProfileDialog)
        self.headerLabel.setObjectName(u"headerLabel")

        self.outerLayout.addWidget(self.headerLabel)

        self.bodyText = QTextEdit(CheckProfileDialog)
        self.bodyText.setObjectName(u"bodyText")
        self.bodyText.setReadOnly(True)

        self.outerLayout.addWidget(self.bodyText)

        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.prevButton = QPushButton(CheckProfileDialog)
        self.prevButton.setObjectName(u"prevButton")

        self.navLayout.addWidget(self.prevButton)

        self.nextButton = QPushButton(CheckProfileDialog)
        self.nextButton.setObjectName(u"nextButton")

        self.navLayout.addWidget(self.nextButton)

        self.navSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.navLayout.addItem(self.navSpacer)

        self.jumpButton = QPushButton(CheckProfileDialog)
        self.jumpButton.setObjectName(u"jumpButton")

        self.navLayout.addWidget(self.jumpButton)


        self.outerLayout.addLayout(self.navLayout)

        self.buttonBox = QDialogButtonBox(CheckProfileDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.outerLayout.addWidget(self.buttonBox)


        self.retranslateUi(CheckProfileDialog)
        self.buttonBox.rejected.connect(CheckProfileDialog.reject)

        QMetaObject.connectSlotsByName(CheckProfileDialog)
    # setupUi

    def retranslateUi(self, CheckProfileDialog):
        CheckProfileDialog.setWindowTitle(QCoreApplication.translate("CheckProfileDialog", u"Check Profile", None))
        self.headerLabel.setText("")
        self.prevButton.setText(QCoreApplication.translate("CheckProfileDialog", u"\u2190 Prev", None))
        self.nextButton.setText(QCoreApplication.translate("CheckProfileDialog", u"Next \u2192", None))
        self.jumpButton.setText(QCoreApplication.translate("CheckProfileDialog", u"Jump to situation", None))
    # retranslateUi

