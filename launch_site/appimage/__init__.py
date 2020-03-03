import os
import shutil
import subprocess


class AppImage:
    def __init__(self, appimage_file):
        self._file = appimage_file

        # Get md5 of AppImage file.
        md5sum = subprocess.run(
            ['md5sum', appimage_file],
            stdout=subprocess.PIPE
        )
        md5sum_result = md5sum.stdout.decode()
        md5sum_result = md5sum_result.split()[0]

        self._md5 = md5sum_result

        # Get offset of AppImage.
        appimage_offset = subprocess.run(
            [appimage_file, '--appimage-offset'],
            stdout=subprocess.PIPE
        )
        appimage_offset_result = appimage_offset.stdout.decode()

        self._offset = int(appimage_offset_result)

    def _make_squashfs(self):
        f = open(self.file, 'rb')
        squash = open('/tmp/appimage-' + self.md5 + '.squashfs', 'wb')
        f.seek(self.offset)
        read = f.read(1024)
        while read != b'':
            squash.write(read)
            read = f.read(1024)
        f.close()
        squash.close()
        return '/tmp/appimage-' + self.md5 + '.squashfs'

    def _unsquashfs(self):
        unsquash = subprocess.run([
                'unsquashfs',
                '-d',
                '/tmp/appimage-' + self.md5,
                '/tmp/appimage-' + self.md5 + '.squashfs'
            ],
            stdout=subprocess.PIPE
        )
        return '/tmp/appimage-' + self.md5

    def _unmount(self, rmdir=True):
        contents = os.listdir('/tmp/appimage-' + self.md5)
        for i in contents:
            file_to_delete = os.path.join('/tmp/appimage-' + self.md5, i)
            if os.path.isfile(file_to_delete) or os.path.islink(file_to_delete):
                os.remove(file_to_delete)
            if os.path.isdir(file_to_delete) and os.path.islink(file_to_delete):
                os.remove(file_to_delete)
            if os.path.isdir(file_to_delete):
                shutil.rmtree(file_to_delete)
        if rmdir is False:
            pass
        os.removedirs('/tmp/appimage-' + self.md5)

    def _delete_squashfs(self):
        os.remove('/tmp/' + 'appimage-' + self.md5 + '.squashfs')

    @property
    def file(self):
        return self._file

    @property
    def name(self):
        return os.path.basename(self.file)

    @property
    def md5(self):
        return self._md5

    @property
    def offset(self):
        return self._offset

    def save_metadata(self, cache_dir):
        self._make_squashfs()
        unsquashed = self._unsquashfs()

        # Do save things.
        # Make directory if not.
        if not os.path.isdir(cache_dir):
            os.makedirs(cache_dir)
        desktop = None
        icons = None
        icon = None
        # Copy .desktop file.
        contents = os.listdir(unsquashed)
        for i in contents:
            if i.endswith('.desktop'):
                desktop = i
        desktop_path = os.path.join(unsquashed, desktop)
        shutil.copyfile(desktop_path, os.path.join(cache_dir, desktop))
        # Save md5.
        f = open(os.path.join(cache_dir, 'md5'), 'w')
        f.write(self.md5)
        f.close()
        # Copy icons.
        # Copy icon.

        self._unmount()
        self._delete_squashfs()
