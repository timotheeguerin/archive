import os
from src import utils
from src.package import Package

import logging


class WowConfig:
    """
        Wow application configuration
    """

    install_folder = 'install'

    link_folder = 'bin'


    @staticmethod
    def list_packages(name=None):
        """
            List all the package installed
        """
        packages = []
        for folder in utils.list_subdir(WowConfig.install_folder):
            config_file = os.path.join(WowConfig.install_folder, folder, 'wow.yml')
            if os.path.isfile(config_file):
                package = Package(config_file)
                package.load()
                if name is None or package.name() == name:
                    packages.append(package)
            else:
                logging.warning("Error this folder `%s` doesn't have a config file", folder)
        return packages

