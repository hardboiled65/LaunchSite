import subprocess
from PySide2.QtCore import QObject, Property, Signal, Slot


class AppImageModel(QObject):
    def __init__(self):
        QObject.__init__(self)

        self._name = ''
        self._file = ''
        self._image = ''

    def file(self):
        return self._file

    def set_file(self, file):
        if file != self._file:
            self._file = file
            self.file_changed.emit()

    def name(self):
        return self._name

    def set_name(self, name):
        if name != self._name:
            self._name = name
            self.name_changed.emit()

    def image(self):
        return self._image

    def set_image(self, image):
        if image != self._image:
            self._image = image
            self.image_changed.emit()

    # Change signals
    @Signal
    def name_changed(self):
        pass

    @Signal
    def file_changed(self):
        pass

    @Signal
    def image_changed(self):
        pass

    # QML Invokables
    @Slot()
    def launch(self):
        print('launch ' + self._file)
        subprocess.Popen([self._file])

    name = Property(str, name, set_name, notify=name_changed)
    file = Property(str, file, set_file, notify=file_changed)
    image = Property(str, image, set_image, notify=image_changed)

