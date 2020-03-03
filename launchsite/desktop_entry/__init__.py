class DesktopEntry:
    def __init__(self, desktop_file):
        self._file = desktop_file
        self._name = ''
        self._localized_name = {}

        self._parse_file()

    @property
    def file(self):
        return self._file

    @property
    def name(self):
        return self._name

    def _parse_file(self):
        f = open(self.file)
        data = f.read()
        f.close()

        entry_field = True
        action_field_name = ''  # Temporary save
        for line in data.split('\n'):
            if entry_field is True:
                if line.startswith('Name='):
                    self._name = line.replace('Name=', '').rstrip()
                elif line.startswith('Name['):
                    pass
                elif line.startswith('[Desktop Action'):
                    entry_field = False
            else:
                pass

