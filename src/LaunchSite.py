from PySide2.QtCore import QObject, Property, Signal


class LaunchSite(QObject):
    def __init__(self):
        QObject.__init__(self)

        # Private members
        self._app_images = []


    def app_images(self):
        return self._app_images


    @Signal
    def app_images_changed(self):
        pass


    appImages = Property(list, app_images, notify=app_images_changed)
