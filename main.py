import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from src.LaunchSite import LaunchSite

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    launch_site = LaunchSite()
    engine.rootContext().setContextProperty('LaunchSite', launch_site)

    engine.load('qml/main.qml')

    app.exec_()
