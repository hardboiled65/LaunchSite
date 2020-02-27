from PySide2.QtCore import QObject, Property, Signal
from .appimagemodel import AppImageModel


class LaunchSite(QObject):
    def __init__(self):
        QObject.__init__(self)

        # Private members
        self._app_images = []
        self._app_image_objects = []


    def app_images(self):
        return self._app_images


    # Private methods
    def _add_app_image(self, app_image):
        self._app_image_objects.append(app_image)
        ai = AppImageModel()

        ai.set_name(app_image.name)
        ai.set_file(app_image.file)

        self._app_images.append(ai)
        self.app_images_changed.emit()


    @Signal
    def app_images_changed(self):
        pass


    appImages = Property('QVariantList', app_images, notify=app_images_changed)

