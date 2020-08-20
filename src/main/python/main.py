#!/usr/bin/env python
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QIcon
import subprocess
from PyQt5.QtCore import QTimer
from ui import UI


class App(UI):

    def __init__(self):
        super().__init__(appctxt.get_resource("trayicon.png"))

        # add functionality to the appmenu

        self.quit_app.triggered.connect(qApp.quit)
        self.start_timer_menu.triggered.connect(self.startTimer)
        self.stop_timer_menu.triggered.connect(self.stopTimer)
        self.quit_btn.clicked.connect(qApp.quit)
        self.about.triggered.connect(self.aboutDialog)

        self.start_btn.clicked.connect(self.startTimer)

    def startTimer(self):
        if self.minutes.value() == 1:
            subprocess.call(['notify-send', 'BreakTimer started', 'You will receive a notification every minute.'])

        else:
            subprocess.call([
                'notify-send', 'BreakTimer started', f'You will receive a notification every {self.minutes.value()} minutes.'])

        self.timer = QTimer()

        self.stop_btn.clicked.connect(self.stopTimer)

        self.stop_btn.setEnabled(True)
        self.stop_timer_menu.setEnabled(True)
        self.start_btn.setDisabled(True)
        self.start_timer_menu.setDisabled(True)

        self.timer.timeout.connect(self.sendNotification)
        self.timer.start(60000 * self.minutes.value())

    def stopTimer(self):
        subprocess.call([
            'notify-send', 'BreakTimer ended', f'You will not receive any further notifications.'])

        self.timer.stop()

        self.stop_btn.setDisabled(True)
        self.stop_timer_menu.setDisabled(True)
        self.start_btn.setEnabled(True)
        self.start_timer_menu.setEnabled(True)

    def sendNotification(self):
        if self.play_sounds.isChecked():
            QSound.play(appctxt.get_resource("notification.wav"))

        self.notification_pause = subprocess.call(['notify-send', 'Take a break', 'Move and see away from the screen!'])


if __name__ == "__main__":
    import sys
    appctxt = ApplicationContext()
    app = QApplication(sys.argv)
    window = App()
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
