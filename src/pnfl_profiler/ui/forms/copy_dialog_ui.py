# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copy_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CopyDialog(object):
    def setupUi(self, CopyDialog):
        if not CopyDialog.objectName():
            CopyDialog.setObjectName(u"CopyDialog")
        CopyDialog.resize(720, 460)
        self.outerLayout = QVBoxLayout(CopyDialog)
        self.outerLayout.setObjectName(u"outerLayout")
        self.bucketsLayout = QGridLayout()
        self.bucketsLayout.setObjectName(u"bucketsLayout")
        self.minutesBox = QGroupBox(CopyDialog)
        self.minutesBox.setObjectName(u"minutesBox")
        self.minutesLayout = QVBoxLayout(self.minutesBox)
        self.minutesLayout.setObjectName(u"minutesLayout")
        self.checkMinutesOverFive = QCheckBox(self.minutesBox)
        self.checkMinutesOverFive.setObjectName(u"checkMinutesOverFive")

        self.minutesLayout.addWidget(self.checkMinutesOverFive)

        self.checkMinutesTwoToFive = QCheckBox(self.minutesBox)
        self.checkMinutesTwoToFive.setObjectName(u"checkMinutesTwoToFive")

        self.minutesLayout.addWidget(self.checkMinutesTwoToFive)

        self.checkMinutesOneToTwo = QCheckBox(self.minutesBox)
        self.checkMinutesOneToTwo.setObjectName(u"checkMinutesOneToTwo")

        self.minutesLayout.addWidget(self.checkMinutesOneToTwo)

        self.checkMinutesFifteenSecToOne = QCheckBox(self.minutesBox)
        self.checkMinutesFifteenSecToOne.setObjectName(u"checkMinutesFifteenSecToOne")

        self.minutesLayout.addWidget(self.checkMinutesFifteenSecToOne)

        self.checkMinutesZeroToFifteenSec = QCheckBox(self.minutesBox)
        self.checkMinutesZeroToFifteenSec.setObjectName(u"checkMinutesZeroToFifteenSec")

        self.minutesLayout.addWidget(self.checkMinutesZeroToFifteenSec)


        self.bucketsLayout.addWidget(self.minutesBox, 0, 0, 1, 1)

        self.downBox = QGroupBox(CopyDialog)
        self.downBox.setObjectName(u"downBox")
        self.downLayout = QVBoxLayout(self.downBox)
        self.downLayout.setObjectName(u"downLayout")
        self.checkDownFirst = QCheckBox(self.downBox)
        self.checkDownFirst.setObjectName(u"checkDownFirst")

        self.downLayout.addWidget(self.checkDownFirst)

        self.checkDownSecond = QCheckBox(self.downBox)
        self.checkDownSecond.setObjectName(u"checkDownSecond")

        self.downLayout.addWidget(self.checkDownSecond)

        self.checkDownThird = QCheckBox(self.downBox)
        self.checkDownThird.setObjectName(u"checkDownThird")

        self.downLayout.addWidget(self.checkDownThird)

        self.checkDownFourth = QCheckBox(self.downBox)
        self.checkDownFourth.setObjectName(u"checkDownFourth")

        self.downLayout.addWidget(self.checkDownFourth)


        self.bucketsLayout.addWidget(self.downBox, 0, 1, 1, 1)

        self.yardsBox = QGroupBox(CopyDialog)
        self.yardsBox.setObjectName(u"yardsBox")
        self.yardsLayout = QVBoxLayout(self.yardsBox)
        self.yardsLayout.setObjectName(u"yardsLayout")
        self.checkYardsZeroToOne = QCheckBox(self.yardsBox)
        self.checkYardsZeroToOne.setObjectName(u"checkYardsZeroToOne")

        self.yardsLayout.addWidget(self.checkYardsZeroToOne)

        self.checkYardsTwoToFive = QCheckBox(self.yardsBox)
        self.checkYardsTwoToFive.setObjectName(u"checkYardsTwoToFive")

        self.yardsLayout.addWidget(self.checkYardsTwoToFive)

        self.checkYardsSixToTen = QCheckBox(self.yardsBox)
        self.checkYardsSixToTen.setObjectName(u"checkYardsSixToTen")

        self.yardsLayout.addWidget(self.checkYardsSixToTen)

        self.checkYardsOverTen = QCheckBox(self.yardsBox)
        self.checkYardsOverTen.setObjectName(u"checkYardsOverTen")

        self.yardsLayout.addWidget(self.checkYardsOverTen)


        self.bucketsLayout.addWidget(self.yardsBox, 0, 2, 1, 1)

        self.fieldBox = QGroupBox(CopyDialog)
        self.fieldBox.setObjectName(u"fieldBox")
        self.fieldLayout = QVBoxLayout(self.fieldBox)
        self.fieldLayout.setObjectName(u"fieldLayout")
        self.checkFieldInsideDef5 = QCheckBox(self.fieldBox)
        self.checkFieldInsideDef5.setObjectName(u"checkFieldInsideDef5")

        self.fieldLayout.addWidget(self.checkFieldInsideDef5)

        self.checkFieldDef5ToDef35 = QCheckBox(self.fieldBox)
        self.checkFieldDef5ToDef35.setObjectName(u"checkFieldDef5ToDef35")

        self.fieldLayout.addWidget(self.checkFieldDef5ToDef35)

        self.checkFieldDef35ToOff35 = QCheckBox(self.fieldBox)
        self.checkFieldDef35ToOff35.setObjectName(u"checkFieldDef35ToOff35")

        self.fieldLayout.addWidget(self.checkFieldDef35ToOff35)

        self.checkFieldOff35ToOff5 = QCheckBox(self.fieldBox)
        self.checkFieldOff35ToOff5.setObjectName(u"checkFieldOff35ToOff5")

        self.fieldLayout.addWidget(self.checkFieldOff35ToOff5)

        self.checkFieldInsideOff5 = QCheckBox(self.fieldBox)
        self.checkFieldInsideOff5.setObjectName(u"checkFieldInsideOff5")

        self.fieldLayout.addWidget(self.checkFieldInsideOff5)


        self.bucketsLayout.addWidget(self.fieldBox, 1, 0, 1, 2)

        self.spreadBox = QGroupBox(CopyDialog)
        self.spreadBox.setObjectName(u"spreadBox")
        self.spreadLayout = QVBoxLayout(self.spreadBox)
        self.spreadLayout.setObjectName(u"spreadLayout")
        self.checkSpreadAheadEightOrMore = QCheckBox(self.spreadBox)
        self.checkSpreadAheadEightOrMore.setObjectName(u"checkSpreadAheadEightOrMore")

        self.spreadLayout.addWidget(self.checkSpreadAheadEightOrMore)

        self.checkSpreadAheadFourToSeven = QCheckBox(self.spreadBox)
        self.checkSpreadAheadFourToSeven.setObjectName(u"checkSpreadAheadFourToSeven")

        self.spreadLayout.addWidget(self.checkSpreadAheadFourToSeven)

        self.checkSpreadAheadOneToThree = QCheckBox(self.spreadBox)
        self.checkSpreadAheadOneToThree.setObjectName(u"checkSpreadAheadOneToThree")

        self.spreadLayout.addWidget(self.checkSpreadAheadOneToThree)

        self.checkSpreadTied = QCheckBox(self.spreadBox)
        self.checkSpreadTied.setObjectName(u"checkSpreadTied")

        self.spreadLayout.addWidget(self.checkSpreadTied)

        self.checkSpreadBehindOneToThree = QCheckBox(self.spreadBox)
        self.checkSpreadBehindOneToThree.setObjectName(u"checkSpreadBehindOneToThree")

        self.spreadLayout.addWidget(self.checkSpreadBehindOneToThree)

        self.checkSpreadBehindFourToSeven = QCheckBox(self.spreadBox)
        self.checkSpreadBehindFourToSeven.setObjectName(u"checkSpreadBehindFourToSeven")

        self.spreadLayout.addWidget(self.checkSpreadBehindFourToSeven)

        self.checkSpreadBehindEightOrMore = QCheckBox(self.spreadBox)
        self.checkSpreadBehindEightOrMore.setObjectName(u"checkSpreadBehindEightOrMore")

        self.spreadLayout.addWidget(self.checkSpreadBehindEightOrMore)


        self.bucketsLayout.addWidget(self.spreadBox, 1, 2, 1, 1)


        self.outerLayout.addLayout(self.bucketsLayout)

        self.whatToCopyBox = QGroupBox(CopyDialog)
        self.whatToCopyBox.setObjectName(u"whatToCopyBox")
        self.whatToCopyLayout = QHBoxLayout(self.whatToCopyBox)
        self.whatToCopyLayout.setObjectName(u"whatToCopyLayout")
        self.checkPlays = QCheckBox(self.whatToCopyBox)
        self.checkPlays.setObjectName(u"checkPlays")
        self.checkPlays.setChecked(True)

        self.whatToCopyLayout.addWidget(self.checkPlays)

        self.checkClock = QCheckBox(self.whatToCopyBox)
        self.checkClock.setObjectName(u"checkClock")
        self.checkClock.setChecked(True)

        self.whatToCopyLayout.addWidget(self.checkClock)

        self.whatToCopySpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.whatToCopyLayout.addItem(self.whatToCopySpacer)


        self.outerLayout.addWidget(self.whatToCopyBox)

        self.countLabel = QLabel(CopyDialog)
        self.countLabel.setObjectName(u"countLabel")

        self.outerLayout.addWidget(self.countLabel)

        self.buttonBox = QDialogButtonBox(CopyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.outerLayout.addWidget(self.buttonBox)


        self.retranslateUi(CopyDialog)
        self.buttonBox.accepted.connect(CopyDialog.accept)
        self.buttonBox.rejected.connect(CopyDialog.reject)

        QMetaObject.connectSlotsByName(CopyDialog)
    # setupUi

    def retranslateUi(self, CopyDialog):
        CopyDialog.setWindowTitle(QCoreApplication.translate("CopyDialog", u"Copy Situation To:", None))
        self.minutesBox.setTitle(QCoreApplication.translate("CopyDialog", u"Minutes in half:", None))
        self.checkMinutesOverFive.setText(QCoreApplication.translate("CopyDialog", u">5", None))
        self.checkMinutesTwoToFive.setText(QCoreApplication.translate("CopyDialog", u">2-5", None))
        self.checkMinutesOneToTwo.setText(QCoreApplication.translate("CopyDialog", u">1-2", None))
        self.checkMinutesFifteenSecToOne.setText(QCoreApplication.translate("CopyDialog", u">:15-1", None))
        self.checkMinutesZeroToFifteenSec.setText(QCoreApplication.translate("CopyDialog", u"0-:15", None))
        self.downBox.setTitle(QCoreApplication.translate("CopyDialog", u"Down:", None))
        self.checkDownFirst.setText(QCoreApplication.translate("CopyDialog", u"1", None))
        self.checkDownSecond.setText(QCoreApplication.translate("CopyDialog", u"2", None))
        self.checkDownThird.setText(QCoreApplication.translate("CopyDialog", u"3", None))
        self.checkDownFourth.setText(QCoreApplication.translate("CopyDialog", u"4", None))
        self.yardsBox.setTitle(QCoreApplication.translate("CopyDialog", u"Yards to go:", None))
        self.checkYardsZeroToOne.setText(QCoreApplication.translate("CopyDialog", u"0-1", None))
        self.checkYardsTwoToFive.setText(QCoreApplication.translate("CopyDialog", u"2-5", None))
        self.checkYardsSixToTen.setText(QCoreApplication.translate("CopyDialog", u"6-10", None))
        self.checkYardsOverTen.setText(QCoreApplication.translate("CopyDialog", u">10", None))
        self.fieldBox.setTitle(QCoreApplication.translate("CopyDialog", u"Field Position:", None))
        self.checkFieldInsideDef5.setText(QCoreApplication.translate("CopyDialog", u"<DEF 5", None))
        self.checkFieldDef5ToDef35.setText(QCoreApplication.translate("CopyDialog", u"DEF 5 - DEF 35", None))
        self.checkFieldDef35ToOff35.setText(QCoreApplication.translate("CopyDialog", u"DEF 35 - OFF 35", None))
        self.checkFieldOff35ToOff5.setText(QCoreApplication.translate("CopyDialog", u"OFF 35 - OFF 5", None))
        self.checkFieldInsideOff5.setText(QCoreApplication.translate("CopyDialog", u"<OFF 5", None))
        self.spreadBox.setTitle(QCoreApplication.translate("CopyDialog", u"Point Spread:", None))
        self.checkSpreadAheadEightOrMore.setText(QCoreApplication.translate("CopyDialog", u"Ahead by 8+", None))
        self.checkSpreadAheadFourToSeven.setText(QCoreApplication.translate("CopyDialog", u"Ahead by 4-7", None))
        self.checkSpreadAheadOneToThree.setText(QCoreApplication.translate("CopyDialog", u"Ahead by 1-3", None))
        self.checkSpreadTied.setText(QCoreApplication.translate("CopyDialog", u"Tied", None))
        self.checkSpreadBehindOneToThree.setText(QCoreApplication.translate("CopyDialog", u"Behind by 1-3", None))
        self.checkSpreadBehindFourToSeven.setText(QCoreApplication.translate("CopyDialog", u"Behind by 4-7", None))
        self.checkSpreadBehindEightOrMore.setText(QCoreApplication.translate("CopyDialog", u"Behind by 8+", None))
        self.whatToCopyBox.setTitle(QCoreApplication.translate("CopyDialog", u"What to Copy?", None))
        self.checkPlays.setText(QCoreApplication.translate("CopyDialog", u"Plays", None))
        self.checkClock.setText(QCoreApplication.translate("CopyDialog", u"Clock", None))
        self.countLabel.setText(QCoreApplication.translate("CopyDialog", u"Situations: 0", None))
    # retranslateUi

