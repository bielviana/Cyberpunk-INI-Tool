from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import *
from interface.res import *



class Ui_CyberpunkINITool(object):
    def setupUi(self, CyberpunkINITool):
        if not CyberpunkINITool.objectName():
            CyberpunkINITool.setObjectName(u"CyberpunkINITool")
        CyberpunkINITool.resize(524, 432)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        CyberpunkINITool.setWindowIcon(icon)
        CyberpunkINITool.setStyleSheet(u"")
        self.centralwidget = QWidget(CyberpunkINITool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"    border-radius: 10px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QFrame, #input_log, #input_file {\n"
"    color: #404040;\n"
"}\n"
"\n"
"#btn_theme {\n"
"    image: url(:/icons/assets/icons_black/dark-mode.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_theme:hover {\n"
"    image: url(:/icons/assets/icons_purple/dark-mode.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#frame_file {\n"
"    background-color: #F7F7F7;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #EBEBEB;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"#input_file {\n"
"    border: 0;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#btn_file {\n"
"    image: url(:/icons/assets/icons_purple/file.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_file:hover {\n"
"    image: url(:/icons/assets/icons_black/file.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_minimize {\n"
"    image: url(:/icons/assets/icons_purple/minimize.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_minimize:hover {\n"
"    image: url(:/icons/assets/icons_bl"
                        "ack/minimize.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_maximize {\n"
"    image: url(:/icons/assets/icons_purple/maximize.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_maximize:hover {\n"
"    image: url(:/icons/assets/icons_black/maximize.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_close {\n"
"    image: url(:/icons/assets/icons_purple/close.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#btn_close:hover {\n"
"    image: url(:/icons/assets/icons_black/close.svg);\n"
"    border: 0;\n"
"}\n"
"\n"
"#frame_app_icon{\n"
"    border-image: url(:/icons/assets/icon.png) 0 0 0 0 stretch stretch;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#titlebar{\n"
"    background-color: #EBEBEB;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#input_log {\n"
"    background-color: #F7F7F7;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #EBEBEB;\n"
"    padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.centralwidget)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setFrameShape(QFrame.NoFrame)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_app_icon = QFrame(self.titlebar)
        self.frame_app_icon.setObjectName(u"frame_app_icon")
        self.frame_app_icon.setMinimumSize(QSize(20, 20))
        self.frame_app_icon.setMaximumSize(QSize(20, 20))
        self.frame_app_icon.setFrameShape(QFrame.NoFrame)
        self.frame_app_icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_app_icon)

        self.label_app_title = QLabel(self.titlebar)
        self.label_app_title.setObjectName(u"label_app_title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_app_title.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_app_title)

        self.titlebar_btn_frame = QFrame(self.titlebar)
        self.titlebar_btn_frame.setObjectName(u"titlebar_btn_frame")
        self.titlebar_btn_frame.setMaximumSize(QSize(16777215, 30))
        self.titlebar_btn_frame.setFrameShape(QFrame.NoFrame)
        self.titlebar_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titlebar_btn_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_theme = QPushButton(self.titlebar_btn_frame)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setMinimumSize(QSize(14, 14))
        self.btn_theme.setMaximumSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.btn_theme)

        self.btn_minimize = QPushButton(self.titlebar_btn_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(14, 14))
        self.btn_minimize.setMaximumSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.titlebar_btn_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(14, 14))
        self.btn_maximize.setMaximumSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.titlebar_btn_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(18, 18))
        self.btn_close.setMaximumSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.titlebar_btn_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.titlebar)

        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_line1 = QFrame(self.frame_main)
        self.frame_line1.setObjectName(u"frame_line1")
        self.frame_line1.setFrameShape(QFrame.NoFrame)
        self.frame_line1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_line1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 10)
        self.label_file = QLabel(self.frame_line1)
        self.label_file.setObjectName(u"label_file")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.label_file.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_file)

        self.frame_file = QFrame(self.frame_line1)
        self.frame_file.setObjectName(u"frame_file")
        self.frame_file.setMinimumSize(QSize(0, 30))
        self.frame_file.setMaximumSize(QSize(16777215, 25))
        self.frame_file.setFrameShape(QFrame.NoFrame)
        self.frame_file.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_file)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.input_file = QLineEdit(self.frame_file)
        self.input_file.setObjectName(u"input_file")
        self.input_file.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.input_file)

        self.btn_file = QPushButton(self.frame_file)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_2.addWidget(self.btn_file)


        self.verticalLayout_3.addWidget(self.frame_file)


        self.verticalLayout_2.addWidget(self.frame_line1)

        self.frame_line2 = QFrame(self.frame_main)
        self.frame_line2.setObjectName(u"frame_line2")
        self.frame_line2.setFrameShape(QFrame.NoFrame)
        self.frame_line2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_line2)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 10, 20, 0)
        self.frame_line3 = QFrame(self.frame_line2)
        self.frame_line3.setObjectName(u"frame_line3")
        self.frame_line3.setFrameShape(QFrame.NoFrame)
        self.frame_line3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_line3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_log = QLabel(self.frame_line3)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_log)

        self.btn_split = QPushButton(self.frame_line3)
        self.btn_split.setObjectName(u"btn_split")
        self.btn_split.setMaximumSize(QSize(100, 16777215))
        self.btn_split.setFont(font1)

        self.horizontalLayout_5.addWidget(self.btn_split)


        self.verticalLayout_4.addWidget(self.frame_line3)

        self.input_log = QPlainTextEdit(self.frame_line2)
        self.input_log.setObjectName(u"input_log")

        self.verticalLayout_4.addWidget(self.input_log)


        self.verticalLayout_2.addWidget(self.frame_line2)


        self.verticalLayout.addWidget(self.frame_main)

        self.statusbar = QFrame(self.centralwidget)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 20))
        self.statusbar.setMaximumSize(QSize(16777215, 20))
        self.statusbar.setFrameShape(QFrame.NoFrame)
        self.statusbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.statusbar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sizegrip = QFrame(self.statusbar)
        self.sizegrip.setObjectName(u"sizegrip")
        self.sizegrip.setMinimumSize(QSize(20, 20))
        self.sizegrip.setMaximumSize(QSize(20, 20))
        self.sizegrip.setFrameShape(QFrame.NoFrame)
        self.sizegrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizegrip, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.statusbar)

        CyberpunkINITool.setCentralWidget(self.centralwidget)

        self.retranslateUi(CyberpunkINITool)

        QMetaObject.connectSlotsByName(CyberpunkINITool)
    # setupUi

    def retranslateUi(self, CyberpunkINITool):
        CyberpunkINITool.setWindowTitle(QCoreApplication.translate("CyberpunkINITool", u"Cyberpunk INI Tool", None))
        self.label_app_title.setText(QCoreApplication.translate("CyberpunkINITool", u"Cyberpunk INI Tool", None))
        self.btn_theme.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.label_file.setText(QCoreApplication.translate("CyberpunkINITool", u"INI File:", None))
        self.btn_file.setText("")
        self.label_log.setText(QCoreApplication.translate("CyberpunkINITool", u"Log:", None))
        self.btn_split.setText(QCoreApplication.translate("CyberpunkINITool", u"Split File", None))
    # retranslateUi
