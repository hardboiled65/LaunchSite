import os
import sys
from launchsite.appimage import AppImage
from src.LaunchSite import LaunchSite
from src.appimagemodel import AppImageModel
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app_images = []
# /usr/local/appimages
try:
    ai_list = os.listdir('/usr/local/appimages')
    for i in ai_list:
        full_path = os.path.join('/usr/local/appimages', i)
        ai = AppImage(full_path)
        app_images.append(ai)
except FileNotFoundError:
    print('Directory not found: /usr/local/appimages')


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    launch_site = LaunchSite()
    engine.rootContext().setContextProperty('LaunchSite', launch_site)

    qmlRegisterType(AppImageModel, 'LaunchSite', 0, 1, 'AppImageModel')

    engine.load(os.path.join(BASE_DIR, 'qml/main.qml'))

    for ai in app_images:
        launch_site._add_app_image(ai)

    app.exec_()
