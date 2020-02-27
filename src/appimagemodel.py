from PySide2.QtCore import QObject, Property, Signal, Slot


class AppImageModel(QObject):
    def __init__(self):
        QObject.__init__(self)

        self._name = ''

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Change signals
    @Signal
    def name_changed(self):
        pass

    # QML Invokables
    @Slot()
    def launch(self):
        print('launch ' + self._name)

    name = Property(str, name, set_name, notify=name_changed)

