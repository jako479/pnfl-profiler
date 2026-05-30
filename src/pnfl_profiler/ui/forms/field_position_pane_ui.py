# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'field_position_pane.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_FieldPositionPane(object):
    def setupUi(self, FieldPositionPane):
        if not FieldPositionPane.objectName():
            FieldPositionPane.setObjectName(u"FieldPositionPane")
        FieldPositionPane.resize(320, 720)
        self.mainLayout = QVBoxLayout(FieldPositionPane)
        self.mainLayout.setObjectName(u"mainLayout")
        self.headerLabel = QLabel(FieldPositionPane)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setTextFormat(Qt.RichText)

        self.mainLayout.addWidget(self.headerLabel)

        self.addButton = QPushButton(FieldPositionPane)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)

        self.mainLayout.addWidget(self.addButton)

        self.panelContainerLayout = QVBoxLayout()
        self.panelContainerLayout.setObjectName(u"panelContainerLayout")

        self.mainLayout.addLayout(self.panelContainerLayout)

        self.paneBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.paneBottomSpacer)


        self.retranslateUi(FieldPositionPane)

        QMetaObject.connectSlotsByName(FieldPositionPane)
    # setupUi

    def retranslateUi(self, FieldPositionPane):
        self.headerLabel.setText(QCoreApplication.translate("FieldPositionPane", u"<Field Position>", None))
        self.addButton.setText(QCoreApplication.translate("FieldPositionPane", u"+ Add edit panel", None))
        pass
    # retranslateUi

