# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'situation_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_SituationPanel(object):
    def setupUi(self, SituationPanel):
        if not SituationPanel.objectName():
            SituationPanel.setObjectName(u"SituationPanel")
        SituationPanel.resize(820, 460)
        self.outerLayout = QVBoxLayout(SituationPanel)
        self.outerLayout.setObjectName(u"outerLayout")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.situationNumberCaption = QLabel(SituationPanel)
        self.situationNumberCaption.setObjectName(u"situationNumberCaption")

        self.headerLayout.addWidget(self.situationNumberCaption)

        self.situationNumberLabel = QLabel(SituationPanel)
        self.situationNumberLabel.setObjectName(u"situationNumberLabel")

        self.headerLayout.addWidget(self.situationNumberLabel)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.stopClockCheck = QCheckBox(SituationPanel)
        self.stopClockCheck.setObjectName(u"stopClockCheck")

        self.headerLayout.addWidget(self.stopClockCheck)

        self.closeButton = QPushButton(SituationPanel)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMaximumSize(QSize(28, 16777215))

        self.headerLayout.addWidget(self.closeButton)


        self.outerLayout.addLayout(self.headerLayout)

        self.bucketsLayout = QGridLayout()
        self.bucketsLayout.setObjectName(u"bucketsLayout")
        self.minutesBox = QGroupBox(SituationPanel)
        self.minutesBox.setObjectName(u"minutesBox")
        self.minutesLayout = QVBoxLayout(self.minutesBox)
        self.minutesLayout.setObjectName(u"minutesLayout")
        self.radioMinutesOverFive = QRadioButton(self.minutesBox)
        self.radioMinutesOverFive.setObjectName(u"radioMinutesOverFive")

        self.minutesLayout.addWidget(self.radioMinutesOverFive)

        self.radioMinutesTwoToFive = QRadioButton(self.minutesBox)
        self.radioMinutesTwoToFive.setObjectName(u"radioMinutesTwoToFive")

        self.minutesLayout.addWidget(self.radioMinutesTwoToFive)

        self.radioMinutesOneToTwo = QRadioButton(self.minutesBox)
        self.radioMinutesOneToTwo.setObjectName(u"radioMinutesOneToTwo")

        self.minutesLayout.addWidget(self.radioMinutesOneToTwo)

        self.radioMinutesFifteenSecToOne = QRadioButton(self.minutesBox)
        self.radioMinutesFifteenSecToOne.setObjectName(u"radioMinutesFifteenSecToOne")

        self.minutesLayout.addWidget(self.radioMinutesFifteenSecToOne)

        self.radioMinutesZeroToFifteenSec = QRadioButton(self.minutesBox)
        self.radioMinutesZeroToFifteenSec.setObjectName(u"radioMinutesZeroToFifteenSec")

        self.minutesLayout.addWidget(self.radioMinutesZeroToFifteenSec)


        self.bucketsLayout.addWidget(self.minutesBox, 0, 0, 1, 1)

        self.downBox = QGroupBox(SituationPanel)
        self.downBox.setObjectName(u"downBox")
        self.downLayout = QVBoxLayout(self.downBox)
        self.downLayout.setObjectName(u"downLayout")
        self.radioDownFirst = QRadioButton(self.downBox)
        self.radioDownFirst.setObjectName(u"radioDownFirst")

        self.downLayout.addWidget(self.radioDownFirst)

        self.radioDownSecond = QRadioButton(self.downBox)
        self.radioDownSecond.setObjectName(u"radioDownSecond")

        self.downLayout.addWidget(self.radioDownSecond)

        self.radioDownThird = QRadioButton(self.downBox)
        self.radioDownThird.setObjectName(u"radioDownThird")

        self.downLayout.addWidget(self.radioDownThird)

        self.radioDownFourth = QRadioButton(self.downBox)
        self.radioDownFourth.setObjectName(u"radioDownFourth")

        self.downLayout.addWidget(self.radioDownFourth)


        self.bucketsLayout.addWidget(self.downBox, 0, 1, 1, 1)

        self.yardsBox = QGroupBox(SituationPanel)
        self.yardsBox.setObjectName(u"yardsBox")
        self.yardsLayout = QVBoxLayout(self.yardsBox)
        self.yardsLayout.setObjectName(u"yardsLayout")
        self.radioYardsZeroToOne = QRadioButton(self.yardsBox)
        self.radioYardsZeroToOne.setObjectName(u"radioYardsZeroToOne")

        self.yardsLayout.addWidget(self.radioYardsZeroToOne)

        self.radioYardsTwoToFive = QRadioButton(self.yardsBox)
        self.radioYardsTwoToFive.setObjectName(u"radioYardsTwoToFive")

        self.yardsLayout.addWidget(self.radioYardsTwoToFive)

        self.radioYardsSixToTen = QRadioButton(self.yardsBox)
        self.radioYardsSixToTen.setObjectName(u"radioYardsSixToTen")

        self.yardsLayout.addWidget(self.radioYardsSixToTen)

        self.radioYardsOverTen = QRadioButton(self.yardsBox)
        self.radioYardsOverTen.setObjectName(u"radioYardsOverTen")

        self.yardsLayout.addWidget(self.radioYardsOverTen)


        self.bucketsLayout.addWidget(self.yardsBox, 0, 2, 1, 1)

        self.spreadBox = QGroupBox(SituationPanel)
        self.spreadBox.setObjectName(u"spreadBox")
        self.spreadLayout = QVBoxLayout(self.spreadBox)
        self.spreadLayout.setObjectName(u"spreadLayout")
        self.radioSpreadAheadEightOrMore = QRadioButton(self.spreadBox)
        self.radioSpreadAheadEightOrMore.setObjectName(u"radioSpreadAheadEightOrMore")

        self.spreadLayout.addWidget(self.radioSpreadAheadEightOrMore)

        self.radioSpreadAheadFourToSeven = QRadioButton(self.spreadBox)
        self.radioSpreadAheadFourToSeven.setObjectName(u"radioSpreadAheadFourToSeven")

        self.spreadLayout.addWidget(self.radioSpreadAheadFourToSeven)

        self.radioSpreadAheadOneToThree = QRadioButton(self.spreadBox)
        self.radioSpreadAheadOneToThree.setObjectName(u"radioSpreadAheadOneToThree")

        self.spreadLayout.addWidget(self.radioSpreadAheadOneToThree)

        self.radioSpreadTied = QRadioButton(self.spreadBox)
        self.radioSpreadTied.setObjectName(u"radioSpreadTied")

        self.spreadLayout.addWidget(self.radioSpreadTied)

        self.radioSpreadBehindOneToThree = QRadioButton(self.spreadBox)
        self.radioSpreadBehindOneToThree.setObjectName(u"radioSpreadBehindOneToThree")

        self.spreadLayout.addWidget(self.radioSpreadBehindOneToThree)

        self.radioSpreadBehindFourToSeven = QRadioButton(self.spreadBox)
        self.radioSpreadBehindFourToSeven.setObjectName(u"radioSpreadBehindFourToSeven")

        self.spreadLayout.addWidget(self.radioSpreadBehindFourToSeven)

        self.radioSpreadBehindEightOrMore = QRadioButton(self.spreadBox)
        self.radioSpreadBehindEightOrMore.setObjectName(u"radioSpreadBehindEightOrMore")

        self.spreadLayout.addWidget(self.radioSpreadBehindEightOrMore)


        self.bucketsLayout.addWidget(self.spreadBox, 0, 3, 1, 1)


        self.outerLayout.addLayout(self.bucketsLayout)

        self.fieldPositionLabel = QLabel(SituationPanel)
        self.fieldPositionLabel.setObjectName(u"fieldPositionLabel")

        self.outerLayout.addWidget(self.fieldPositionLabel)

        self.playsLayout = QGridLayout()
        self.playsLayout.setObjectName(u"playsLayout")
        self.playsHeaderPlay = QLabel(SituationPanel)
        self.playsHeaderPlay.setObjectName(u"playsHeaderPlay")

        self.playsLayout.addWidget(self.playsHeaderPlay, 0, 0, 1, 1)

        self.playsHeaderWeight = QLabel(SituationPanel)
        self.playsHeaderWeight.setObjectName(u"playsHeaderWeight")

        self.playsLayout.addWidget(self.playsHeaderWeight, 0, 1, 1, 1)

        self.playsHeaderPercent = QLabel(SituationPanel)
        self.playsHeaderPercent.setObjectName(u"playsHeaderPercent")

        self.playsLayout.addWidget(self.playsHeaderPercent, 0, 2, 1, 1)

        self.categoryCombo1 = QComboBox(SituationPanel)
        self.categoryCombo1.setObjectName(u"categoryCombo1")

        self.playsLayout.addWidget(self.categoryCombo1, 1, 0, 1, 1)

        self.weightSpin1 = QSpinBox(SituationPanel)
        self.weightSpin1.setObjectName(u"weightSpin1")
        self.weightSpin1.setMaximum(10)

        self.playsLayout.addWidget(self.weightSpin1, 1, 1, 1, 1)

        self.percentLabel1 = QLabel(SituationPanel)
        self.percentLabel1.setObjectName(u"percentLabel1")

        self.playsLayout.addWidget(self.percentLabel1, 1, 2, 1, 1)

        self.categoryCombo2 = QComboBox(SituationPanel)
        self.categoryCombo2.setObjectName(u"categoryCombo2")

        self.playsLayout.addWidget(self.categoryCombo2, 2, 0, 1, 1)

        self.weightSpin2 = QSpinBox(SituationPanel)
        self.weightSpin2.setObjectName(u"weightSpin2")
        self.weightSpin2.setMaximum(10)

        self.playsLayout.addWidget(self.weightSpin2, 2, 1, 1, 1)

        self.percentLabel2 = QLabel(SituationPanel)
        self.percentLabel2.setObjectName(u"percentLabel2")

        self.playsLayout.addWidget(self.percentLabel2, 2, 2, 1, 1)

        self.categoryCombo3 = QComboBox(SituationPanel)
        self.categoryCombo3.setObjectName(u"categoryCombo3")

        self.playsLayout.addWidget(self.categoryCombo3, 3, 0, 1, 1)

        self.weightSpin3 = QSpinBox(SituationPanel)
        self.weightSpin3.setObjectName(u"weightSpin3")
        self.weightSpin3.setMaximum(10)

        self.playsLayout.addWidget(self.weightSpin3, 3, 1, 1, 1)

        self.percentLabel3 = QLabel(SituationPanel)
        self.percentLabel3.setObjectName(u"percentLabel3")

        self.playsLayout.addWidget(self.percentLabel3, 3, 2, 1, 1)


        self.outerLayout.addLayout(self.playsLayout)

        self.buttonRow = QHBoxLayout()
        self.buttonRow.setObjectName(u"buttonRow")
        self.buttonRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonRow.addItem(self.buttonRowSpacer)

        self.copyButton = QPushButton(SituationPanel)
        self.copyButton.setObjectName(u"copyButton")

        self.buttonRow.addWidget(self.copyButton)


        self.outerLayout.addLayout(self.buttonRow)


        self.retranslateUi(SituationPanel)

        QMetaObject.connectSlotsByName(SituationPanel)
    # setupUi

    def retranslateUi(self, SituationPanel):
        SituationPanel.setTitle(QCoreApplication.translate("SituationPanel", u"Situation", None))
        self.situationNumberCaption.setText(QCoreApplication.translate("SituationPanel", u"Situation #", None))
        self.situationNumberLabel.setText(QCoreApplication.translate("SituationPanel", u"\u2014", None))
        self.stopClockCheck.setText(QCoreApplication.translate("SituationPanel", u"Stop Clock?", None))
        self.closeButton.setText(QCoreApplication.translate("SituationPanel", u"\u2715", None))
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("SituationPanel", u"Remove this panel", None))
#endif // QT_CONFIG(tooltip)
        self.minutesBox.setTitle(QCoreApplication.translate("SituationPanel", u"Minutes in half:", None))
        self.radioMinutesOverFive.setText(QCoreApplication.translate("SituationPanel", u">5", None))
        self.radioMinutesTwoToFive.setText(QCoreApplication.translate("SituationPanel", u">2-5", None))
        self.radioMinutesOneToTwo.setText(QCoreApplication.translate("SituationPanel", u">1-2", None))
        self.radioMinutesFifteenSecToOne.setText(QCoreApplication.translate("SituationPanel", u">:15-1", None))
        self.radioMinutesZeroToFifteenSec.setText(QCoreApplication.translate("SituationPanel", u"0-:15", None))
        self.downBox.setTitle(QCoreApplication.translate("SituationPanel", u"Down:", None))
        self.radioDownFirst.setText(QCoreApplication.translate("SituationPanel", u"1", None))
        self.radioDownSecond.setText(QCoreApplication.translate("SituationPanel", u"2", None))
        self.radioDownThird.setText(QCoreApplication.translate("SituationPanel", u"3", None))
        self.radioDownFourth.setText(QCoreApplication.translate("SituationPanel", u"4", None))
        self.yardsBox.setTitle(QCoreApplication.translate("SituationPanel", u"Yards to go:", None))
        self.radioYardsZeroToOne.setText(QCoreApplication.translate("SituationPanel", u"0-1", None))
        self.radioYardsTwoToFive.setText(QCoreApplication.translate("SituationPanel", u"2-5", None))
        self.radioYardsSixToTen.setText(QCoreApplication.translate("SituationPanel", u"6-10", None))
        self.radioYardsOverTen.setText(QCoreApplication.translate("SituationPanel", u">10", None))
        self.spreadBox.setTitle(QCoreApplication.translate("SituationPanel", u"Point Spread:", None))
        self.radioSpreadAheadEightOrMore.setText(QCoreApplication.translate("SituationPanel", u"Ahead by 8+", None))
        self.radioSpreadAheadFourToSeven.setText(QCoreApplication.translate("SituationPanel", u"Ahead by 4-7", None))
        self.radioSpreadAheadOneToThree.setText(QCoreApplication.translate("SituationPanel", u"Ahead by 1-3", None))
        self.radioSpreadTied.setText(QCoreApplication.translate("SituationPanel", u"Tied", None))
        self.radioSpreadBehindOneToThree.setText(QCoreApplication.translate("SituationPanel", u"Behind by 1-3", None))
        self.radioSpreadBehindFourToSeven.setText(QCoreApplication.translate("SituationPanel", u"Behind by 4-7", None))
        self.radioSpreadBehindEightOrMore.setText(QCoreApplication.translate("SituationPanel", u"Behind by 8+", None))
        self.fieldPositionLabel.setText(QCoreApplication.translate("SituationPanel", u"Field Position: \u2014", None))
        self.playsHeaderPlay.setText(QCoreApplication.translate("SituationPanel", u"Selected Play", None))
        self.playsHeaderWeight.setText(QCoreApplication.translate("SituationPanel", u"Weight", None))
        self.playsHeaderPercent.setText(QCoreApplication.translate("SituationPanel", u"%", None))
        self.percentLabel1.setText(QCoreApplication.translate("SituationPanel", u"0%", None))
        self.percentLabel2.setText(QCoreApplication.translate("SituationPanel", u"0%", None))
        self.percentLabel3.setText(QCoreApplication.translate("SituationPanel", u"0%", None))
        self.copyButton.setText(QCoreApplication.translate("SituationPanel", u"COPY", None))
    # retranslateUi

