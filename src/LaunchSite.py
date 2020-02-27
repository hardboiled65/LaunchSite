import os
from PySide2.QtCore import QObject, Property, Signal, Slot
from .appimagemodel import AppImageModel


class LaunchSite(QObject):
    def __init__(self):
        QObject.__init__(self)

        # Private members
        self._app_images = []
        self._app_image_objects = []

        # Connect
        self.app_image_added.connect(
            self.on_app_image_added
        )


    def app_images(self):
        return self._app_images


    # Private methods
    def _add_app_image(self, app_image):
        self._app_image_objects.append(app_image)
        ai = AppImageModel()

        ai.set_name(app_image.name)
        ai.set_file(app_image.file)

        self._app_images.append(ai)
        self.app_image_added.emit()
        self.app_images_changed.emit()

    def _has_cache(self, app_image):
        cache_dir = os.path.join(
            os.getenv('HOME'),
            '.local/share/launch-site/appimages'
        )
        if os.path.isdir(cache_dir):
            li = os.listdir(cache_dir)
            if app_image.name in li:
                return True
            return False
        return False


    # Notify signals
    @Signal
    def app_images_changed(self):
        pass

    # Logic signals
    @Signal
    def app_image_added(self):
        pass

    # Private slots
    @Slot()
    def on_app_image_added(self):
        print('app image added!')

    appImages = Property('QVariantList', app_images, notify=app_images_changed)

