from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class UI(QWidget):

    def __init__(self, path_to_trayicon):
        super().__init__()
        self.tray_icon_file = path_to_trayicon
        self.mainUI()
        self.resize(480, 360)
        self.setWindowIcon(QIcon("icon/icon.png"))
        self.setWindowTitle("BreakTimer")


    def mainUI(self):

        # define icon

        self.icon_quit = QIcon.fromTheme("application-exit")
        self.icon_about = QIcon.fromTheme("help-about")
        self.icon_start = QIcon.fromTheme("media-playback-start")
        self.icon_stop = QIcon.fromTheme("media-playback-stop")

        # menubar entries

        # file
        self.start_timer_menu = QAction("Start", self)
        self.start_timer_menu.setIcon(self.icon_start)
        self.start_timer_menu.setShortcut("Ctrl+S")

        self.stop_timer_menu = QAction("Stop", self)
        self.stop_timer_menu.setIcon(self.icon_stop)
        self.stop_timer_menu.setShortcut("Ctrl+Alt+S")
        self.stop_timer_menu.setDisabled(True)

        self.quit_app = QAction("Quit", self)
        self.quit_app.setShortcut("Ctrl+Q")
        self.quit_app.setIcon(QIcon.fromTheme("application-exit"))

        # help
        self.about = QAction("About", self)
        self.about.setShortcut("F1")
        self.about.setIcon(self.icon_about)

        # menubar

        self.menubar = QMenuBar(self)

        self.file_menu = self.menubar.addMenu("File")
        self.file_menu.addAction(self.start_timer_menu)
        self.file_menu.addAction(self.stop_timer_menu)
        self.file_menu.addAction(self.quit_app)

        self.help_menu = self.menubar.addMenu("Help")
        self.help_menu.addAction(self.about)

        # widgets on the window

        self.start_btn = QPushButton("Start", self)
        self.start_btn.setIcon(self.icon_start)

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.setIcon(self.icon_stop)
        self.stop_btn.setDisabled(True)

        self.quit_btn = QPushButton("Quit", self)
        self.quit_btn.setIcon(self.icon_quit)


        self.interval = QLabel("Interval: ", self)

        self.minutes = QSpinBox(self)
        self.minutes.setMaximumWidth(125)
        self.minutes.setRange(1, 99)
        self.minutes.setValue(30)
        self.minutes.setSuffix(" minutes")

        self.minutes.valueChanged.connect(self.changeMinuteText)

        self.play_sounds = QCheckBox(self)
        self.play_sounds.setText("Play sounds")
        self.play_sounds.setChecked(True)

        # layout

        self.hbox_btn = QHBoxLayout()
        self.hbox_btn.addStretch(1)
        self.hbox_btn.addWidget(self.start_btn)
        self.hbox_btn.addWidget(self.stop_btn)
        self.hbox_btn.addWidget(self.quit_btn)

        self.hbox_minutes = QHBoxLayout()
        self.hbox_minutes.addWidget(self.interval)
        self.hbox_minutes.addWidget(self.minutes)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox_minutes)
        self.vbox.addWidget(self.play_sounds)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox_btn)

        self.setLayout(self.vbox)

        # system tray icon

        self.tray = QSystemTrayIcon(QIcon(self.tray_icon_file), self)
        self.tray.setToolTip("Break Timer")
        self.tray.setVisible(True)

        self.tray.activated.connect(self.toggleShowWindow)

        self.tray_menu = QMenu()

        self.tray_menu.addAction(self.start_timer_menu)
        self.tray_menu.addAction(self.stop_timer_menu)
        self.tray_menu.addAction(self.quit_app)

        self.tray.setContextMenu(self.tray_menu)


    def changeMinuteText(self):
        if self.minutes.value() == 1:
            self.minutes.setSuffix(" minute")

        else:
            self.minutes.setSuffix(" minutes")


    def toggleShowWindow(self):
        if self.isHidden():
            self.show()
        
        else:
            self.hide()


    def aboutDialog(self):
        self.about_dialog = QMessageBox()
        self.about_dialog.setIcon(QMessageBox.Information)
        self.about_dialog.setText(
            "Break Timer is a little application, that regularly notifies you to take a break.")
        self.about_dialog.setInformativeText(
            "For more details see https://github.com/Palexer/break-timer")

        self.about_dialog.setWindowTitle("About")
        self.about_dialog.setStandardButtons(QMessageBox.Ok)
        self.about_dialog.exec_()


    def closeEvent(self, event):
        event.ignore()
        self.hide()
