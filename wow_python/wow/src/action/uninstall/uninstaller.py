from src.wow_config import WowConfig
from src.exception import WowException

import logging


class Uninstaller:
    def uninstall(self, packagename):
        packages = WowConfig.list_packages(packagename)
        if len(packages) == 0:
            raise WowException('No package with this name')
        for package in packages:
            logging.info('Removing %s version %s', packagename, package.version())

