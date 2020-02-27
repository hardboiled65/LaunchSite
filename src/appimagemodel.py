import subprocess
from PySide2.QtCore import QObject, Property, Signal, Slot


class AppImageModel(QObject):
    def __init__(self):
        QObject.__init__(self)

        self._name = ''
        self._file = ''

    def file(self):
        return self._file

    def set_file(self, file):
        self._file = file

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Change signals
    @Signal
    def name_changed(self):
        pass

    @Signal
    def file_changed(self):
        pass

    # QML Invokables
    @Slot()
    def launch(self):
        print('launch ' + self._file)
        subprocess.Popen([self._file])

    name = Property(str, name, set_name, notify=name_changed)
    file = Property(str, file, set_file, notify=file_changed)

