from src.archive import Archive
from src.wow_config import WowConfig
from src.package import Package
import os


class Extractor:
    filename = ''

    def destination(self):
        return os.path.join(WowConfig.install_folder, os.path.splitext(os.path.basename(self.filename))[0])

    def extract(self, filename):
        self.filename = filename
        Archive.extract(filename, self.destination())

        config_file = os.path.join(self.destination(), 'wow.yml')
        config = Package(config_file)
        config.load()

        for filepath in config.all_executables():
            filename = os.path.basename(filepath)
            Extractor.symlink(os.path.join(self.destination(), filepath), os.path.join(WowConfig.link_folder, filename))

    @staticmethod
    def symlink(src, dest):
        os.symlink(
            os.path.abspath(src),
            os.path.abspath(dest))