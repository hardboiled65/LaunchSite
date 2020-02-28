import os
import sys
from PySide2.QtCore import QObject, Property, Signal, Slot
from .appimagemodel import AppImageModel

sys.path.append('..')

from launch_site.desktop_entry import DesktopEntry


BASE_CACHE_DIR = cache_dir = os.path.join(
    os.getenv('HOME'),
    '.local/share/launch-site/appimages'
)


class LaunchSite(QObject):
    # Logic signals
    app_image_added = Signal(str)

    def __init__(self):
        QObject.__init__(self)

        # Private members
        self._app_images = []           # AppImageModel
        self._app_image_objects = []    # AppImage

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
        self.app_image_added.emit(ai.file)
        self.app_images_changed.emit()

    def _get_object_by_path(self, app_image_path):
        for ai in self._app_image_objects:
            if app_image_path == ai.file:
                return ai
        return None

    def _get_cache_dir_by_path(self, app_image_path):
        basename = os.path.basename(app_image_path)
        return os.path.join(BASE_CACHE_DIR, basename)

    def _has_cache(self, app_image_path):
        cache_dir = os.path.join(
            os.getenv('HOME'),
            '.local/share/launch-site/appimages'
        )
        basename = os.path.basename(app_image_path)
        cache_dir = os.path.join(cache_dir, basename)
        if os.path.isdir(cache_dir):
            return True
        return False

    def _make_cache(self, app_image_path):
        cache_dir = os.path.join(
            os.getenv('HOME'),
            '.local/share/launch-site/appimages'
        )
        basename = os.path.basename(app_image_path)
        # Get AppImage object by path.
        ai = self._get_object_by_path(app_image_path)

        # Save cache in ~/.local/share/launch-site/appimages/MyApp.AppImage/
        ai.save_metadata(os.path.join(cache_dir, ai.name))

    def _read_metadata(self, app_image_path):
        cache_dir = self._get_cache_dir_by_path(app_image_path)
        desktop = None
        for i in os.listdir(cache_dir):
            if i.endswith('.desktop'):
                desktop = i
        entry = DesktopEntry(os.path.join(cache_dir, desktop))


    # Notify signals
    @Signal
    def app_images_changed(self):
        pass

    # Private slots
    @Slot(str)
    def on_app_image_added(self, app_image_path):
        print('app image added!: ' + app_image_path)
        if self._has_cache(app_image_path):
            print('has cache')
        else:
            print('no cache. making...')
            self._make_cache(app_image_path)
        self._read_metadata(app_image_path)

    appImages = Property('QVariantList', app_images, notify=app_images_changed)

